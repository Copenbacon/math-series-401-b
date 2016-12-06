"""Testing Series.py."""
import pytest

PARAMS_TABLE = [
    [0, 0],
    [1, 1],
    [2, 1],
    [3, 2],
]

PARAMS_TABLE2 = [
    [0, 2],
    [1, 1],
    [2, 3],
    [3, 4],
    [4, 7],
    [5, 11],
    [6, 18],
    [7, 29],
]


@pytest.mark.parametrize("n, result", PARAMS_TABLE)
def test_fibonacci(n, result):
    """Test the fibonacci with input n."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize("n, result", PARAMS_TABLE2)
def test_lucas(n, result):
    """Test the fibonacci with input n."""
    from series import lucas
    assert lucas(n) == result
