"""Числа Фибоначчи: итеративная и рекурсивная реализации"""


def _validate(n):
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError(f"n must be int, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"n must be >= 0, got {n}")


def fib_iterative(n):
    _validate(n)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_recursive(n):
    _validate(n)

    def _go(k):
        if k < 2:
            return k
        return _go(k - 1) + _go(k - 2)

    return _go(n)