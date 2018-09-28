def factorial(n):
    """
    0.5 point
    Return the factorial of `n`.
    Example:
        factorial(0) == 1
        factorial(1) == 1
        factorial(5) == 120
    """
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


def dot_product(a, b):
    """
    0.5 point
    Calculate the dot product of `a` and `b`.
    Assume that `a` and `b` have same length.
    Hint:
        lookup `zip` function
    Example:
        dot_product([1, 2, 3], [0, 3, 4]) == 1*0 + 2*3 + 3*4 == 18
    """
    res = 0

    for i, v in enumerate(a):
        res += a[i] * b[i]

    return res


def is_palindrome(data):
    """
    0.5 point
    Returns True if `data` is a palindrome and False otherwise.
    Hint:
        slicing is your friend, use it
    Example:
        is_palindrome('aba') == True
        is_palindrome('abc') == False
    """
    last = len(data) - 1

    for i, v in enumerate(data):
        if v != data[last - i]:
            return False

    return True


def lex_compare(a, b):
    """
    1 point
    Lexicographically compare `a` with `b` and return the smaller string.
    Example:
        lex_compare('a', 'b') == 'a'
        lex_compare('ahoj', 'buvol') == 'ahoj'
        lex_compare('ahoj', 'ahojky') == 'ahoj'
        lex_compare('dum', 'automobil') == 'automobil'
    """
    a_last = len(a) - 1
    b_last = len(b) - 1

    for i, v in enumerate(a):
        if (i == a_last) or (v < b[i]):
            return a
        elif (i == b_last) or (v > b[i]):
            return b

    return ''


def redact(data, chars):
    """
    1 point
    Return `data` with all characters from `chars` replaced by the character 'x'.
    Characters are case insensitive.
    Example:
        redact("Hello world!", "lo")        # Hexxx wxrxd!
        redact("Secret message", "mse")     # xxcrxt xxxxagx
    """
    for char in chars:
        data = data.replace(char.lower(), 'x').replace(char.upper(), 'x')

    return data


def std_dev(data):
    """
    1 point
    Return the (population) standard deviation of `data`.
    Assume that `data` is non-empty.
    Equation: √(Σᵢ((xᵢ - x̅̅)²) / |data|)
    (sqrt(sum(square(xi - mean)) / len(data))
    """
    avg = sum(data) / len(data)
    res = 0

    for v in data:
        res += pow(v - avg, 2)

    return pow(res / len(data), 0.5)


def count_words(data):
    """
    0.5 point
    Return a dictionary that maps word -> number of occurences in `data`.
    Words are separated by spaces (' ').
    Characters are case sensitive.

    Hint:
        "hi there".split(" ") -> ["hi", "there"]

    Example:
        count_words('this car is my favourite what car is this')
        {
            'this': 2,
            'car': 2,
            'is': 2,
            'my': 1,
            'favourite': 1,
            'what': 1
        }
    """
    data_split = data.split(' ')
    res = {}

    for item in data_split:
        if item == '':
            pass
        elif item in res:
            res[item] = res.get(item) + 1
        else:
            res.update({item: 1})

    return res


