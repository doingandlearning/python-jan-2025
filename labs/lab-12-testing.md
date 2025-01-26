# Lab: Testing

The aim of this lab is to allow you to write a set of tests for your utility functions.

These tests should validate that the functions such as `minimum`, `average`, `range`, etc., operate in the way you expect.

Once you have done this, write a set of tests for your `TemperatureReading` class. Think about what tests you need to ensure its correct functionality.

Don't forget to add `pytest` to the list of libraries in your Python environment's `PYTHONPATH`.

This can be done interactively through your IDE. For example, in PyCharm:

1. Open your **Preferences** (on macOS) or **Settings** (on Windows).
2. Select **Project: <your project name>** and then **Python Interpreter**.

You can then add a package to the current environment for the specified interpreter using the "+" button at the bottom of the dialog.

```
pip install pytest
```

To add `pytest`, type `pytest` into the search bar and click **Install**.

### Note on Floating Point Numbers in Tests

Working with floating point numbers can be notoriously difficult when running tests.

To help with this, Python provides the `isclose()` function from the `math` module.

You must import this into your test file, for example:

```python
from math import isclose
```

You can then use this with an assertion, for example:

```python
def test_average_int():
    result = average(data)
    assert isclose(result, 4.1, rel_tol=0.01)
```

The `rel_tol` parameter indicates the relative tolerance, which is the maximum allowed difference between the two values being compared. `0.01` indicates a tolerance of 1%.

### Example Test File for the `utils` Module

```python
from math import isclose
import pytest
from readings import TemperatureReading, CELSIUS
from utils import average, minimum, maximum, median, celsius_to_fahrenheit, fahrenheit_to_celsius

@pytest.fixture()
def temperatures():
    return [
        TemperatureReading(13.5, '01/05/20', 'London', CELSIUS),
        TemperatureReading(12.6, '02/05/20', 'London', CELSIUS),
        TemperatureReading(15.3, '03/05/20', 'London', CELSIUS),
        TemperatureReading(12.2, '04/05/20', 'London', CELSIUS),
        TemperatureReading(16.6, '05/05/20', 'London', CELSIUS),
        TemperatureReading(14.6, '05/05/20', 'London', CELSIUS),
        TemperatureReading(15.6, '05/05/20', 'London', CELSIUS)
    ]

@pytest.fixture()
def data():
    return [2, 3, 4, 5, 6, 5, 4]

def test_average(temperatures):
    result = average(temperatures)
    assert isclose(result, 14.34, rel_tol=0.01)

def test_median(temperatures):
    result_temp = median(temperatures)
    assert isclose(result_temp.value, 14.6, rel_tol=0.01)

def test_min_int(data):
    assert minimum(data) == 2

def test_max_int(data):
    result = maximum(data)
    assert result == 6

def test_celsius_to_fahrenheit():
    result = celsius_to_fahrenheit(12.3)
    assert isclose(result, 54.14, rel_tol=0.01)

def test_fahrenheit_to_celsius():
    result = fahrenheit_to_celsius(54.14)
    assert isclose(result, 12.3, rel_tol=0.01)
```

---
