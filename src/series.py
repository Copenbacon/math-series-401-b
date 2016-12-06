"""A Set of Math Series Functions."""


def fibonacci(n):
    """Fibonacci Sequence."""
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    return n


def lucas(n):
    """Lucas sequence."""
    if n < 0:
        return None
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
    return n


def sum_series(n, k=0, l=1):
    """Sum Series Sequence with optional parameters k and l."""
    if n < 0:
        return None
    elif n == 0:
        return k
    elif n == 1:
        return l
    else:
        return sum_series(n - 1, k, l) + sum_series(n - 2, k, l)
