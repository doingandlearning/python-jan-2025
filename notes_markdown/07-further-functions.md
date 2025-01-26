# Plan for Session
- Local & Global Variables
- Modifying Globals within a function
- Anonymous / Lambda Functions
- Functions and Containers
  - filter
  - map
  - nesting filter and map

---

## Local & Global Variables
- Variables can be declared as being global (to the program) or local to a function.
- Local variables can only be referenced within the scope they are defined in.
- Global variables can be referenced anywhere.

### Example:
```python
a_global_count = 10

def some_func():
    a_local_variable = 100
    print('a_local_variable:', a_local_variable)
    print('a_global_count:', a_global_count)

some_func()
```

---

## Modifying Globals within a Function
- By default, local variables will hide global variables with the same name (known as 'Shadowing').

### Example:
```python
def my_function():
    a_variable = 100
    print('inside function:', a_variable)

a_variable = 25

print('before function:', a_variable)
my_function()
print('outside function:', a_variable)
```

- To modify a global variable within a function, it must first be declared as `global` inside the function before use.

### Example:
```python
max = 100

print('initial value of max:', max)

def print_max():
    global max
    max = max + 1
    print('inside function:', max)

print_max()
print('outside function:', max)
```

---

## Anonymous / Lambda Functions
- Can define anonymous functions, also known as lambda functions.
- Can optionally take parameters.
- Always return a value.

### Syntax:
```python
lambda arguments: expression
```

### Example:
```python
func0 = lambda: print('no args')
func1 = lambda x: x * x
func2 = lambda x, y: x * y
func3 = lambda x, y, z: x + y + z

func0()
print(func1(4))
print(func2(3, 4))
print(func3(2, 3, 4))
```

---

## Functions and Containers
- Functional programming style operations available on containers, also known as Higher Order Functions.

### filter()
- Filters out elements from a collection.
- The returned iterable is the same size or smaller than the original collection.

### map()
- Applies a function to all elements in a collection.
- The returned iterable is always the same size as the original.

### Example Using filter():
```python
data = [1, 3, 5, 2, 7, 4, 10]
print('data:', data)

# Filter for even numbers using a lambda function
d1 = list(filter(lambda i: i % 2 == 0, data))
print(f'filtered d1: {d1}')

def is_even(i):
    return i % 2 == 0

d2 = list(filter(is_even, data))
print(f'filtered d2: {d2}')
```

### Example Using map():
```python
data = [1, 3, 5, 2, 7, 4, 10]
print('data:', data)

# Apply the lambda function to each element in the list using the map function
d1 = list(map(lambda i: i + 1, data))
print('d1:', d1)

def add_one(i):
    return i + 1

# Apply the add_one function to each element in the list using the map function
d2 = list(map(add_one, data))
print('d2:', d2)
```

### Nesting Operations
- Can nest operations: apply `filter` to initial data to find even numbers, use `map` to add 10 to the iterable returned from `filter`.

### Example:
```python
data = [1, 3, 5, 2, 7, 4, 10]
print('data:', data)

def is_even(i):
    return i % 2 == 0

# Filter for even numbers and use map to add 10
new_data = list(map(lambda i: i + 10, filter(is_even, data)))
print('new_data:', new_data)
```

---

## Questions?

?
