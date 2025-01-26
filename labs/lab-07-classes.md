# Lab 7: Classes

The aim of this lab is to allow you to explore the creation of Python classes. You will create a class to represent the temperature readings we have been working on. This class will not just represent the reading but also provide other information about the reading, such as the date of the reading, the location, and the scale used for the reading, such as Celsius or Fahrenheit.

The lab is made up of 4 steps:
1. Create the class
2. Add string representation (`__repr__`) behavior to the class
3. Add a class docstring
4. Use the class

Step 5 onwards should be considered an extension point in this lab.

## Step 1: Create the Class

Create a `TemperatureReading` class that we can use with our application.

The `TemperatureReading` class should have the following attributes:

- `temperature`
- `date` (of the reading)
- `location` (of the reading)
- `scale` (either Celsius or Fahrenheit) with Celsius as the default

It should also have an `__init__()` method that will be used to initialize the attributes of the object.

The class might be defined so far as:

```python
CELSIUS = "Celsius"
FAHRENHEIT = "Fahrenheit"

class TemperatureReading:
    def __init__(self, temp, date, location, scale=CELSIUS):
        self.temp = temp
        self.date = date
        self.location = location
        self.scale = scale
```

## Step 2: Add String Representation Behavior to the Class

The `TemperatureReading` class should also have a `__repr__(self)` method and optionally a `__str__(self)` method that can be used to convert the `TemperatureReading` into a string for printing purposes. For example:

```python
def __repr__(self):
    return f'TemperatureReading({self.temp}, {self.date}, {self.location}, {self.scale})'

def __str__(self):
    return f'TemperatureReading[{self.scale}]({self.temp} on {self.date} at {self.location})'
```

## Step 3: Add a Class Docstring

You could also give the class a docstring that describes its purpose.

## Step 4: Use the Class

You should now create a list of readings as shown below:

```python
readings = [
    TemperatureReading(13.5, '01/05/20', 'London', 'Celsius'),
    TemperatureReading(12.6, '02/05/20', 'London', 'Celsius'),
    TemperatureReading(15.3, '03/05/20', 'London', 'Celsius'),
    TemperatureReading(12.2, '04/05/20', 'London', 'Celsius'),
    TemperatureReading(16.6, '05/05/20', 'London', 'Celsius'),
    TemperatureReading(14.6, '05/05/20', 'London', 'Celsius'),
    TemperatureReading(15.6, '05/05/20', 'London', 'Celsius')
]
```

You should verify that all functionality still works. It probably won't—so you can comment out the code that doesn't work for now (or see extension point).

## Extension Points

### Step 5: Conversion Method

In terms of behavior, the class should have a `convert` method that will convert an instance of a temperature from Celsius to Fahrenheit or vice versa.

The `convert` function should not modify the original object; instead, it should create a new object representing the new version of the temperature reading with the correct scale specified.

### Step 6: Make Existing Functions Work

Note that some functions may need to change, such as the `median()`, `min()`, and `max()` functions. This is because the values in the list are now `TemperatureReading` objects rather than plain float numbers.

Another utility function may be one to extract a temperature from a temperature reading object, for example:

```python
def extract_readings(reading):
    return reading.temp
```

### Hints

The `convert` function should work as shown below:

```python
temp1 = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius')
temp2 = temp1.convert()
print(f'temp1: {temp1}')
print(f'temp2: {temp2}')
```

The output from this code snippet is shown below:

```
temp1: TemperatureReading[Celsius](13.5 on 01/05/20 at London)
temp2: TemperatureReading[Fahrenheit](56.3 on 01/05/20 at London)
```

To print out a list of temperatures using `__repr__`, you can just print:

```python
print(readings)
```

But note to print out a list of temperature readings using the `__str__()` method, you can use:

```python
print(*readings)
```
