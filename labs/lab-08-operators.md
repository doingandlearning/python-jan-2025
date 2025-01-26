# Lab 8: Operators

The aim of this lab is to explore defining a set of methods that will map to a set of operators for the `TemperatureReading` class.

In this lab, we will update the `TemperatureReading` class such that it now supports operations such as `+`, `-`, `==`, `!=`, `>`, `>=`, `<`, and `<=`.

This means that you will need to implement the appropriate associated methods for these operators.

This lab is made up of 5 steps:
1. Add an equals method (`__eq__`)
2. Define the `__add__` and `__sub__` methods
3. Define further operators
4. Revise sort functions
5. Using the operators

Steps 3 onwards should be considered extension points for those with more programming experience.

## Step 1: Add an Equals Method (`__eq__`)

For example, your equals method might look like:

```python
def __eq__(self, other):
    return self.temp == other.temp
```

## Step 2: Define the `__add__` and `__sub__` Methods

Note that `add` and `subtract` should support adding two temperatures together as well as adding an `int` or a `float` to a temperature. In the same way, `subtract` should also allow one temperature to be subtracted from another as well as an `int` or a `float` to be subtracted. You should check to see whether the value supplied is an `int`, a `float`, or a `TemperatureReading` and take the appropriate steps.

An example of the `__add__` method is given below:

```python
def __add__(self, other):
    if isinstance(other, int) or isinstance(other, float):
        new_value = self.temp + other
    else:
        new_value = self.temp + other.temp
    return TemperatureReading(new_value, self.date, self.location, self.scale)
```

The `__sub__` method should follow a similar pattern.

You should now be able to run:

```python
# Add temperatures together
new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + TemperatureReading(15.5, '01/05/20', 'London', 'Celsius')
print('Add two temperatures', new_temperature)

# Add an int to a temperature
new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + 5
print('Add a temperature and an int', new_temperature)

# Add a float to a temperature
new_temperature = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + 5.5
print('Add a temperature and a float', new_temperature)
```

## Step 3: Define Further Operators

You should now define other logical operators such as `!=`, `>`, `>=`, `<`, and `<=`.

```python
another_temperature = TemperatureReading(14.6, '05/05/20', 'London')

print(new_temperature > another_temperature)
print(new_temperature >= another_temperature)
print(new_temperature == another_temperature)
print(new_temperature != another_temperature)
print(new_temperature < another_temperature)
print(new_temperature <= another_temperature)
```

## Step 4: Revise the Sort Functions

You should now find that you can simplify the sorting of temperatures as they now support the required operators. That is, you should now be able to write:

```python
sorted_data = sorted(data)
```

## Step 5: Using the Operators

Test your new operator methods by running different comparisons and arithmetic operations on `TemperatureReading` objects. This will ensure that your class behaves as expected when used in expressions involving these operators.

---