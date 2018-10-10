import itertools
import tempfile
from collections import deque

import pytest

from tasks import (bonus_tree_walker, cached, fibonacci_closure,
                   fibonacci_generator, filter_file, incrementor, sort_file)


def test_filter_file():
    with tempfile.NamedTemporaryFile() as tmp:
        lines = [
            "my car is awesome",
            "but it is so slow",
            "is this your car?",
            "no, this is Patrick"
        ]
        tmp.write('\n'.join(lines).encode('utf-8'))
        tmp.file.flush()
        assert filter_file(tmp.name, 'car') == [lines[0], lines[2]]


def test_sort_file():
    with tempfile.NamedTemporaryFile() as src:
        with tempfile.NamedTemporaryFile() as dst:
            assert sort_file(src.name, dst.name) == 'ok'

    with tempfile.NamedTemporaryFile() as src:
        with tempfile.NamedTemporaryFile() as dst:
            lines = [
                "dceb",
                "abc",
                "fff"
            ]
            src.write('\n'.join(lines).encode('utf-8'))
            src.file.flush()
            assert sort_file(src.name, dst.name) == 'ok'

            result = dst.file.readlines()
            assert [r.strip().decode('utf-8') for r in result] == sorted(lines)

    assert sort_file('missing-file.txt', 'out.txt') == 'file not found'

    import os, stat
    with tempfile.NamedTemporaryFile() as src:
        with tempfile.NamedTemporaryFile() as dst:
            os.chmod(dst.name, stat.S_IREAD)
            assert sort_file(src.name, dst.name) == 'error'


def test_incrementor():
    inc = incrementor(5)
    assert inc(-1) == 4
    assert inc(0) == 5
    assert inc(1) == 6
    assert inc(1332) == 1337
    assert inc(10.5) == 15.5

    inc = incrementor()
    assert inc(0) == 1
    assert inc(-5) == -4


def test_fibonacci_closure():
    f = fibonacci_closure()
    q = deque((f(), f()), maxlen=2)

    assert q[0] == 1
    assert q[1] == 1

    for _ in range(1000):
        x = f()
        assert x == sum(q)
        q.append(x)


def test_fibonacci_generator():
    g = fibonacci_generator()
    assert next(g) == 1

    q = deque((0, 1), maxlen=2)
    for i in itertools.islice(g, 1000):
        assert i == sum(q)
        q.append(i)



def test_cached():
    counts = 0

    @cached
    def counter(a):
        nonlocal counts
        counts += 1
        return counts

    assert counter(1) == 1
    assert counter(1) == 1
    assert counter(3) == 2
    assert counter(1) == 3
    assert counter(None) == 4
    assert counter(None) == 4
    assert counter(None) == 4
    assert counter([1, 2, 3]) == 5
    assert counter(0) == 6
    assert counter('') == 7


def test_bonus_tree_walker():
    tree = (((None, 8, None), 3, (None, 4, None)), 5, (None, 1, None))
    assert list(bonus_tree_walker(tree, 'inorder')) == [8, 3, 4, 5, 1]
    assert list(bonus_tree_walker(tree, 'preorder')) == [5, 3, 8, 4, 1]
    assert list(bonus_tree_walker(tree, 'postorder')) == [8, 4, 3, 1, 5]

    assert list(bonus_tree_walker((None, 1, None), 'postorder')) == [1]

    tree = (((None, 1, None), 2, ((None, 3, None), 4, (None, 5, None))), 6, (None, 7, ((None, 9, None), 8, None)))
    assert list(bonus_tree_walker(tree, 'inorder')) == [1, 2, 3, 4, 5, 6, 7, 9, 8]
    assert list(bonus_tree_walker(tree, 'preorder')) == [6, 2, 1, 4, 3, 5, 7, 8, 9]
    assert list(bonus_tree_walker(tree, 'postorder')) == [1, 3, 5, 4, 2, 9, 8, 7, 6]
