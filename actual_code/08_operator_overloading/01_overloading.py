print(1 + 34)
print("Hello " + "World")

# +  -> __add__
# -  -> __sub__
# /  -> __truediv  (// -> __floordiv)
# *  -> __mul__
# ** -> __pow__
# %  -> __mod__
# <  -> __lt__
# >  -> __gt__
# =  -> __eq__
# <= -> __le__
# and -> __and__


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

q1 = Quantity(10)
q2 = Quantity(15)

q3 = q1 - q2  # Operator overloading
print(q3)

q4 = q1.add(q2)
print(q4)

print(q1 * 5) # Quantity(50)

print(q1 * q2)  # Quantity(150)

print(q2 > q1)
print(Quantity(3) <= Quantity(3))
#
# if q1 and q2:
#     print("Both servers running")
#
# if q1 or q2:
#
# if not q1:
