# Plan for Session
- Why have Operator Overloading?
- Defining Operators
- Numerical Operators
- Comparison Operators
- Logical Operators

---

## Why have Operator Overloading?
- Allows user-defined classes to have a natural way of using operators such as `+`, `-`, `/`, `*`, `<`, `>`, `==`, `!=`, `and`, `or`, `not`.
- Leads to more succinct and readable code.
- Makes user-defined types feel more integrated with Python.

### Example:
```python
q1 = Quantity(5)
q2 = Quantity(10)
q3 = q1 + q2

# Versus
q1 = Quantity(5)
q2 = Quantity(10)
q3 = q1.add(q2)
```

---

## Defining Operators
- To implement operators in a class, need to implement special methods.
- Each operator has an associated special method.
- All such methods start and end with a double underbar (`__`).
- For example:
  - `add(+)` is implemented by `__add__(self, other)`
  - `subtract(-)` by `__sub__(self, other)`

### Example - Defining Operators:
```python
class Quantity:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        new_value = self.value + other.value
        return Quantity(new_value)

    def __sub__(self, other):
        new_value = self.value - other.value
        return Quantity(new_value)

    def __str__(self):
        return 'Quantity[' + str(self.value) + ']'

q1 = Quantity(5)
q2 = Quantity(10)
print('q1 =', q1, 'q2 =', q2)

q3 = q1 + q2
print('q3 =', q3)
```
- Note: `Quantity` is immutable. Adding two quantities together generates a new quantity.

---

## Numerical Operators
| Operator | Expression | Method |
| --- | --- | --- |
| Addition | `q1 + q2` | `__add__(self, q2)` |
| Subtraction | `q1 - q2` | `__sub__(self, q2)` |
| Multiplication | `q1 * q2` | `__mul__(self, q2)` |
| Power | `q1 ** q2` | `__pow__(self, q2)` |
| Division | `q1 / q2` | `__truediv__(self, q2)` |
| Floor Division | `q1 // q2` | `__floordiv__(self, q2)` |
| Modulo (Remainder) | `q1 % q2` | `__mod__(self, q2)` |

---

## Adding Numerical Operators to the Quantity Type
### Example:
```python
class Quantity:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        new_value = self.value + other.value
        return Quantity(new_value)

    def __sub__(self, other):
        new_value = self.value - other.value
        return Quantity(new_value)

    def __mul__(self, other):
        new_value = self.value * other.value
        return Quantity(new_value)

    def __truediv__(self, other):
        new_value = self.value / other.value
        return Quantity(new_value)

q1 = Quantity(5)
q2 = Quantity(10)
print('q1 =', q1, 'q2 =', q2)

q3 = q1 + q2
print('q3 =', q3)
print('q2 - q1 =', q2 - q1)

print('q1 * q2 =', q1 * q2)
print('q1 / q2 =', q1 / q2)
```

---

## Using Integers with Quantities
- May want to use integers with Quantities.

### Example:
```python
class Quantity:
    def __mul__(self, other):
        if isinstance(other, int):
            new_value = self.value * other
        else:
            new_value = self.value * other.value
        return Quantity(new_value)

    def __truediv__(self, other):
        if isinstance(other, int):
            new_value = self.value / other
        else:
            new_value = self.value / other.value
        return Quantity(new_value)

q1 = Quantity(5)
q2 = Quantity(10)

print('q1 * 2', q1 * 2)
print('q2 / 2', q2 / 2)
```
- Can use `isinstance` to check the type of a parameter, providing useful flexibility.

---

## Comparison Operators
| Operator | Expression | Method |
| --- | --- | --- |
| Less than | `q1 < q2` | `__lt__(q1, q2)` |
| Less than or equal to | `q1 <= q2` | `__le__(q1, q2)` |
| Equal to | `q1 == q2` | `__eq__(q1, q2)` |
| Not equal to | `q1 != q2` | `__ne__(q1, q2)` |
| Greater than | `q1 > q2` | `__gt__(q1, q2)` |
| Greater than or equal to | `q1 >= q2` | `__ge__(q1, q2)` |

---

## Adding Comparison Operators to the Quantity Type
### Example:
```python
class Quantity:
    def __init__(self, value=0):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

q1 = Quantity(5)
q2 = Quantity(10)

print('q1 =', q1, 'q2 =', q2)

q3 = q1 + q2
print('q3 =', q3)

print('q1 < q2:', q1 < q2)
print('q3 > q2:', q3 > q2)
print('q3 == q1:', q3 == q1)
```

---

## Logical Operators
| Operator | Expression | Method |
| --- | --- | --- |
| And | `q1 and q2` | `__and__(self, q2)` |
| OR | `q1 or q2` | `__or__(self, q2)` |
| NOT | `not q1` | `__not__(self)` |

- Logical Operators don’t make sense for the `Quantity` type (e.g., what is the meaning of `q1 and q2`?).
- Only use operators when they make sense!

---

## Questions?

?
