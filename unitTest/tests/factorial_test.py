import pytest
from programs import factorial

def test_factorial0():
    assert factorial.fact(0) == 1
def test_factorial8():
    assert factorial.fact(8) == 40320
def test_factorial5():
    assert factorial.fact(5) == 120
def test_factorial10():
    assert factorial.fact(10) == 3628800