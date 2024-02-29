
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

# testing various operations
# pylint: disable-next=invalid-name
def test_operation(a, b, operation, expected):
    calculation = Calculation(a, b, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"

# retaining the divide by zero test as is , its a  specific scenario to be tested
def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
