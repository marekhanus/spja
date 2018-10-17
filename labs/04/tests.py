import tempfile

import pytest
from tasks import Vector, LowerCaseDecorator, BonusObservable


def test_vector_init():
    vec = Vector(1.2, 3.4, 5.6)
    assert vec.x == 1.2
    assert vec.y == 3.4
    assert vec.z == 5.6

    vec = Vector()
    assert vec.x == 0
    assert vec.y == 0
    assert vec.z == 0

    vec = Vector(z=3)
    assert vec.x == 0
    assert vec.y == 0
    assert vec.z == 3


def test_vector_length():
    assert Vector(0, 0, 0).length() == 0
    assert Vector(1, 0, 0).length() == 1
    assert "{:.3f}".format(Vector(10, 12, 13).length()) == "20.322"


def test_vector_add():
    a = Vector(1, 2, 3)
    b = Vector(3, 4, 5)
    c = a + b

    assert a.x == 1
    assert a.y == 2
    assert a.z == 3
    assert b.x == 3
    assert b.y == 4
    assert b.z == 5
    assert c.x == 4
    assert c.y == 6
    assert c.z == 8

    with pytest.raises(ValueError):
        Vector(1, 2, 3) + 5


def test_vector_sub():
    a = Vector(1, 2, 3)
    b = Vector(3, 4, 5)
    c = a - b

    assert a.x == 1
    assert a.y == 2
    assert a.z == 3
    assert b.x == 3
    assert b.y == 4
    assert b.z == 5
    assert c.x == -2
    assert c.y == -2
    assert c.z == -2

    with pytest.raises(ValueError):
        Vector(1, 2, 3) - 5


def test_vector_neg():
    a = -Vector(1, 2, 3)
    assert a.x == -1
    assert a.y == -2
    assert a.z == -3

    a = -Vector(0, 0, 0)
    assert a.x == 0
    assert a.y == 0
    assert a.z == 0


def test_vector_mul():
    a = Vector(1, 2, 3)
    b = a * 5
    assert a.x == 1
    assert b.x == 5
    assert b.y == 10
    assert b.z == 15

    b = a * 5.0
    assert b.x == 5
    assert b.y == 10
    assert b.z == 15

    with pytest.raises(ValueError):
        Vector(1, 2, 3) * "1"


def test_vector_div():
    a = Vector(2, 4, 6)
    b = a / 2
    assert a.x == 2
    assert b.x == 1
    assert b.y == 2
    assert b.z == 3

    b = a / 2.0
    assert b.x == 1
    assert b.y == 2
    assert b.z == 3

    with pytest.raises(ValueError):
        Vector(1, 2, 3) / "1"


def test_vector_eq():
    assert Vector(0, 0, 0) == Vector(0, 0, 0)
    assert Vector(1, 2, 3) == Vector(1, 2, 3)
    assert Vector(1, 2, 3) != Vector(1, 2, 4)
    assert Vector(1, 2, 3) != 5


def test_vector_unit():
    assert Vector(0, 0, 0).unit == Vector(0, 0, 0)
    assert Vector(0, 8, 0).unit == Vector(0, 1, 0)


def test_vector_str():
    assert str(Vector(0, 0, 0)) == "(0, 0, 0)"
    assert str(Vector(1, 2, 3)) == "(1, 2, 3)"


def test_vector_indexing():
    v = Vector(1, 2, 3)
    assert v[0] == 1
    assert v[2] == 3
    v[1] = 5
    assert v[1] == 5
    assert v.y == 5

    with pytest.raises(IndexError):
        a = v[10]

    with pytest.raises(IndexError):
        v[8] = 5


def test_vector_iteration():
    v = Vector(1, 2, 3)
    assert list(v) == [1, 2, 3]
    assert list(v) == [1, 2, 3]

    it = iter(v)
    assert it is not v

    it2 = iter(v)

    assert next(it) == 1
    assert next(it2) == 1


def test_lower_case_decorator():
    with tempfile.NamedTemporaryFile(mode="w+") as f:
        decorator = LowerCaseDecorator(f)
        decorator.write("Hello World\n")
        decorator.writelines(["Prefer\n", "compOSItioN OVeR\n", "INHERITance\n"])
        f.seek(0)
        assert """hello world
prefer
composition over
inheritance
""" == f.read()


def test_bonus_observable_complex():
    obs = BonusObservable()

    calls = [0, 0]

    def fn1(x):
        calls[0] += x

    def fn2(x):
        calls[1] += x

    unsub1 = obs.subscribe(fn1)
    unsub2 = obs.subscribe(fn2)

    assert calls == [0, 0]

    obs.notify(5)
    assert calls == [5, 5]

    unsub1()
    obs.notify(6)
    assert calls == [5, 11]
    unsub2()

    obs.notify(3)
    assert calls == [5, 11]

    args = [None, None]

    def fn3(*p, **kw):
        args[0] = p
        args[1] = kw

    obs.subscribe(fn3)
    obs.notify(1, 2, 3, a=5, b=6)
    assert args == [(1, 2, 3), {"a": 5, "b": 6}]
