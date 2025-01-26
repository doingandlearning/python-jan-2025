# Step 1: Define the Reading Class
class Reading:
    def __init__(self, value, date, location):
        self.value = value
        self.date = date
        self.location = location

    def __repr__(self):
        return f'Reading({self.value}, {self.date}, {self.location})'

    def __eq__(self, other):
        if isinstance(other, Reading):
            return self.value == other.value and self.date == other.date and self.location == other.location
        return False

    def __lt__(self, other):
        if isinstance(other, Reading):
            return self.value < other.value
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Reading):
            return self.value <= other.value
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Reading):
            return self.value > other.value
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Reading):
            return self.value >= other.value
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

# Step 2: Change TemperatureReading to Extend the Reading Class

class TemperatureReading(Reading):
    def __init__(self, temp, date, location, scale='Celsius'):
        super().__init__(temp, date, location)
        self.scale = scale

    def __repr__(self):
        return f'TemperatureReading[{self.scale}]({self.value} on {self.date} at {self.location})'

    def convert(self):
        if self.scale == 'Celsius':
            new_temp = celsius_to_fahrenheit(self.value)
            return TemperatureReading(new_temp, self.date, self.location, 'Fahrenheit')
        elif self.scale == 'Fahrenheit':
            new_temp = fahrenheit_to_celsius(self.value)
            return TemperatureReading(new_temp, self.date, self.location, 'Celsius')
        else:
            raise ValueError("Unknown temperature scale")

    def __add__(self, other):
        if isinstance(other, (int, float)):
            new_value = self.value + other
        elif isinstance(other, TemperatureReading):
            if self.scale == other.scale:
                new_value = self.value + other.value
            else:
                raise ValueError("Cannot add temperatures with different scales")
        else:
            return NotImplemented
        return TemperatureReading(new_value, self.date, self.location, self.scale)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            new_value = self.value - other
        elif isinstance(other, TemperatureReading):
            if self.scale == other.scale:
                new_value = self.value - other.value
            else:
                raise ValueError("Cannot subtract temperatures with different scales")
        else:
            return NotImplemented
        return TemperatureReading(new_value, self.date, self.location, self.scale)

# Step 3: Define the RainfallReading Class

class RainfallReading(Reading):
    def __init__(self, value, date, time, location):
        super().__init__(value, date, location)
        self.time = time

    def __repr__(self):
        return f'RainfallReading[{self.time}]({self.value} on {self.date} at {self.location})'

    def __add__(self, other):
        if isinstance(other, (int, float)):
            new_value = self.value + other
        elif isinstance(other, RainfallReading):
            if self.date == other.date and self.location == other.location:
                new_value = self.value + other.value
            else:
                raise ValueError("Cannot add rainfall readings with different dates or locations")
        else:
            return NotImplemented
        return RainfallReading(new_value, self.date, self.time, self.location)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            new_value = self.value - other
        elif isinstance(other, RainfallReading):
            if self.date == other.date and self.location == other.location:
                new_value = self.value - other.value
            else:
                raise ValueError("Cannot subtract rainfall readings with different dates or locations")
        else:
            return NotImplemented
        return RainfallReading(new_value, self.date, self.time, self.location)

# Utility functions for conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Step 4: Example Usage

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

# Working with Temperature readings
temp1 = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius')
temp2 = TemperatureReading(15.5, '01/05/20', 'London', 'Celsius')
temp3 = TemperatureReading(14.6, '05/05/20', 'London', 'Celsius')

print('Temperature addition:', temp1 + temp2)
print('Temperature comparison (temp1 < temp3):', temp1 < temp3)
