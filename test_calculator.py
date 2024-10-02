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
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)


def test_calculation_class():
    # Adjust the operation to match what your Calculation class expects
    addition = Calculation("add", 2, 3)
    assert addition.execute() == 5  # This checks if 2 + 3 equals 5

    subtraction = Calculation("subtract", 5, 3)
    assert subtraction.execute() == 2  # This checks if 5 - 3 equals 2

    multiplication = Calculation("multiply", 4, 2)
    assert multiplication.execute() == 8  # This checks if 4 * 2 equals 8

    division = Calculation("divide", 6, 2)
    assert division.execute() == 3  # This checks if 6 / 2 equals 3

    # You can also test division by zero
    with pytest.raises(ZeroDivisionError):
        Calculation("divide", 5, 0).execute()
