# Variables, Types, and Operations

**Kevin Cunningham**

---

## Plan for Session

- Variables
- Variable Naming Conventions
- Variables and Types
- Converting Types
- Strings & String Formatting
- Numbers
- Arithmetic Operations
- Assignment Operators
- None Value
- Comments

---

## Variables

### Simplest Hello World Program

```python
print('Hello World')
```

### Making it Interactive

```python
# Print out a message and then ask the user for input
print('Hello world')
user_name = input('Enter your name: ')
print('Hello ' + user_name)
```

- `user_name` is a variable.

---

## Variable Naming Conventions

- **All lowercase**
- **Descriptive names** (e.g., `my_name`, `your_name`)
- **Words separated by underscores**
  - Examples:
    - `my_name`, `user_name`, `account_name`
    - `count`, `total_number_of_users`, `percentage_passed`
    - `office_address`, `house_number`
    - `is_okay`, `is_correct`, `status_flag`
- **Exceptions**:
  - Variables like `i` and `j` in looping constructs.

---

## Variables and Types

- Variables can hold different types.
- Python is a **dynamically typed language** (not an untyped language).

### Example:

```python
my_variable = 422
print(my_variable)
print(type(my_variable))

my_variable = 'Adam'
print(my_variable)
print(type(my_variable))

my_variable = True
print(my_variable)
print(type(my_variable))
```

---

## Strings in Python

- Represented by an ordered sequence of characters.
- Strings are **immutable** (string operations produce a new string).
- Created using single, double, or triple quotes.

### Example:

```python
my_variable = 'Bob'
print(my_variable)

my_variable = "Eloise"
print(my_variable)

# A multi-line string
my_variable = """Hello
World"""
print(my_variable)
```

---

## Strings in Python (Continued)

- Find the length of a string.
- Can concatenate strings (note overloading of `+` operator).
- **Concatenation Example**:

```python
string_1 = 'Good'
string_2 = " day"
string_3 = string_1 + string_2
print(string_3)

my_string = 'Hello World'
print(len(my_string))

msg = 'Hello Lloyd you are ' + str(21)
print(msg)
```

---

## String Operations

- Many operations available.

### Example:

```python
msg = 'Hello World'
print(msg.replace("Hello", "Goodbye"))

print('Edward Alan Rawlings'.find('Alan'))
print('Edward John Rawlings'.find('Alan'))

print('James' == 'James')  # prints True
print('James' != 'John')  # prints True

print(msg.startswith('H'))
print(msg.endswith('d'))
print(msg.upper())

print('Hello-World'[1:5])  # a slice
```

---

## String Formatting

- Simplest approach uses **f-strings** (available since Python 3.6).
- **f-strings** are string literals with an `f` at the beginning and curly braces containing Python expressions.

### Example:

```python
name = "Adam"
age = 22
message = f"Hello {name}, you are {age}"
print(message)
```

---

## Numbers

- Two types: **Integers** and **Floats**.
- Can convert between types.

### Example:

```python
count = 1
print(count)
print(type(count))

exchange_rate = 1.83
print(exchange_rate)
print(type(exchange_rate))

print(float(count))
print(int(exchange_rate))
```

---

## Arithmetic Operations

| Operator | Description                                                | Example   |
| -------- | ---------------------------------------------------------- | --------- |
| `+`      | Add the left and right values together                     | `1 + 2`   |
| `-`      | Subtract the right value from the left value               | `3 - 2`   |
| `*`      | Multiply the left and right values                         | `3 * 4`   |
| `/`      | Divide the left value by the right value (returns float)   | `12 / 3`  |
| `//`     | Integer division (ignores any remainder)                   | `12 // 3` |
| `%`      | Modulus (returns the remainder)                            | `13 % 3`  |
| `**`     | Exponent (raises the left value to the power of the right) | `3 ** 4`  |

---

## Assignment Operators

| Operator | Description                                         | Example   | Equivalent   |
| -------- | --------------------------------------------------- | --------- | ------------ |
| `+=`     | Add the value to the left-hand variable             | `x += 2`  | `x = x + 2`  |
| `-=`     | Subtract the value from the left-hand variable      | `x -= 2`  | `x = x - 2`  |
| `*=`     | Multiply the left-hand variable by the value        | `x *= 2`  | `x = x * 2`  |
| `/=`     | Divide the variable's value by the right-hand value | `x /= 2`  | `x = x / 2`  |
| `//=`    | Use integer division to divide the variable's value | `x //= 2` | `x = x // 2` |
| `%=`     | Use the modulus operator                            | `x %= 2`  | `x = x % 2`  |
| `**=`    | Apply the power of operator                         | `x **= 3` | `x = x ** 3` |

---

## Converting Types

- A value can be converted from one type to another using a conversion function.

### Example:

```python
a_string = '32'
print(f'a_string {a_string} is {type(a_string)}')

an_int = int(a_string)
print(f'an_int {an_int} is {type(an_int)}')

a_float = float(a_string)
print(f'a_float {a_string} is {type(a_float)}')

another_string = str(42)
print(f'another_string {a_string} is {type(another_string)}')
```

---

## None Value

- Special type `NoneType` with a single value `None`.
- Can assign to variables and test for it.
- Use `is None` and `is not None` to test for `None`.

### Example:

```python
winner = None
print('winner:', winner)
print('winner is None:', winner is None)
print('winner is not None:', winner is not None)

winner = 'Player 1'
print('winner:', winner)
print('winner is None:', winner is None)
print('winner is not None:', winner is not None)
```

---

## Comments

- Comments are represented by a `#`.

### Example:

```python
# Set up the winner variable to hold None
winner = None
print('winner:', winner)

# Check to see if there is a winner
print('winner is None:', winner is None)
print('winner is not None:', winner is not None)

# Print out the winner's type
print(type(winner))
```

---

## Questions?

?
