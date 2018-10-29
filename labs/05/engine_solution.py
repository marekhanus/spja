import sys
from random import Random

import pygame
from pygame.locals import K_SPACE, K_DOWN, K_UP, K_LEFT, K_RIGHT, KEYDOWN, \
    KEYUP

from utils import load_image, Cooldown

EVENT_SPAWN_ENEMY = pygame.USEREVENT


class Explosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = load_image('images/explosion_anim.jpg')
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.crop = (64, 64)
        self.dim = 4
        self.cooldown = Cooldown(220)
        self.back = False

    def update(self, engine, delta):
        self.cooldown.update(delta)

        if self.cooldown.reset_if_ready():
            if self.back:
                self.kill()
            else:
                self.back = True

    def draw(self, surface):
        target = pygame.rect.Rect((0, 0), self.crop)
        target.center = self.rect.center

        surface.blit(self.image, target, area=self.get_crop())

    def get_crop(self):
        progress = self.cooldown.progress
        frame_count = self.dim ** 2
        index = int(progress * frame_count) % frame_count

        if self.back:
            index = frame_count - index - 1

        dim = self.dim - 1
        x = dim - (index % self.dim)
        y = dim - (index // self.dim)

        cx = x * self.crop[0]
        cy = y * self.crop[1]

        return pygame.rect.Rect((cx, cy), self.crop)


class Missile(pygame.sprite.Sprite):
    def __init__(self, player, pos, damage=20, speed=700):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('images/bullet.gif')
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.player = player
        self.damage = damage
        self.speed = speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, engine, delta):
        self.rect = self.rect.move(0, -self.speed * delta)

        _, y = self.rect.center
        if y <= 0:
            self.kill()

        collisions = pygame.sprite.spritecollide(self, engine.enemies, False)
        if collisions:
            for enemy in collisions:
                if enemy.receive_damage(self.damage):
                    self.player.on_enemy_destroyed(enemy)
                self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos, health=100, score=10, speed=100):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.health = health
        self.score = score
        self.speed = speed

    def update(self, engine, delta):
        self.rect = self.rect.move(0, self.speed * delta)

        _, y = self.rect.center
        if y >= engine.screen.get_height():
            engine.player.lose_health()
            self.kill()
        if pygame.sprite.spritecollide(self, [engine.player], False):
            engine.player.lose_health()
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def receive_damage(self, damage):
        self.health -= damage

        if self.health <= 0:
            self.kill()
            return True
        return False


class Player(pygame.sprite.Sprite):
    def __init__(self, engine, pos):
        super().__init__()

        self.image_straight = load_image('images/plane.gif')
        self.image_left = load_image('images/plane_turning_right_1.gif')
        self.image_right = load_image('images/plane_turning_left_1.gif')
        self.rect = self.image_straight.get_rect()
        self.rect.center = pos

        self.engine = engine
        self.image = self.image_straight

        self.speed = [0, 0]  # [x, y]
        self.health = 3
        self.score = 0

        self.missiles = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.font = pygame.font.Font(None, 36)
        self.cooldown = Cooldown(150)

        self.explosion_sound = pygame.mixer.Sound('sound/explosion.wav')

        self.key = {
            K_RIGHT: False,
            K_LEFT: False,
            K_UP: False,
            K_DOWN: False,
            K_SPACE: False
        }

    def handle_keys(self, event):
        if event.type not in (KEYDOWN, KEYUP):
            return

        speed_value = 500

        if event.key in self.key:
            self.key[event.key] = event.type == KEYDOWN

        image = self.image_straight
        speed = [0, 0]
        if self.key[K_RIGHT]:
            speed[0] = speed_value
            image = self.image_right
        if self.key[K_LEFT]:
            speed[0] = -speed_value
            image = self.image_left
        if self.key[K_UP]:
            speed[1] = -speed_value
        if self.key[K_DOWN]:
            speed[1] = speed_value

        self.speed = speed
        self.image = image

    def update(self, engine, delta):
        x, y = self.speed
        rect = self.rect
        self.rect = self.rect.move(x * delta, y * delta)
        if (self.rect.left <= 0 or
                self.rect.right >= engine.screen.get_width() or
                self.rect.top <= 0 or
                self.rect.bottom >= engine.screen.get_height()):
            self.rect = rect

        self.cooldown.update(delta)

        if self.key[K_SPACE] and self.cooldown.reset_if_ready():
                self.spawn_missile()

        self.missiles.update(engine, delta)
        self.explosions.update(engine, delta)

    def draw(self, surface):
        for missile in self.missiles:
            missile.draw(surface)
        for explosion in self.explosions:
            explosion.draw(surface)

        surface.blit(self.image, self.rect)
        self.draw_status(surface)

    def draw_status(self, screen):
        if pygame.font:
            # draw score
            text = self.font.render('Score: {}'.format(self.score), 1,
                                    (255, 0, 0))
            textpos = text.get_rect(centerx=screen.get_width() / 2)
            screen.blit(text, textpos)

            # draw health
            text = self.font.render('Health: {}'.format(self.health), 1,
                                    (0, 255, 0))
            textpos = text.get_rect(centerx=screen.get_width() / 2, centery=40)
            screen.blit(text, textpos)

    def lose_health(self):
        self.health -= 1
        if self.health <= 0:
            self.engine.end()

    def on_enemy_destroyed(self, enemy):
        self.score += enemy.score
        self.explosions.add(Explosion(enemy.rect.center))
        self.explosion_sound.play()

    def spawn_missile(self):
        missile = Missile(self, self.rect.center)
        self.missiles.add(missile)


class Engine:
    def __init__(self, width=640, height=480):
        pygame.init()
        pygame.mixer.init()

        pygame.display.set_caption('SPJA invaders')
        pygame.key.set_repeat(100, 30)
        pygame.time.set_timer(EVENT_SPAWN_ENEMY, 3000)

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()

        self.player = Player(self, (self.width / 2, self.height - 20))
        self.enemies = pygame.sprite.Group()
        self.random = Random()

        self.spawn_enemy()

    def main_loop(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

        while True:
            self.handle_keys()
            self.update()
            self.draw()

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == EVENT_SPAWN_ENEMY:
                self.spawn_enemy()
            else:
                self.player.handle_keys(event)

    def update(self):
        delta = self.clock.tick(60) / 1000

        self.enemies.update(self, delta)
        self.player.update(self, delta)

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        for enemy in self.enemies:
            enemy.draw(self.screen)
        self.player.draw(self.screen)

        pygame.display.flip()

    def spawn_enemy(self):
        start = 20
        end = self.screen.get_width() - start
        x = self.random.randint(start, end)

        image = self.select_enemy_image()
        enemy = Enemy(image, (x, -20), speed=100)
        self.enemies.add(enemy)

    def end(self):
        print("GAME OVER")
        exit(0)

    def select_enemy_image(self):
        images = (
            'images/enemy1.gif',
            'images/enemy2.gif',
            'images/enemy3.gif',
            'images/enemy4.gif',
            'images/enemy5.gif'
        )
        return load_image(self.random.choice(images))


if __name__ == '__main__':
    engine = Engine()
    engine.main_loop()
