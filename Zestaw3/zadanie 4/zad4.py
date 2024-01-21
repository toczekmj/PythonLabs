import functools


def pamiec(func):
    dct = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args in dct:
            return dct[args]
        else:
            res = func(*args, **kwargs)
            dct[args] = res
            return res

    return wrapper


@pamiec
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


for i in range(100):
    print(fib(i))
