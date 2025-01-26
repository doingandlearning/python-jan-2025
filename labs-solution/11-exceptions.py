from utils import celsius_to_fahrenheit, fahrenheit_to_celsius
from readings import Reading

class InvalidTemperatureException(ValueError):
    """Represents an invalid Temperature reading"""
    def __init__(self, value, message):
        super().__init__(message)
        self.value = value
        self.message = message

    def __str__(self):
        return f'InvalidTemperatureException({self.value}, {self.message})'

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
        if isinstance(other, (int, float)): # temperature + (int, float)
            new_value = self.value + other
        elif isinstance(other, TemperatureReading):
            if self.scale == other.scale: 
                new_value = self.value + other.value
            else:
                raise ValueError("Cannot add temperatures with different scales")
        else:
            raise InvalidTemperatureException(other, 'Invalid type for addition to TemperatureReading')
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
            raise InvalidTemperatureException(other, 'Invalid type for subtraction from TemperatureReading')
        return TemperatureReading(new_value, self.date, self.location, self.scale)

if __name__ == "__main__":
    try:
        result = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') + '5.5'
    except InvalidTemperatureException as e:
        print(e)

    try:
        result = TemperatureReading(13.5, '01/05/20', 'London', 'Celsius') - [5.5]
    except InvalidTemperatureException as e:
        print(e)
