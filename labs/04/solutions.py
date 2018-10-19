import math


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, rhs):
        if not isinstance(rhs, Vector):
            raise ValueError()
        return Vector(self.x + rhs.x, self.y + rhs.y, self.z + rhs.z)

    def __sub__(self, rhs):
        if not isinstance(rhs, Vector):
            raise ValueError()
        return Vector(self.x - rhs.x, self.y - rhs.y, self.z - rhs.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __mul__(self, rhs):
        if isinstance(rhs, int) or isinstance(rhs, float):
            return Vector(self.x * rhs, self.y * rhs, self.z * rhs)
        else:
            raise ValueError()

    def __truediv__(self, rhs):
        if isinstance(rhs, int) or isinstance(rhs, float):
            return Vector(self.x / rhs, self.y / rhs, self.z / rhs)
        else:
            raise ValueError()

    def __eq__(self, rhs):
        if not isinstance(rhs, Vector):
            return False
        return self.x == rhs.x and self.y == rhs.y and self.z == rhs.z

    @property
    def unit(self):
        if self.x == 0 and self.y == 0 and self.z == 0:
            return Vector(0, 0, 0)
        return self / self.length()

    def __getitem__(self, index):
        return (self.x, self.y, self.z)[index]

    def __setitem__(self, index, val):
        if index == 0:
            self.x = val
        elif index == 1:
            self.y = val
        elif index == 2:
            self.z = val
        else:
            raise IndexError()

        """
        or replace conditions with table lookup:
        mapping = {
            0: 'x',
            1: 'y',
            2: 'z'
        }
        self.__dict__[mapping[index]] = val
        """

    def __iter__(self):
        for attribute in (self.x, self.y, self.z):
            yield attribute
        """
        or
        yield from iter((self.x, self.y, self.z))
        or simply
        yield self.x
        yield self.y
        yield self.z
        """

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)


class LowerCaseDecorator:
    def __init__(self, f):
        self.f = f

    def write(self, data):
        self.f.write(data.lower())

    def writelines(self, lines):
        self.f.writelines(l.lower() for l in lines)


class BonusObservable:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

        def rm():
            if subscriber in self.subscribers:
                self.subscribers.remove(subscriber)
        return rm

    def notify(self, *args, **kwargs):
        for s in self.subscribers:
            s(*args, **kwargs)
