import itertools
from collections import deque

from tasks import fizzbuzz


def test_fizzbuzz():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(25) == 'Buzz'
    assert fizzbuzz(8) == 8
    assert fizzbuzz(45) == 'FizzBuzz'
    assert fizzbuzz(1) == 1
    assert fizzbuzz(0) == 'FizzBuzz'
