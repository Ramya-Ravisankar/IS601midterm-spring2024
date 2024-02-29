import pytest
from main import calculate_and_print  # Ensure this import matches your project structure

# Parameterize the test function to cover different operations and scenarios, including errors
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("4", "2", 'add', "The result of 4 add 2 is equal to 6"),
    ("10", "6", 'subtract', "The result of 10 subtract 6 is equal to 4"),
    ("5", "6", 'multiply', "The result of 5 multiply 6 is equal to 30"),
    ("30", "5", 'divide', "The result of 30 divide 5 is equal to 6"),
    ("5", "0", 'divide', "An error occurred: Cannot divide by zero"),  # Adjusted for the actual error message
    ("6", "3", 'unknown', "Unknown operation: unknown"),  # Test for unknown operation
    ("a", "6", 'add', "Invalid number input: a or 6 is not a valid number."),  # Testing invalid number input
    ("9", "b", 'subtract', "Invalid number input: 9 or b is not a valid number.")  # Testing another invalid number input
])
def test_calculate_and_print(a_string, b_string, operation_string,expected_string, capsys):
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string
