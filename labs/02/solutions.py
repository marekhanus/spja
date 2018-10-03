import math
from functools import wraps


def factorial(n):
    if n == 0:
        return 1

    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def dot_product(a, b):
    return sum(a * b for (a, b) in zip(a, b))


def is_palindrome(data):
    return data == data[::-1]


def lex_compare(a, b):
    for (i, j) in zip(a, b):
        if i < j:
            return a
        elif i > j:
            return b
    if len(a) <= len(b):
        return a
    else:
        return b

    # or just [b, a][a < b]


def redact(data, chars):
    chars = [c.lower() for c in chars]
    result = []
    for d in data:
        if d.lower() in chars:
            result.append('x')
        else:
            result.append(d)
    return ''.join(result)


def std_dev(data):
    avg = sum(data) / len(data)
    sub = [math.pow(d - avg, 2) for d in data]
    dev = sum(sub) / len(sub)
    return math.sqrt(dev)


def count_words(data):
    mapping = {}
    for word in data.split(" "):
        if word:
            mapping[word] = mapping.get(word, 0) + 1
    return mapping


def bonus_utf8(cp):
    import math

    def comp(bits):
        num = cp
        res = []
        byte_count = math.ceil(bits / 6)

        while bits >= 6:
            res.append(0x80 | (num & 0b00111111))
            num >>= 6
            bits -= 6

        if bits:
            s = 0xC0
            mask = 0b00100000
            for _ in range(byte_count - 2):
                s |= mask
                mask >>= 1
            s |= num & ((1 << bits) - 1)
            res.append(s)

        return reversed(res)

    if cp <= 0x7F:
        return [cp]
    elif cp <= 0x7FF:
        return comp(11)
    elif cp <= 0xFFFF:
        return comp(16)
    elif cp <= 0x1FFFFF:
        return comp(21)
