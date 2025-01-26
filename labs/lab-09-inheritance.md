# Lab 9: Inheritance

This lab will focus on inheritance in Python. We will create a root class for our inheritance hierarchy called `Reading` and make `TemperatureReading` extend that. We will also define a `RainfallReading` class that will also extend `Reading`.

The lab is made up of 4 steps:
1. Define the `Reading` class
2. Change `TemperatureReading` to extend the `Reading` class
3. Define a `RainfallReading` class
4. Add Rainfall Readings code

Steps 3 and 4 are extension points in this lab.

## Step 1: Define the `Reading` Class

The `Reading` class will become the root of our class hierarchy.

The class will have `value`, `date`, and `location` attributes.

It should have an `__init__` method to initialize those attributes.

It should also have operators for `>`, `>=`, `==`, `!=`, `<`, `<=`.

The `Reading` class should also have a `__repr__` method.

## Step 2: Change `TemperatureReading` to Extend the `Reading` Class

Modify the `TemperatureReading` class so that it extends the `Reading` class.

Modify the `__init__` method so that it uses the parent class's `__init__` method to initialize the `temp` (or `value`), `date`, and `location`.

The `TemperatureReading` class will add a `scale` (such as Celsius or Fahrenheit). The scale is therefore an attribute on the `TemperatureReading` class.

The `TemperatureReading` will still have a `convert()` method.

It will also need its own versions of `__add__` and `__sub__` to handle generating a `TemperatureReading` object.

The class should also define a `__repr__` method.

## Step 3: Define a `RainfallReading` Class

The `RainfallReading` class should also extend the `Reading` class.

It extends this class by adding a `time` attribute.

The class will also define its own `__add__` and `__sub__` methods so that they can return `RainfallReading` objects.

The class should also have its own `__repr__` method.

## Step 4: Add Rainfall Readings Code

You should add the following code to your application and verify that it executes correctly:

```python
# Working with Rainfall readings
rainfall_readings = [
    RainfallReading(2.0, '01/05/20', '11:00', 'London'),
    RainfallReading(2.6, '02/05/20', '11:30', 'London'),
    RainfallReading(2.3, '03/05/20', '11:00', 'London'),
    RainfallReading(3.2, '04/05/20', '12:00', 'London'),
    RainfallReading(1.6, '05/05/20', '10:45', 'London')
]
print('All Rainfall Readings:')
print(*rainfall_readings, sep=" ")

rr1 = RainfallReading(2.0, '01/05/20', '11:00', 'London')
rr2 = RainfallReading(2.3, '03/05/20', '11:00', 'London')
print(rr1 < rr2)
print(rr1 == rr2)
print(rr1 > rr2)
```

The output from this is:

```
All Rainfall Readings:
RainfallReading[11:00](2.0 on 01/05/20 at London) RainfallReading[11:30](2.6 on 02/05/20 at London) RainfallReading[11:00](2.3 on 03/05/20 at London) RainfallReading[12:00](3.2 on 04/05/20 at London) RainfallReading[10:45](1.6 on 05/05/20 at London)
True
False
False
```

All other remaining code should work as it did before.