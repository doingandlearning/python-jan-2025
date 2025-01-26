# Plan for Session
- What is pytest?
- Writing tests
- Test Fixtures
- Parameterized Tests
- Ignoring Tests
- Testing for exceptions

---

## What is pytest?
- Testing library for Python; one of the most popular.
- Builds on top of/extends `unittest`.
- Provides an extended set of facilities.
- Can be used for different levels of testing: unit, integration, system.
  - Most typically used for unit testing.
  - Used by companies like Dropbox, Mozilla, etc., as their Python testing framework.
- Has support in IDEs such as PyCharm, allowing for red bar/green bar development.

---

## Simple pytest Example
- Need something to test:
  - May be a function.
  - Can be a class.
  
### Example: Calculator class in `calculator.py` file
- Has the concept of the current total, current value entered, and the action to apply to the current value.

```python
class Calculator:
    def __init__(self):
        self.current = 0
        self.total = 0

    def set(self, value):
        self.current = value

    def add(self):
        self.total += self.current

    def sub(self):
        self.total -= self.current

    def total(self):
        return self.total

def add(x, y):
    return x + y
```

---

## Writing a Test
- Place tests in a separate file/module.
  - Test defined in a file `test_calculator.py`, therefore a separate module.
  - Will need to import from the `calculator` module.
- pytest uses conventions to find tests:
  - Searches for `test_*.py` or `*_test.py` files.
  - From those files, collects test items: `test_` prefixed test functions.
  - IDE typically provides support for creating suitable test files.

### Example:
```python
from calculator import add

def test_add_zeros():
    result = add(0, 0)
    assert result == 0

def test_add_one_and_zero():
    result = add(1, 0)
    assert result == 1

def test_add_zero_and_one():
    result = add(0, 1)
    assert result == 1, "should be one"
```

- Can also test classes in exactly the same way.

### Example:
```python
from calculator import Calculator

def test_add_one():
    calc = Calculator()
    calc.set(1)
    calc.add()
    assert calc.total == 1
```

- Run using pytest from the command line or via an IDE.

---

## Running a Test
- In an IDE, you can see the result of tests and explore test reports.

---

## Test Fixtures
- May need to run some behavior before or after each test or before or after a group of tests in a module.
  - To provide resources for a test.
- Such code is known as a fixture.
  - May set up a scenario for a test.
  - Supply an object to be tested.
  - Perform post-test housekeeping, etc.
- Two styles:
  - Naming conventions.
  - pytest Python decorators.

### Example: Test Fixtures as Functions
- Based on naming conventions.

```python
from calculator import add

def setup_module():
    print('module set up')

def teardown_module():
    print('module teardown')

def setup_function():
    print('function set up')

def teardown_function():
    print('function teardown')

def test_add_one_and_one():
    result = add(1, 1)
    assert result == 2
```
- Output:
  - `module set up`
  - `function set up`
  - `PASSED [100%]`
  - `function teardown`
  - `module teardown`

### Example: Test Fixtures Using Decorators
- Can use `pytest` fixture decorator, have format `@<name>` to indicate fixtures for tests.

```python
import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    """Returns a Calculator instance"""
    print('calculator fixture')
    return Calculator()

def test_initial_value(calculator):
    assert calculator.total == 0

def test_add_one(calculator):
    calculator.set(1)
    calculator.add()
    assert calculator.total == 1

def test_subtract_one(calculator):
    calculator.set(1)
    calculator.sub()
    assert calculator.total == -1

def test_add_one_and_one(calculator):
    calculator.set(1)
    calculator.add()
    calculator.set(1)
    calculator.add()
    assert calculator.total == 2
```
- `autouse` means automatically run—doesn't need to be explicitly referenced.

---

## Ignoring Tests
- May want to ignore tests, particularly during development.
- To ignore a test, decorate it with `@pytest.mark.skip`.

### Example:
```python
@pytest.mark.skip(reason='not implemented yet')
def test_calculator_multiply(calculator):
    calculator.multiply(2, 3)
    assert calculator.total == 6
```
- Reported in IDE/pytest report.

---

## Parameterized Tests
- Common to run the same tests multiple times with several different input values.
- Can greatly reduce the number of tests needed.
- Such tests are referred to as parameterized tests, specified via `@pytest.mark.parametrize` decorator with values to apply provided to the decorator.

### Example:
```python
@pytest.mark.parametrize('input1, input2, expected', [
    (3, 1, 4),
    (3, 2, 5),
])
def test_calculator_add_operation(calculator, input1, input2, expected):
    calculator.set(input1)
    calculator.add()
    calculator.set(input2)
    calculator.add()
    assert calculator.total == expected
```
- This illustrates setting up a parameterized test for the Calculator in which two input values are added together and compared with the expected value.

---

## Testing for Exceptions
- Can write tests that verify that an exception was raised.
- In pytest, use the `with` statement and `pytest.raises`.

### Example:
```python
import pytest

def test_current_account_overdraft():
    current_account = CurrentAccount(0.0)
    with pytest.raises(accounts.BalanceError):
        current_account.withdraw(200.0)
```

---

## Questions?

?
