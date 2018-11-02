import math


class Vector:
    """
    Implement the methods below to create an immutable 3D vector class.
    Each implemented method will award you half a point.

    Magic methods cheatsheet: https://rszalski.github.io/magicmethods
    """

    """
    Implement a constructor that takes three coordinates (x, y, z) and stores
    them as attributes with the same names in the Vector.
    Default value for all coordinates should be 0.
    Example:
        v = Vector(1.2, 3.5, 4.1)
        v.x # 1.2
        v = Vector(z=1) # == Vector(0, 0, 1)
    """
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    """
    Implement method `length` that returns the length of the vector
    (https://chortle.ccsu.edu/VectorLessons/vch04/vch04_8.html).
    Example:
        Vector(2, 3, 4).length() # 5.38...
    """
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    """
    Implement vector addition and subtraction using `+` and `-` operators.
    Both operators should return a new vector and not modify its operands.
    If the second operand isn't a vector, raise ValueError.
    Example:
        Vector(1, 2, 3) + Vector(4, 5, 6) # Vector(5, 7, 8)
        Vector(1, 2, 3) - Vector(4, 5, 6) # Vector(-3, -3, -3)
    Hint:
        You can use isinstance(object, class) to check whether `object` is an instance of `class`.
    """
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ValueError
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise ValueError
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    """
    Implement vector negation using the unary `-` operator.
    Return a new vector, don't modify the input vector.
    Example:
        -Vector(1, 2, 3) # Vector(-1, -2, -3)
    """
    def __neg__(self):
        return Vector(- self.x, - self.y, - self.z)

    """
    Implement multiplication and division by scalar using `*` and `/` operators.
    Both operators should return a new Vector and not modify the input vector.
    If the second operand isn't `int` or `float`, raise ValueError.
    Example:
        Vector(1, 2, 3) * 4 # Vector(4, 8, 12)
        Vector(2, 4, 6) / 2 # Vector(1, 2, 3)
    Hint:
        Division with the `/` operator uses the magic method `__truediv__` in Python 3.
    """
    def __mul__(self, other: float):
        if not isinstance(other, int) and not isinstance(other, float):
            raise ValueError
        return Vector(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: float):
        if not isinstance(other, int) and not isinstance(other, float):
            raise ValueError
        return Vector(self.x / other, self.y / other, self.z / other)

    """
    Implement the `==` comparison operator for Vector that returns True if both vectors have the same attributes.
    If the second operand isn't a vector, return False.
    Example:
        Vector(1, 1, 1) == Vector(1, 1, 1)  # True
        Vector(1, 1, 1) == Vector(2, 1, 1)  # False
        Vector(1, 2, 3) == 5                # False
    """
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False

        if self.x != other.x or self.y != other.y or self.z != other.z:
            return False

        return True

    """
    Implement *property* `unit` that will return the unit vector of this vector
    (vector with the same direction and length one).
    If the vector has length zero, return a zero vector (Vector(0, 0, 0)).
    Example:
        Vector(0, 8, 0).unit # Vector(0, 1, 0)
    """

    """
    Implement string representation of Vector in the form `(x, y, z)`.
    Example:
        str(Vector(1, 2, 3))    # (1, 2, 3)
        print(Vector(0, 0, 0))  # (0, 0, 0)
    """

    """
    Implement indexing for the vector, both for reading and writing.
    If the index is out of range (> 2), raise IndexError.
    Example:
        v = Vector(1, 2, 3)
        v[0] # 1
        v[2] # 3
        v[1] = 5 # v.y == 5

        v[10] # raises IndexError
    """

    """
    Implement the iterator protocol for the vector.
    Hint:
        Use `yield`.
    Example:
        v = Vector(1, 2, 3)
        for x in v:
            print(x) # prints 1, 2, 3
    """


class LowerCaseDecorator:
    """
    Points: 1

    Implement the `decorator` design pattern.
    LowerCaseDecorator should decorate a file which will be passed to its constructor.
    It should make all characters/strings written to the file lowercase.
    It is enough to support the `write` and `writelines` methods of file.
    Example:
        with open("file.txt", "w") as f:
            decorated = LowerCaseDecorator(f)
            decorated.write("Hello World\n")
            decorated.writelines(["Nice to MEET\n", "YOU"])

        file.txt content after the above code is executed:
        hello world
        nice to meet
        you
    """
    pass


class BonusObservable:
    """
    Points: 1 (bonus)

    Implement the `observer` design pattern.
    Observable should have a `subscribe` method for adding new subscribers.
    It should also have a `notify` method that calls all of the stored subscribers and passes them its parameters.
    Example:
        obs = BonusObservable()

        def fn1(x):
            print("fn1: {}".format(x))

        def fn2(x):
            print("fn2: {}".format(x))

        unsub1 = obs.subscribe(fn1)     # fn1 will be called everytime obs is notified
        unsub2 = obs.subscribe(fn2)     # fn2 will be called everytime obs is notified
        obs.notify(5)                   # should call fn1(5) and fn2(5)
        unsub1()                        # fn1 is no longer subscribed
        obs.notify(6)                   # should call fn2(6)
    """

    def subcribe(self, subscriber):
        """
        Add subscriber to collection of subscribers.
        Return a function that will remove this subscriber from the collection when called.
        """
        pass

    def notify(self):
        """
        Pass all parameters given to this function to all stored subscribers by calling them.
        """
        pass
