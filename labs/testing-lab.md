# Lab: Testing Utility Functions with `pytest`

In this lab, you’ll learn how to install `pytest`, write utility functions, and test them using the principles of Test-Driven Development (TDD): Red (Fail) -> Green (Pass) -> Refactor.

We’ll start by installing `pytest` in your IDE, then write and test several functions in `utils.py` to ensure they handle both valid and invalid inputs.

---

## Objectives

1. Install `pytest` in your Python environment (PyCharm or VSCode).
2. Write utility functions using TDD.
3. Test functions for both happy and unhappy paths.
4. Use parameterized tests to cover multiple cases efficiently.

---

### Part 1: Install `pytest`

1. **In PyCharm**:
   - Open your project.
   - Go to **File > Settings > Project: [Your Project Name] > Python Interpreter**.
   - Click the `+` button to add a new package and search for `pytest`.
   - Select `pytest` and install it.

2. **In VSCode**:
   - Open a terminal within VSCode.
   - Run the following command to install `pytest`:
     ```bash
     pip install pytest
     ```

### Part 2: Write Utility Functions in `utils.py`

Your `utils.py` file contains a function called `add()` and placeholders for additional functions. Following the TDD process, you’ll write tests for these functions before implementing them. This lab will guide you through implementing and testing these functions one by one.

**Example utility functions to implement:**

1. `add(a, b)`: Adds two numbers.
2. `subtract(a, b)`: Subtracts `b` from `a`.
3. `multiply(a, b)`: Multiplies two numbers.
4. `divide(a, b)`: Divides `a` by `b`. Raises a `ZeroDivisionError` if `b` is zero.
5. `square_root(a)`: Returns the square root of `a`. Raises a `ValueError` if `a` is negative.

### Part 3: Write Tests in `test_utils.py`

In your `test_utils.py` file, write tests for each utility function in `utils.py`. Use a combination of happy path, parameterized, and error handling tests.

Below is a sample structure to guide you through writing the tests.

### Task 1: Write and Test the `subtract` Function

1. **Implement the `subtract()` function** in `utils.py`.
   ```python
   def subtract(a, b):
       if type(a) not in (int, float):
           raise TypeError("a must be a number")
       if type(b) not in (int, float):
           raise TypeError("b must be a number")
       return a - b
   ```

2. **Write Tests for `subtract()`** in `test_utils.py`.
 - What is the happy path?
 - Parametrize some values
 - What is the unhappy path?

Example `subtract` tests:

```python
from utils import subtract

def test_subtracting_two_numbers():
    assert subtract(5, 3) == 2

@pytest.mark.parametrize("input1, input2, expected", [
    (5, 3, 2),
    (0, 3, -3),
    (-1, -1, 0)
])
def test_subtract_various_numbers(input1, input2, expected):
    assert subtract(input1, input2) == expected

def test_subtract_raises_type_error_on_invalid_input():
    with pytest.raises(TypeError):
        subtract("a", "b")
```

---

### Task 2: Write and Test the `multiply` Function

1. Implement `multiply(a, b)` to handle non-numeric inputs with a `TypeError`.
2. Write tests for valid and invalid inputs in `test_utils.py`.

Example `multiply` tests:

```python
from utils import multiply

def test_multiplying_two_numbers():
    assert multiply(3, 2) == 6

@pytest.mark.parametrize("input1, input2, expected", [
    (5, 2, 10),
    (0, 5, 0),
    (-1, 3, -3)
])
def test_multiply_various_numbers(input1, input2, expected):
    assert multiply(input1, input2) == expected

def test_multiply_raises_type_error_on_invalid_input():
    with pytest.raises(TypeError):
        multiply("a", "b")
```

---

### Task 3: Write and Test the `divide` Function

1. **Implement `divide(a, b)`**, ensuring it raises a `TypeError` for non-numeric inputs and a `ZeroDivisionError` if `b` is zero.
2. **Write Tests for `divide()`** that check for valid inputs, division by zero, and non-numeric inputs.

Example `divide` tests:

```python
from utils import divide

def test_dividing_two_numbers():
    assert divide(6, 2) == 3

@pytest.mark.parametrize("input1, input2, expected", [
    (10, 2, 5),
    (-6, 2, -3),
    (0, 1, 0)
])
def test_divide_various_numbers(input1, input2, expected):
    assert divide(input1, input2) == expected

def test_divide_raises_type_error_on_invalid_input():
    with pytest.raises(TypeError):
        divide("a", "b")

def test_divide_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
```

---

### Task 4: Write and Test the `square_root` Function

1. **Implement `square_root(a)`** to calculate the square root of `a`, raising a `TypeError` for non-numeric inputs and a `ValueError` for negative numbers.
2. **Write Tests for `square_root()`** for positive numbers, non-numeric inputs, and negative numbers.

Example `square_root` tests:

```python
from utils import square_root

def test_square_root_of_positive_number():
    assert square_root(4) == 2

@pytest.mark.parametrize("input, expected", [
    (9, 3),
    (0, 0),
    (1.44, 1.2)
])
def test_square_root_various_numbers(input, expected):
    assert square_root(input) == expected

def test_square_root_raises_value_error_on_negative():
    with pytest.raises(ValueError):
        square_root(-4)
```

---

### Running Tests

To run all tests, use the command:

```bash
pytest
```

Each test will be executed, and `pytest` will provide a summary indicating which tests passed or failed.

