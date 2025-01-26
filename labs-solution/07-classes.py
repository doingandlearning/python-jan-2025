CELSIUS = "Celsius"  # Magic strings!
FAHRENHEIT = "Fahrenheit"

class TemperatureReading:
    """
    TemperatureReading represents a temperature measurement at a specific location and date,
    with the option to specify the scale (Celsius or Fahrenheit).
    """
    def __init__(self, temp: float, date: str, location:str, scale=CELSIUS):
        self.temp = temp
        self.date = date
        self.location = location
        self.scale = scale

    def __repr__(self): # Machine Readable Representation
        return f'TemperatureReading({self.temp}, {self.date}, {self.location}, {self.scale})'

    def __str__(self): # Human Readable Representation
        return f'TemperatureReading[{self.scale}]({self.temp} on {self.date} at {self.location})'


    def convert(self):
        """Convert the temperature to the opposite scale."""
        if self.scale == CELSIUS:
            new_temp = celsius_to_fahrenheit(self.temp)
            return TemperatureReading(new_temp, self.date, self.location, FAHRENHEIT)
        elif self.scale == FAHRENHEIT:
            new_temp = fahrenheit_to_celsius(self.temp)
            return TemperatureReading(new_temp, self.date, self.location, CELSIUS)
        else:
            raise ValueError("Unknown temperature scale")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def extract_temp(reading):
    """Extracts the temperature from a TemperatureReading object."""
    return reading.temp

def average(data):
    """Returns the average temperature from a list of TemperatureReading objects."""
    return sum(map(extract_temp, data)) / len(data)

def median(data):
    """Calculates the median temperature from a list of TemperatureReading objects."""
    sorted_data = sorted(data, key=extract_temp)
    data_length = len(sorted_data)
    index = (data_length - 1) // 2
    if data_length % 2 == 1:  # Checks for an odd number
        return sorted_data[index]
    else:
        return (extract_temp(sorted_data[index]) + extract_temp(sorted_data[index + 1])) / 2.0

def minimum(data, index=0):
    """Returns the minimum temperature from a list of TemperatureReading objects."""
    return min(data[index:], key=extract_temp)

def maximum(data, index=0):
    """Returns the maximum temperature from a list of TemperatureReading objects."""
    return max(data[index:], key=extract_temp)

def data_range(data):
    """Returns the minimum and maximum temperature readings."""
    return minimum(data), maximum(data)

# Sample readings
readings = [
    TemperatureReading(13.5, '01/05/20', 'London', CELSIUS),
    TemperatureReading(12.6, '02/05/20', 'London', CELSIUS),
    TemperatureReading(15.3, '03/05/20', 'London', CELSIUS),
    TemperatureReading(12.2, '04/05/20', 'London', CELSIUS),
    TemperatureReading(16.6, '05/05/20', 'London', CELSIUS),
    TemperatureReading(14.6, '05/05/20', 'London', CELSIUS),
    TemperatureReading(15.6, '05/05/20', 'London', CELSIUS)
]

# Print the list of readings using __repr__
print(readings)

# Print the list of readings using __str__
print(*readings)

for reading in readings:
  print(str(reading))

# Display summary statistics with the new class
print(f'Average temperature: {average(readings)}')
print(f'Median temperature: {median(readings)}')
print(f'Minimum temperature: {minimum(readings)}')
print(f'Maximum temperature: {maximum(readings)}')
print(f'Temperature range: {data_range(readings)}')

# Example of conversion
temp1 = TemperatureReading(13.5, '01/05/20', 'London', CELSIUS)
temp2 = temp1.convert()
print(f'temp1: {temp1}')
print(f'temp2: {temp2}')
