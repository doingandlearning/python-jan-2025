# Flow of Control

---

## Plan for Session

- If statement
- Using else and elif
- Nesting if statements
- Comparison Operators
- Logical Operators
- If expressions
- True and False
- While Loops
- For loops
- Break and Continue

---

## The if Statement

### Basic Structure

- Note indentation.

### Simple Example:

```python
num = int(input('Enter a number: '))

if num > 0:
    print(num, 'is positive')
```

### Extending the Example:

```python
num = int(input('Enter another number: '))

if num > 0:
    print(num, 'is positive')
    print(num, 'squared is', num * num)

print('Bye')
```

- Layout is key in Python; it helps define the structure of the program.

---

## Using else and elif

- Optionally can have else.
- Also additional conditional tests.

### Example:

```python
num = int(input('Enter yet another number: '))

if num < 0:
    print('It\'s negative')
else:
    print('It\'s not negative')
```

```python
savings = float(input("Enter how much you have in savings: "))

if savings == 0:
    print("Sorry, no savings")
elif savings < 500:
    print('Well done')
else:
    print('Thank you')
```

- Can have multiple elif conditions.

---

## Nesting if Statements

- Can nest one if statement inside another.

### Example:

```python
snowing = True
temp = -1

if temp < 0:
    print('It is freezing')
    if snowing:
        print('Put on boots')
    print('Time for Hot Chocolate')

print('Bye')
```

- Note style of checking for snowing – it is already a bool.

---

## Comparison Operators

- Return True or False.

| Operator | Description                                                                   | Example  |
| -------- | ----------------------------------------------------------------------------- | -------- |
| `==`     | Tests if two values are equal                                                 | `3 == 3` |
| `!=`     | Tests that two values are not equal to each other                             | `2 != 3` |
| `<`      | Tests if the left-hand value is less than the right-hand value                | `2 < 3`  |
| `>`      | Tests if the left-hand value is greater than the right-hand value             | `3 > 2`  |
| `<=`     | Tests if the left-hand value is less than or equal to the right-hand value    | `3 <= 4` |
| `>=`     | Tests if the left-hand value is greater than or equal to the right-hand value | `5 >= 4` |

---

## Logical Operators

- Combine Boolean expressions together.
- Can use logical operations to combine Boolean conditions together.

| Operator | Description                                          | Example           |
| -------- | ---------------------------------------------------- | ----------------- |
| `and`    | Returns True if both left and right are true         | `3 < 4 and 5 > 4` |
| `or`     | Returns True if either the left or the right is true | `3 < 4 or 3 > 5`  |
| `not`    | Returns True if the value being tested is False      | `not 3 < 2`       |

### Example:

```python
age = 15
status = None

if age > 12 and age < 20:
    status = 'teenager'
else:
    status = 'not teenager'

print(status)
```

---

## If Expressions

- Shorthand form of an if statement that returns a value.
- Has the form:
  ```python
  <result1> if <condition-is-met> else <result2>
  ```

### Example:

```python
age = 15
status = 'teenager' if age > 12 and age < 20 else 'not teenager'
print(status)
```

---

## A Note on True and False

- Python is flexible on what is equivalent to True and False.
  - `0`, `''` (empty strings), `None` equate to False.
  - Non-zero, non-empty strings, any object equate to True.
- Best practice is to use `True` and `False`.

---

## While (Conditional) Loops

### Basic Form:

```python
while <test-condition-is-true>:
    statement or statements
```

### Example:

```python
valid_data = False

while not valid_data:
    age = int(input('Please enter your age: '))
    if age < 0 or age > 120:
        print('Invalid Age')
    else:
        valid_data = True

print('Done')
```

- No do-while loop in Python.

---

## For Loop

### Basic Form:

- Iterates over an iterable.
- Note the indentation.

### Example:

```python
# Loop over a set of values in a range
print('Print out values in a range')

for i in range(0, 10):
    print(i, ' ', end='')

print('Done')
```

- Can also do:

```python
# Increment by 2
for i in range(0, 10, 2):
    print(i, ' ', end='')

print('Done')
```

- Can also count down:

```python
# Count down
for i in range(10, 0, -2):
    print(i, ' ', end='')

print('Done')
```

---

## Break Loop Statement

- Can choose to break out of a loop.

### Example:

```python
num = int(input('Enter a number to check for: '))

for i in range(0, 6):
    if i == num:
        break
    print(i, ' ', end='')

print('Done')
```

---

## Continue Loop Statement

- Can choose to skip the current iteration.

### Example:

```python
for i in range(0, 10):
    print(i, ' ', end='')
    if i % 2 == 1:
        continue
    print('hey, it\'s an even number')
    print('we love even numbers')

print('Done')
```

---

## Questions?

?
