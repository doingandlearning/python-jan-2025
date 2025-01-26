CELSIUS = "Celsius"
FAHRENHEIT = "Fahrenheit"

class TemperatureReading:
    def __init__(self, temp, date, location, scale=CELSIUS):
        self.temp = temp
        self.date = date
        self.location = location
        self.scale = scale

    def __repr__(self):
        return f'TemperatureReading({self.temp}, {self.date}, {self.location}, {self.scale})'

    def __str__(self):
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

    # Step 1: Equals method
    def __eq__(self, other):
        if isinstance(other, TemperatureReading):
            return self.temp == other.temp and self.scale == other.scale
        return False

    # Step 2: Addition and Subtraction methods
    def __add__(self, other):
        if isinstance(other, (int, float)):
            new_value = self.temp + other
        elif isinstance(other, TemperatureReading):
            if self.scale == other.scale:
                new_value = self.temp + other.temp
            else:
                raise ValueError("Cannot add temperatures with different scales")
        else:
            return NotImplemented
        return TemperatureReading(new_value, self.date, self.location, self.scale)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            new_value = self.temp - other
        elif isinstance(other, TemperatureReading):
            if self.scale == other.scale:
                new_value = self.temp - other.temp
            else:
                raise ValueError("Cannot subtract temperatures with different scales")
        else:
            return NotImplemented
        return TemperatureReading(new_value, self.date, self.location, self.scale)

    # Step 3: Further comparison operators
    def __lt__(self, other):
        if isinstance(other, TemperatureReading):
            if self.scale == other.scale:
                return self.temp < other.temp
            else:
                raise ValueError("Cannot compare temperatures with different scales")
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, TemperatureReading):
            if self.scale == other.scale:
                return self.temp <= other.temp
            else:
                raise ValueError("Cannot compare temperatures with different scales")
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, TemperatureReading):
            if self.scale == other.scale:
                return self.temp > other.temp
            else:
                raise ValueError("Cannot compare temperatures with different scales")
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, TemperatureReading):
            if self.scale == other.scale:
                return self.temp >= other.temp
            else:
                raise ValueError("Cannot compare temperatures with different scales")
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

# Utility functions for conversion (assume these are already provided)
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Example Usage

# Create some TemperatureReading instances
temp1 = TemperatureReading(13.5, '01/05/20', 'London', CELSIUS)
temp2 = TemperatureReading(15.5, '01/05/20', 'London', CELSIUS)
temp3 = TemperatureReading(14.6, '05/05/20', 'London', CELSIUS)

# Adding temperatures together
print('Add two temperatures:', temp1 + temp2)

# Adding an int to a temperature
print('Add a temperature and an int:', temp1 + 5)

# Adding a float to a temperature
print('Add a temperature and a float:', temp1 + 5.5)

# Comparison operations
print('temp1 == temp2:', temp1 == temp2)
print('temp1 != temp2:', temp1 != temp2)
# print('temp1 < temp2:', temp1 < temp2)
# print('temp1 > temp3:', temp1 > temp3)
# print('temp1 >= temp3:', temp1 >= temp3)
# print('temp1 <= temp3:', temp1 <= temp3)

# Sorting based on the implemented operators
temperatures = [temp1, temp2, temp3]
sorted_temperatures = sorted(temperatures)
print('Sorted temperatures:', sorted_temperatures)
