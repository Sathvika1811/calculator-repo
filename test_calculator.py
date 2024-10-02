import pytest
from calculator import Calculator
from calculation import Calculation

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_calculation_class():
    calculation = Calculation("2 + 3", 5)
    assert calculation.operation == "2 + 3"
    assert calculation.result == 5
