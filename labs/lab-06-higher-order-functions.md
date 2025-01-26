# Lab 6: Higher Order Functions

The aim of this lab is to use higher-order functions to apply operations to the collections of temperature data in the application we have been developing.

We will use two higher-order functions: `map` and `filter`.

This lab is made up of 5 steps:

1. Convert all temperatures to Fahrenheit
2. Select all temperatures above 14.0
3. Convert all the temperatures above 14.0 to Fahrenheit
4. Run all the examples

Steps 3 onwards should be considered extension points for those with more programming experience.

## Step 1: Convert All Temperatures to Fahrenheit

Currently, all the temperatures in the `readings` list are in Celsius. However, we now want to convert all of the readings from Celsius to Fahrenheit.

Use the `map()` higher-order function to apply the `celsius_to_fahrenheit` function to each value in `readings` and generate a new list containing the Fahrenheit values.

You should then print these Fahrenheit readings out:

```python
print(f'Fahrenheit Temperatures: {fahrenheit_temperatures}')
```

Note: For this example, you do not need to create a lambda function.

You can use the conversion functions created in the last lab. If you did not implement these, then the following definitions can be used:

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
```

## Step 2: Select All Temperatures Above 14.0

For the next function, you should use the `filter()` function to select all those readings that are greater than 14.0.

The result of the `filter()` function could be wrapped up in a list. This list should then be printed, for example:

```python
print(f'Temperatures above 14.0: {higher_temperatures}')
```

## Step 3: Convert All the Temperatures Above 14.0 to Fahrenheit

Combine the `filter` and `map` functions to convert only those temperatures above 14.0 to Fahrenheit.

Then print them out:

```python
print(f'Fahrenheit Temperatures above 14.0°C: {converted_temperatures}')
```

## Step 4: Run All the Examples

As an example, the following is sample output from the above steps:

```
Readings: [13.5, 12.6, 15.3, 12.2, 16.6, 14.6, 15.6]
Fahrenheit Temperatures: [56.3, 54.68, 59.540000000000006, 53.96, 61.88, 58.28, 60.08]
Temperatures above 14.0: [15.3, 16.6, 14.6, 15.6]
Fahrenheit Temperatures above 14.0°C: [59.540000000000006, 61.88, 58.28, 60.08]
```
