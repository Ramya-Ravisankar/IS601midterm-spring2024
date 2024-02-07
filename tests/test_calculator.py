'''My Calculator Test'''
from calculator import add, subtract , multiply

def test_addition():
    '''Test that the addition function works '''    
    assert add(3,3) == 6

def test_subtraction():
    '''Test that the subtraction function works '''    
    assert subtract(4,4) == 0

def test_multiply():
    '''Test that the multiply function works '''    
    assert multiply(3,4) == 12
