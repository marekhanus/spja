def filter_file(path, keyword):
    """
    0.5 point
    Open file located at `path` and return all lines that contain the `keyword`.
    Strip line feeds from the lines.
    Example:
        filter_file('test.txt', 'car') == ['my car is awesome', 'is this your car?']

        test.txt:
        my car is awesome
        but it is so slow
        is this your car?
        no, this is Patrick
    """
    res = []

    with open(path, 'r') as f:
        for line in f.readlines():
            if keyword in line:
                res.append(line.strip())

    return res


def sort_file(source, target):
    """
    1 point
    Open file located at `source`, read its lines and sort them.
    Then output the sorted lines to the file located at `target`.

    Return 'ok' if everything was successful.
    Return 'file not found' if the `source` file was not found (FileNotFoundError).
    Return 'error' if anything else went wrong.

    Example:
        sort_file('from.txt', 'to.txt') == 'ok'

        from.txt:
        dceb
        abc
        fff

        to.txt
        abc
        dceb
        fff
    """
    try:
        with open(source, 'r') as f:
            lines = f.read()

        lines_sorted = sorted(lines.split('\n'))

        with open(target, 'r+') as f:
            f.write('\n'.join(lines_sorted))
            f.flush()
    except FileNotFoundError:
        return 'file not found'
    except:
        return 'error'

    return 'ok'


def incrementor(n=1):
    """
    0.5 point
    Return a function that will add `n` to its parameter.
    If this function receives no parameter, it should create an incrementor that adds 1 to its parameter.
    Example:
        inc = incrementor(5)
        inc(6) # 11
        inc(1) # 6

        inc = incrementor()
        inc(2) # 3
    """
    return lambda x: n + x


def fibonacci_closure():
    """
    2 points
    Return a closure that will generate elements of the Fibonacci sequence when called repeatedly.
    Example:
        g = fibonacci_closure()
        g() # 1
        g() # 1
        g() # 2
        g() # 3
        ...
    """
    x = fibonacci_generator()
    return lambda: next(x)


def fibonacci_generator():
    """
    2 points
    Return a generator that will generate elements of the Fibonacci sequence when iterated.
    Example:
        for i in fibonacci_generator():
            print(i)
        # 1, 1, 2, 3, 5 ...
    """
    yield 1
    a, b = 0, 1

    while True:
        a, b = b, a + b
        yield b


def cached(f):
    """
    2 points
    Create a decorator that caches the latest function result.
    When `f` is called multiple times in a row with the same parameter, compute the result just
    once and then return the result from cache.
    When `f` receives a different parameter, reset the cache and compute the new result.
    Assume that `f` receives exactly one parameter.
    Example:
        @cached
        def fn(a):
            return a + 1 # imagine an expensive computation

        fn(1) == 2 # computed
        fn(1) == 2 # returned from cache, fn is not called
        fn(3) == 4 # computed
        fn(1) == 2 # computed
    """
    cached_arg = cached_res = 0

    def drake(arg):
        nonlocal cached_arg, cached_res

        if arg != cached_arg:
            cached_arg, cached_res = arg, f(arg)

        return cached_res

    return drake


def bonus_tree_walker(tree, order):
    """
    1 point (bonus)
    Write a generator that traverses `tree` in the given `order` ('inorder', 'preorder' or 'postorder').
    You should know this from 'Algoritmy II'.
    The tree is represented with nested tuples (left subtree, value, right subtree).
    If there is no subtree, it will be marked as None.
    Example:
        tree = (((None, 8, None), 3, (None, 4, None)), 5, (None, 1, None))
            5
           / \
          3   1
         / \
        8   4
        list(bonus_tree_walker(tree, 'inorder')) == [8, 3, 4, 5, 1]
        list(bonus_tree_walker(tree, 'preorder')) == [5, 3, 8, 4, 1]
        list(bonus_tree_walker(tree, 'postorder')) == [8, 4, 3, 1, 5]
    """
    res = []

    def inorder(subtree) -> None:
        for i in subtree:
            if type(i) is tuple:
                inorder(i)
            elif i is not None:
                res.append(i)

    def preorder(subtree) -> None:
        res.append(subtree[1])

        if subtree[0] is not None:
            preorder(subtree[0])

        if subtree[2] is not None:
            preorder(subtree[2])

    def postorder(subtree) -> None:
        if subtree[0] is not None:
            postorder(subtree[0])

        if subtree[2] is not None:
            postorder(subtree[2])

        res.append(subtree[1])

    locals()[order](tree)

    return res


def bonus_tree_walker_yield(tree, order):
    def inorder(subtree) -> None:
        for i in subtree:
            if type(i) is tuple:
                yield from inorder(i)
            elif i is not None:
                yield i

    def preorder(subtree) -> None:
        yield subtree[1]

        if subtree[0] is not None:
            yield from preorder(subtree[0])

        if subtree[2] is not None:
            yield from preorder(subtree[2])

    def postorder(subtree) -> None:
        if subtree[0] is not None:
            yield from postorder(subtree[0])

        if subtree[2] is not None:
            yield from postorder(subtree[2])

        yield subtree[1]

    return locals()[order](tree)
