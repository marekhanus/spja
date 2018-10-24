import pygame
from pygame.constants import RLEACCEL

image_cache = {}


def load_image(name, colorkey=-1):
    if name in image_cache:
        return image_cache[name].copy()

    try:
        image = pygame.image.load(name)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)

    image_cache[name] = image
    return image


class Cooldown:
    """
    Represents time cooldown in milliseconds.
    """
    def __init__(self, time_ms):
        self.cooldown = time_ms / 1000.0
        self.time = 0

    def update(self, delta):
        """
        Updates the timer.
        :param delta: Time in milliseconds.
        """
        self.time += delta

    def reset(self):
        self.time = 0

    @property
    def progress(self):
        return self.time / self.cooldown

    @property
    def ready(self):
        """
        Returns true if the cooldown is ready.
        """
        return self.time >= self.cooldown

    def reset_if_ready(self):
        """
        Same as ready, but also resets the cooldown if it's ready.
        """
        ready = self.ready
        if ready:
            self.reset()
        return ready
