from maths import add
from quantity import Quantity

import pytest
def test_add_zeros():
    # Arrange
    # Act
    result = add(0,0)
    # Assert
    assert result == 0

def test_add_one_and_zero():
    result = add(1,0)
    assert result == 1


# Parameterising our tests
@pytest.mark.parametrize(
    "a,b,want", [
        (1,1,2),
        (-1, -1, -2),
        (0, -1, -1),
        (0.1, 0.1, 0.2),
        (-1000000, 1000000, 0)
    ]
)
def test_adding_works_as_expect(a, b, want):
    got = add(a, b)
    assert want == got


def setup_module():
    print("This will run before any test but once per file")

def teardown_module():
    print("This will after all the tests in a file have ran")

def setup_function():
    print("Before every test")

def teardown_function():
    print("After each test")

def test_quantities_with_equal_values_are_equal():
    # Arrange (Given)
    q1 = Quantity(10)
    q2 = Quantity(10)

    # Act (when)/Assert (then)
    assert q1 == q2

def test_add_errors_when_we_add_non_numbers():
    with pytest.raises(TypeError):
        result = add(True, [])