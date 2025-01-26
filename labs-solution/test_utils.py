import pytest
from utils import *

def test_average():
    assert average([1, 2, 3, 4, 5]) == 3
    assert average([10, 20, 30, 40, 50]) == 30
    assert average([1.5, 2.5, 3.5]) == 2.5
    with pytest.raises(ZeroDivisionError):
        average([])  # Should raise an error when trying to average an empty list

def test_median():
    assert median([1, 3, 3, 6, 7, 8, 9]) == 6
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4]) == 2.5
    assert median([3, 1, 4, 2]) == 2.5
    assert median([7]) == 7

def test_minimum():
    assert minimum([3, 1, 4, 1, 5, 9, 2]) == 1
    assert minimum([3, 1, 4, 1, 5, 9, 2], 2) == 1
    assert minimum([3, 1, 4, 1, 5, 9, 2], 5) == 2

def test_maximum():
    assert maximum([3, 1, 4, 1, 5, 9, 2]) == 9
    assert maximum([3, 1, 4, 1, 5, 9, 2], 2) == 9
    assert maximum([3, 1, 4, 1, 5, 9, 2], 5) == 9

def test_data_range():
    assert data_range([3, 1, 4, 1, 5, 9, 2]) == (1, 9)
    assert data_range([7, 7, 7, 7]) == (7, 7)
    assert data_range([5, 3, 8, -1, 10]) == (-1, 10)

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(37) == pytest.approx(98.6, 0.1)

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40
    assert fahrenheit_to_celsius(98.6) == pytest.approx(37, 0.1)
