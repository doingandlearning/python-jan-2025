# Lab 5: Functions

The aim of this lab is to develop a number of functions that can be used within the temperature readings data application you created in the last lab.

Each of the functions to be created will take the readings in as a data parameter and perform some operation on the data. For example, the average or minimum or maximum values might be obtained.

This lab is made up of 6 steps:
1. Implement a function to average the temperatures
2. Implement a function to calculate the median
3. Minimum and maximum functions
4. Return a data range
5. Convert Celsius to Fahrenheit
6. Convert Fahrenheit into Celsius

Steps 3 onwards should be treated as extension points if you are new to programming.

## Step 0: Change the Code to Use Hard-Coded List

To speed up running your application, you might want to change the readings to be initialized as follows:

```python
readings = [13.5, 11.1, 17.5, 12.6, 15.3, 12.2, 16.6, 14.6]
```

This means you can use `-1` to just get the code to run the application without needing you to enter the data interactively.

## Step 1: Implement a Function to Average the Temperatures

The first function to create will average the temperatures in the list. There are several ways in which you could do this, but the simplest is to use the built-in functions `sum()` and `len()` to total up the values in a list and divide that value by the length of the list. For example:

```python
def average(data):
    return sum(data) / len(data)
```

You can test your function using the code you have already written to obtain a list of readings from the user. For example:

```python
# Find the average and median values - note old and new styles
print('Average temperature = {:.2f}'.format(average(readings)))
print(f'Average temperature = {average(readings):.2f}')
```

Note that in this example, we have used the `format()` function available on strings. This can be used to indicate that the average should be formatted to two decimal places (see [W3Schools Python String format() Method](https://www.w3schools.com/python/ref_string_format.asp)).

## Step 2: Implement a Function to Calculate the Median

For the next function, we will implement a function that will return the median value (if there is one) or an approximation if there is an even number of values.

Call the function `median`. This function will require the data to be sorted, so we will use the `sorted()` function for a list rather than the `sort()` operation on a list. This is because `sorted` does not modify the original list.

We can then find the median value if present; if not, we can take the average between the two values in the middle of the range.

For example:

```python
def median(data):
    """Calculates the median value in a list or tuple"""
    sorted_data = sorted(data)
    data_length = len(data)
    index = (data_length - 1) // 2
    if data_length % 2 == 1:  # Checks for an odd number
        return sorted_data[index]
    else:
        return (sorted_data[index] + sorted_data[index + 1]) / 2.0
```

You can now test this function using your readings:

```python
print(f'Median temperature value = {median(readings)}')
```

## Step 3: Minimum and Maximum Functions

The aim of these functions is to write a function that will return the minimum or maximum value in the list starting at a particular point in the list. They thus take two parameters: the data to search through and the starting index to use. For example, you should be able to write:

```python
print(f'Min temp in list = {minimum(readings)}')
print(f'Min temp in list start position 4 = {minimum(readings, 3)}')
print(f'Max temp in list = {maximum(readings)}')
print(f'Max temp in list starting position 4 = {maximum(readings, 3)}')
```

Note that the second parameter, the index, has a default value that is used if no value is supplied when the function is called. This default value should be `0`.

Note that lists support the concept of slices.

To obtain a sub-list starting at a particular location, you can use the slice syntax. The slice syntax uses the `[]` index operator but uses a `:` to indicate the scope of the slice as shown below:

```python
list[start:stop]  # Items start through stop-1
list[start:]      # Items start through the rest of the list
list[:stop]       # Items from the beginning through stop-1
list[:]           # A copy of the whole list
```

## Step 4: Return a Data Range Tuple

The `data_range` function returns the minimum and maximum values in the temperature list. For example:

```python
min_temp, max_temp = data_range(readings)
print(f'Range of temperatures from {min_temp} to {max_temp}')
```

This should produce output like:

```
Range of temperatures from 11.1 to 17.5
```

## Step 5: Convert Celsius to Fahrenheit

The final function to implement is a `celsius_to_fahrenheit` converter function. This function is given a number representing a temperature in Celsius and returns that temperature in Fahrenheit.

The calculation for this is:

```python
(celsius * 9 / 5) + 32
```

The `celsius_to_fahrenheit()` might be called in the following way:

```python
print(f'13.5 celsius as fahrenheit - {celsius_to_fahrenheit(13.5)}')
```

The output from this would be:

```
13.5 celsius as fahrenheit - 56.3
```

## Step 6: Convert Fahrenheit into Celsius

You should also define a function to convert Fahrenheit into Celsius. For example:

```python
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
```

Then you can test it:

```python
print(f'56.3 fahrenheit as celsius - {fahrenheit_to_celsius(56.3):.1f}')
```

## Sample Solution

```python
def average(data):
    """Returns the average of the values in the data iterable"""
    return sum(data) / len(data)

def median(data):
    """Calculates the median value in a list or tuple"""
    sorted_data = sorted(data)
    data_length = len(data)
    index = (data_length - 1) // 2
    if data_length % 2 == 1:  # Checks for an odd number
        return sorted_data[index]
    else:
        return (sorted_data[index] + sorted_data[index + 1]) / 2.0

def minimum(data, index=0):
    """Returns the minimum value in a list or tuple starting at index"""
    if index == 0:
        data_slice = data
    else:
        data_slice = data[index:]
    return min(data_slice)

def maximum(data, index=0):
    """Returns the maximum value in a list or tuple starting at index"""
    if index == 0:
        data_slice = data
    else:
        data_slice = data[index:]
    return max(data_slice)

def data_range(data):
    """Returns the minimum and maximum values in data"""
    return minimum(data), maximum(data)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
```
