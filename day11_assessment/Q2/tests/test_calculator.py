import pytest
from ..calculator import add,sub,mul,div

def test_add():
    assert add(2,3) == 5

def test_sub():
    assert sub(5,3) == 2, "Subtraction result is incorrect"

def test_mul():
    assert mul(3,4) == 12

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(3,0)