"""
Magic methods cheatsheet: https://rszalski.github.io/magicmethods
Design patterns: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/PatternConcept.html
"""


class Car:
    def __init__(self, engine):
        self.engine = engine
        self.emissions = 0

    def drive(self):
        self.emissions += self.engine.drive()


class Engine:
    def drive(self): # similar to abstract method in C++, no implementation
        raise NotImplementedError()


class DieselEngine(Engine):
    def drive(self):
        return 5


class VolksWagenEngine(DieselEngine):
    def drive(self):
        emissions = super().drive()  # calling parent method
        return emissions / 2


class BankAccount:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Bank account can't be negative")
        self._amount = value


b = BankAccount(500)
b.amount = 100
try:
    b.amount = -100
except:
    pass


class Color:
    @staticmethod
    def white():
        return Color(1, 1, 1)

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def is_reddish(self):
        return self.r > self.g and self.r > self.b

    # magic methods
    def __add__(self, rhs):
        return Color(self.r + rhs.r, self.g + rhs.g, self.b + rhs.b)

    def __str__(self):
        return "rgb({}, {}, {})".format(self.r, self.g, self.b)


c = Color(0.5, 0.3, 0.2)
c.r = 0.2
c += Color(0, 0, 0.3)
r = c.is_reddish()
reddish = Color.is_reddish(c)
