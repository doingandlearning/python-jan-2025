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

# Display the collected readings and the number of readings
print(f'Temperature readings input: {readings}')
print(f'There are {len(readings)} readings in total')

# Sort and display the readings
readings.sort()
print(f'Temperature readings sorted: {readings}')

# Reverse and display the readings
readings.reverse()
print(f'Temperature readings in reverse: {readings}')

# Count and display the number of zero readings
print(f'There are {readings.count(0.0)} zero readings')

# Create and manipulate a copy of the readings list
readings_copy = readings.copy()
print(f'Copy of temperature readings: {readings_copy}')

# Append a value to the copy and show the difference between the original and the copy
readings_copy.append(5.5)
print(f'Temperature readings: {readings}')
print(f'Copy of temperature readings: {readings_copy}')

# Pop the last element from the copy and display the result
print(f'Popping element from end of copy list {readings_copy.pop()}')
print(f'Readings copy now contains {readings_copy}')

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

# Display summary statistics
print(f'Average temperature: {average(readings)}')
print(f'Median temperature: {median(readings)}')
print(f'Minimum temperature: {minimum(readings)}')
print(f'Maximum temperature: {maximum(readings)}')
print(f'Temperature range: {data_range(readings)}')

# Example conversions
if readings:
    print(f'First reading in Fahrenheit: {celsius_to_fahrenheit(readings[0])}')
    print(f'First reading in Celsius (converted back from Fahrenheit): {fahrenheit_to_celsius(celsius_to_fahrenheit(readings[0]))}')
