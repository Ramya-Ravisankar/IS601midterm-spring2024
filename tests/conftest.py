# conftest.py
from decimal import Decimal
from faker import Faker
import pytest
from calculator.operations import Operations as op
fake = Faker()
def generate_test_data(num_records):
    operation_mappings = {
        'add': op.addition,
        'subtract': op.subtraction,
        'multiply': op.multiplication,
        'divide': op.division
    }
    # Generate test data
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        # ensuring b is not zero for divide operation
        if operation_func == op.division: # pylint: disable=W0143
            b = Decimal('1') if b == Decimal('0') else b
        try:
            if operation_func == op.division and b == Decimal('0'): # pylint: disable=W0143
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        yield a, b, operation_name, operation_func, expected
def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")
def pytest_generate_tests(metafunc):
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
         # 'operation' (function reference) is used for Calculation class tests
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
         # Modify parameters to fit test functions' expectations
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
