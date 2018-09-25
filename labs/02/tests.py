import itertools
from collections import deque

from tasks import (bonus_utf8, count_words, dot_product, factorial,
                   is_palindrome, lex_compare, redact, std_dev)


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_dot_product():
    assert dot_product([1, 2, 3], [0, 3, 4]) == 18
    assert dot_product((-1,), (5,)) == -5
    assert "{:.2f}".format(dot_product((-5.6, 0, 10), (12, 8, 5))) == "-17.20"


def test_is_palindrome():
    assert is_palindrome('')
    assert is_palindrome('a')
    assert is_palindrome('aa')
    assert is_palindrome('aba')
    assert is_palindrome('bbbb')
    assert not is_palindrome('ab')
    assert not is_palindrome('abc')
    assert not is_palindrome('abca')


def test_lex_compare():
    assert lex_compare('a', 'b') == 'a'
    assert lex_compare('ahoj', 'buvol') == 'ahoj'
    assert lex_compare('ahoj', 'ahojky') == 'ahoj'
    assert lex_compare('dum', 'automobil') == 'automobil'
    assert lex_compare('', '') == ''
    assert lex_compare('abc', 'abd') == 'abc'
    assert lex_compare('dbe', 'dca') == 'dbe'


def test_redact():
    assert redact("Hello world!", "lo") == "Hexxx wxrxd!"
    assert redact("Secret message", "mse") == "xxcrxt xxxxagx"
    assert redact("No spaces allowed", " ") == "Noxspacesxallowed"
    assert redact("S", "s") == "x"
    assert redact("xxsx", "s") == "xxxx"
    assert redact("", []) == ""


def test_std_dev():
    assert "{:.5f}".format(std_dev([1, 3, 3, 5, -6, 8, 12])) == "5.22943"
    assert "{:.5f}".format(std_dev([5, 13, 17, 20, 2, 2, 1, 0, 90])) == "26.85765"


def test_count_words():
    assert count_words('this car is my favourite what car is this') == \
    {
        'this': 2,
        'car': 2,
        'is': 2,
        'my': 1,
        'favourite': 1,
        'what': 1
    }
    assert count_words('what happens in kernel mode stays in kernel mode') == \
    {
        'what': 1,
        'happens': 1,
        'in': 2,
        'kernel': 2,
        'mode': 2,
        'stays': 1
    }
    assert count_words('') == {}


def test_bonus_utf8():
    assert bytes(bonus_utf8(ord('0'))).decode('utf-8') == '0'
    assert bytes(bonus_utf8(ord('č'))).decode('utf-8') == 'č'
    assert bytes(bonus_utf8(ord('⤴'))).decode('utf-8') == '⤴'
    assert bytes(bonus_utf8(ord('😁'))).decode('utf-8') == '😁'
