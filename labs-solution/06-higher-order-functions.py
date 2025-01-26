# Initialize list for temperature readings
readings = [13.5, 11.1, 17.5, 12.6, 15.3, 12.2, 16.6, 14.6]
continue_to_enter_data = True

# Collect temperature readings from user input
while continue_to_enter_data:
    input_string = input('Please enter a temperature reading (-1 to end): ')
    if input_string == '-1':
        continue_to_enter_data = False
    elif input_string.count('.') > 1 or not input_string.replace('.', '').isdigit():
        print('Must be a positive floating point number')
    else:
        reading = float(input_string)
        readings.append(reading)

# Define utility functions

def average(data):
    """Returns the average of the values in the data iterable"""
    return sum(data) / len(data)

def median(data):
    """Calculates the median value in a list or tuple"""
    sorted_data = sorted(data)
    data_length = len(sorted_data)
    index = (data_length - 1) // 2
    if data_length % 2 == 1:  # Checks for an odd number
        return sorted_data[index]
    else:
        return (sorted_data[index] + sorted_data[index + 1]) / 2.0

def minimum(data, index=0):
    """Returns the minimum value in a list or tuple starting at index"""
    return min(data[index:])

def maximum(data, index=0):
    """Returns the maximum value in a list or tuple starting at index"""
    return max(data[index:])

def data_range(data):
    """Returns the minimum and maximum values in data"""
    return minimum(data), maximum(data)

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit"""
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5 / 9

# Step 1: Convert All Temperatures to Fahrenheit
fahrenheit_temperatures = list(map(celsius_to_fahrenheit, readings))
print(f'Fahrenheit Temperatures: {fahrenheit_temperatures}')

# Step 2: Select All Temperatures Above 14.0
higher_temperatures = list(filter(lambda x: x > 14.0, readings))
print(f'Temperatures above 14.0: {higher_temperatures}')

# Step 3: Convert All the Temperatures Above 14.0 to Fahrenheit
converted_temperatures = list(map(celsius_to_fahrenheit, higher_temperatures))
print(f'Fahrenheit Temperatures above 14.0°C: {converted_temperatures}')