class Quantity:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"Quantity({self.amount})"

    def __add__(self, other):
        # new_amount = self.amount + other.amount
        # return Quantity(new_amount)
        return Quantity(self.amount + other.amount)

    def __sub__(self, other):
        return Quantity(self.amount - other.amount)

    def __mul__(self, other):
        if isinstance(other, int):
            new_value = self.amount * other
        elif isinstance(other, Quantity):
            new_value = self.amount * other.amount
        else:
            raise TypeError("Must multiply by Quantity or int")
        return Quantity(new_value)

    def add(self, other):
        return Quantity(self.amount + other.amount)

    def __gt__(self, other):
        return self.amount > other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __ge__(self, other):
        return self.amount >= other.amount