def bonus_utf8(cp):
    """
    1 point (bonus)
    Encode `cp` (a Unicode code point) into 1-4 UTF-8 bytes - you should know this from `Logické obvody`.
    Example:
        bonus_utf8(0x01) == [0x01]
        bonus_utf8(0x1F601) == [0xF0, 0x9F, 0x98, 0x81]

    RFC 2279: http://www.faqs.org/rfcs/rfc2279.html

    Bit count   UCS-4 range (hex.)  UTF-8 octet sequence (binary)
    7 bit       0000 007F           0xxxxxxx
    11 bit      0000 07FF           110xxxxx 10xxxxxx
    16 bit      0000 FFFF           1110xxxx 10xxxxxx 10xxxxxx
    21 bit      001F FFFF           11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
    26 bit      03FF FFFF           111110xx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
    31 bit      7FFF FFFF           1111110x 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx
                    |                  |         |        |        |        |        |
    last position --                   |         |        |        |        |        |
                                       |         |        |        |        |        |
              leading sequence --------          --------------------------------------------- continuation sequences
       7 bit: 00000000 => 0x0                                                                  10xxxxxx
      11 bit: 11000000 => 0xC0                               For filtering only `x` positions: 00111111 => 0x3F
      16 bit: 11100000 => 0xE0                                                Sequence prefix: 10000000 => 0x80
      21 bit: 11110000 => 0xF0                                             Variable `x` count: 6        => 0x6
      26 bit: 11111000 => 0xF8
      31 bit: 11111100 => 0xFC

                  U + 1    F    6    0    1
                   0001 1111 0110 0000 0001

    1111 0xxx | 10xx xxxx | 10xx xxxx | 10xx xxxx
    1111 0000 | 1001 1111 | 1001 1000 | 1000 0001
       F    0 |    9    F |    9    8 |    8    1
    """

    # last position x bit
    last_pos_7bit = 0x7F
    last_pos_11bit = 0x7FF
    last_pos_16bit = 0xFFFF
    last_pos_21bit = 0x1FFFFF
    last_pos_26bit = 0x3FFFFFF
    last_pos_31bit = 0x7FFFFFFF

    # leading sequence x bit prefix
    lead_seq_7bit_pref = 0x0
    lead_seq_11bit_pref = 0xC0
    lead_seq_16bit_pref = 0xE0
    lead_seq_21bit_pref = 0xF0
    lead_seq_26bit_pref = 0xF8
    lead_seq_31bit_pref = 0xFC

    # continuation sequence
    cont_seq_filter = 0x3F
    cont_seq_pref = 0x80
    cont_seq_shift = 0x6

    if cp <= last_pos_7bit:
        return [
            (cp >> 0 * cont_seq_shift) + lead_seq_7bit_pref,
        ]
    elif cp <= last_pos_11bit:
        return [
            (cp >> 1 * cont_seq_shift) + lead_seq_11bit_pref,
            (cp >> 0 * cont_seq_shift & cont_seq_filter) + cont_seq_pref,
        ]
    elif cp <= last_pos_16bit:
        return [
            (cp >> 2 * cont_seq_shift) + lead_seq_16bit_pref,
            (cp >> 1 * cont_seq_shift & cont_seq_filter) + cont_seq_pref,
            (cp >> 0 * cont_seq_shift & cont_seq_filter) + cont_seq_pref,
        ]
    elif cp <= last_pos_21bit:
        return [
            (cp >> 3 * cont_seq_shift) + lead_seq_21bit_pref,
            (cp >> 2 * cont_seq_shift & cont_seq_filter) + cont_seq_pref,
            (cp >> 1 * cont_seq_shift & cont_seq_filter) + cont_seq_pref,
            (cp >> 0 * cont_seq_shift & cont_seq_filter) + cont_seq_pref,
        ]
    elif cp <= last_pos_26bit:
        return [
            (cp >> 4 * cont_seq_shift) + lead_seq_26bit_pref,
            (cp >> 3 * cont_seq_shift & cont_seq_filter) + cont_seq_pref,
            (cp >> 2 * cont_seq_shift & cont_seq_filter) + cont_seq_pref,
            (cp >> 1 * cont_seq_shift & cont_seq_filter) + cont_seq_pref,
            (cp >> 0 * cont_seq_shift & cont_seq_filter) + cont_seq_pref,
        ]
    elif cp <= last_pos_31bit:
        return [
            (cp >> 5 * cont_seq_shift) + lead_seq_31bit_pref,
            (cp >> 4 * cont_seq_shift & cont_seq_filter) + cont_seq_pref,
            (cp >> 3 * cont_seq_shift & cont_seq_filter) + cont_seq_pref,
            (cp >> 2 * cont_seq_shift & cont_seq_filter) + cont_seq_pref,
            (cp >> 1 * cont_seq_shift & cont_seq_filter) + cont_seq_pref,
            (cp >> 0 * cont_seq_shift & cont_seq_filter) + cont_seq_pref,
        ]
    return None
