import pytest
from day9_assessment.Q1.utilities.calculator import Calculator

def test_addition():
    calc = Calculator()
    assert calc.add(5, 5) == 10

def test_division():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)
