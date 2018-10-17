from functools import wraps


def filter_file(path, keyword):
    with open(path, "r") as f:
        return [l.strip() for l in f if keyword in l]


def sort_file(src, dst):
    try:
        with open(src, "r") as f:
            lines = sorted([l.strip() for l in f])
        with open(dst, "w") as d:
            d.writelines("\n".join(lines))
    except FileNotFoundError:
        return 'file not found'
    except Exception:
        return 'error'

    return 'ok'


def incrementor(n=1):
    return lambda x: x + n


def fibonacci_closure():
    data = []
    # or you could use two variables and refer to them using `nonlocal`

    def fn():
        if not data:
            data.extend((0, 1))
            return 1

        next = sum(data)
        data[0] = data[1]
        data[1] = next
        return next
    return fn


def fibonacci_generator():
    yield 1

    # same solution as in closure, but we are in the same scope, so we can
    # rewrite variables
    last = [0, 1]
    while True:
        next = sum(last)
        last = [last[1], next]
        yield next


def cached(f):
    params = []
    cached = [None]

    # functools.wraps keeps the wrapped function's name and documentation
    @wraps(f)
    def fn(*args):
        nonlocal params

        # you should check whether this is the first call
        # pre-setting cache to None or 0 may not work if the inner function
        # really receives None or 0 as a parameter
        if params and params == args:
            return cached[0]
        params = args
        cached[0] = f(*args)
        return cached[0]

    return fn


def bonus_tree_walker(tree, order):
    if not tree:
        return

    l, v, r = tree

    if order == 'inorder':
        yield from bonus_tree_walker(l, order)
        yield v
        yield from bonus_tree_walker(r, order)
    elif order == 'preorder':
        yield v
        yield from bonus_tree_walker(l, order)
        yield from bonus_tree_walker(r, order)
    else:
        yield from bonus_tree_walker(l, order)
        yield from bonus_tree_walker(r, order)
        yield v
