"""Testing Series.py."""
import pytest

FIBONACCI_TABLE = [
    [0, 0],
    [1, 1],
    [2, 1],
    [3, 2],
]

LUCAS_TABLE = [
    [0, 2],
    [1, 1],
    [2, 3],
    [3, 4],
    [4, 7],
    [5, 11],
    [6, 18],
    [7, 29],
]

SUM_TABLE = [
    [0, 0, 0, 0],
    [1, 0, 1, 1],
    [2, 0, 1, 1],
    [3, 0, 1, 2],
    [4, 0, 1, 3],
    [0, 2, 1, 2],
    [4, 2, 1, 7],
]


@pytest.mark.parametrize("n, result", FIBONACCI_TABLE)
def test_fibonacci(n, result):
    """Test the fibonacci with input n."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize("n, result", LUCAS_TABLE)
def test_lucas(n, result):
    """Test the fibonacci with input n."""
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize("n, k, l, result", SUM_TABLE)
def test_sum_series(n, k, l, result):
    """Test the fibonacci with input n."""
    from series import sum_series
    assert sum_series(n, k, l) == result
