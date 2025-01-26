from utils import celsius_to_fahrenheit, fahrenheit_to_celsius

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