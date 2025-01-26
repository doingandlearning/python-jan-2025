# Plan for Session
- Generators
- Generator Functions
- Generator with a `for` loop
- When do `yield` statements execute?
- An Even Number Generator
- Generator Expression

---

## Generators
- May not be possible to generate all data for iteration; may need a way to lazily generate the data.
- Generators are a special function that can be used to generate a sequence of values to be iterated over on demand.
- The only thing that makes a generator a generator function is the use of the `yield` keyword.
- On execution of the `yield` expression, the function is suspended, and the value of `yield` is returned until the next cycle of the loop.

---

## Generator Functions
- A very simple generator function:

### Example:
```python
def gen_numbers():
    yield 1
    yield 2
    yield 3
```
- It’s a generator function as it has at least one `yield` statement.
- Each time it is called, it will return a `yield` value, then suspend until the next invocation.
- Will terminate after the third `yield`.

---

## Generator with a `for` Loop
- Can use the `gen_numbers()` function with a `for` loop.
- The generator function can have a sequence of `yield` statements or may have its own internal loop that generates `yield` values.
- The loop is suspended along with the function.

### Example:
```python
for i in gen_numbers():
    print(i)
```
- Output:
  - `1`
  - `2`
  - `3`

---

## When Do `yield` Statements Execute?
- The generator function is suspended when the `yield` value is supplied and only resumed when the next request is received.

### Example:
```python
def gen_numbers2():
    print('Start')
    yield 1
    print('Continue')
    yield 2
    print('Final')
    yield 3
    print('End')

for i in gen_numbers2():
    print('-', end='')
    print(i, end='')
    print('*')
```
- Output:
  - `Start`
  - `-1*`
  - `Continue`
  - `-2*`
  - `Final`
  - `-3*`
  - `End`
- Notice that the `yield` value is only generated when required.

---

## An Even Number Generator
- An Evens number generator function implemented as a generator function.
- Can be called multiple times—yielding a value each time.

### Example:
```python
def evens_up_to(limit):
    value = 0
    while value <= limit:
        yield value
        value += 2

for i in evens_up_to(6):
    print(i, end=' ')
```
- Output:
  - `0 2 4 6`

---

## Generator Expression
- A more concise way to create a generator is by enclosing the expression within round brackets `()`.

### Example:
```python
# Create a generator expression
gen = (x * 2 for x in range(10))

# Use the generator expression
for i in gen:
    print(i, end=' ')
print()
```
- Output:
  - `0 2 4 6 8 10 12 14 16 18`

---

## Questions?

?
