import pytest
from ..math_utils import multiply, divide

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (5, 5, 25),
    (-1, 10, -10)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    assert multiply(0, 0) == 0

@pytest.mark.xfail(reason="Known bug in divide by negative zero")
def test_divide_by_negative_zero():
    assert divide(10, -0) == 0

def test_env_variable(env):
    print(f"Running tests in {env} environment")
    assert env in ["dev", "staging", "prod"]

