import pytest
from app.operation import add, subtract, multiply, divide

@pytest.mark.parametrize("values, expected", [
    ([1,2,3], 6),
    ([], 0),
    ([5], 5),
])
def test_add(values, expected):
    assert add(values) == expected

@pytest.mark.parametrize("values, expected", [
    ([5,2,1], 2),
    ([5], 5),
    ([], 0),
])
def test_subtract(values, expected):
    assert subtract(values) == expected

@pytest.mark.parametrize("values, expected", [
    ([2,3,4], 24),
    ([5], 5),
    ([], 0),
])
def test_multiply(values, expected):
    assert multiply(values) == expected

@pytest.mark.parametrize("values, expected", [
    ([8,2], 4),
    ([9,3,3], 1),
    ([5], 5),
])
def test_divide(values, expected):
    assert divide(values) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide([1,0])
def test_divide_empty_returns_zero():
    from app.operation import divide
    assert divide([]) == 0
