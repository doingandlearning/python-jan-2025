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