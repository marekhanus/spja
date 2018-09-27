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
    pass


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
    pass


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
    pass


def redact(data, chars):
    """
    1 point
    Return `data` with all characters from `chars` replaced by the character 'x'.
    Characters are case insensitive.
    Example:
        redact("Hello world!", "lo")        # Hexxx wxrxd!
        redact("Secret message", "mse")     # xxcrxt xxxxagx
    """
    pass


def std_dev(data):
    """
    1 point
    Return the (population) standard deviation of `data`.
    Assume that `data` is non-empty.
    Equation: √(Σᵢ((xᵢ - x̅̅)²) / |data|)
    (sqrt(sum(square(xi - mean)) / len(data))
    """
    pass


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
    pass


def bonus_utf8(cp):
    """
    1 point (bonus)
    Encode `cp` (a Unicode code point) into 1-4 UTF-8 bytes - you should know this from `Logické obvody`.
    Example:
        bonus_utf8(0x01) == [0x01]
        bonus_utf8(0x1F601) == [0xF0, 0x9F, 0x98, 0x81]
    """
    pass
