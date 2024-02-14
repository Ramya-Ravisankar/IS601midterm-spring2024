'''My Calculator Test'''
from calculator.operations import add, multiply, subtract, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(3,3) == 6

def test_subtraction():
    '''Test that subtraction function works '''    
    assert subtract(4,2) == 2

def test_multiplication():
    '''Test that multiplication function works'''
    assert multiply(2,3) == 6

def test_division():
    '''Test that division function works'''
    assert divide(2,2) == 1
    