import pytest
from programs import list_of_squares

def test_list_of_squares5():
    assert list_of_squares.list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
def test_list_of_squares3(): 
    assert list_of_squares.list_of_squares(3) == {1: 1, 2: 4, 3: 9}
def test_list_of_squares7():
    assert list_of_squares.list_of_squares(7) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36 , 7: 49}
def test_list_of_squares1():
    assert list_of_squares.list_of_squares(1) == {1: 1}