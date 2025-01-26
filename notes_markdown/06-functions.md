# Plan for Session
- Defining Functions
- Zero single and multiple parameter options
- Default Parameter Values
- Named Parameters
- Returning Values
- Returning Multiple Values
- Arbitrary Parameter Lists

---

## Defining Functions
- Basic Syntax

```python
def function_name(parameter_list):
    """docstring"""
    statement
    statement(s)
```
- As always, note the indentation.
- All (named) functions are defined using the keyword `def`.
- Can have named and anonymous/lambda functions.
- Parameter list is optional.
- Colon marks the end of the function header before the function body.
- Optional docstring.
- One or more (indented) statements form the function body.
- Must be defined before use.

---

## Example Functions
- Simplest function – no parameters & no return value.

### Example:
```python
def print_msg():
    print('Hello World!')
    
print_msg()
```

- Can also provide a parameter.

### Example:
```python
def print_my_msg(msg):
    print(msg)
    
print_my_msg('Hello World')
print_my_msg('Good day')
print_my_msg('Welcome')
print_my_msg('Hola')
```

---

## Multiple Parameters
- Functions can have multiple parameters, separated by commas.

### Example:
```python
def greeter(name, message):
    print('Welcome', name, '-', message)
    
greeter('Eloise', 'Hope you like Rugby')
```

---

## Default Parameter Values
- Can have default parameter values.

### Example:
```python
def greeter(name, message='Live Long and Prosper'):
    print('Welcome', name, '-', message)
    
greeter('Eloise')
greeter('Eloise', 'Hope you like Rugby')
```

### Note:
- Two concepts: mandatory parameters and optional parameters.
- Optional parameters have a default value.
- Once one parameter has a default value, all parameters to the right must also have default values.

### Example:
```python
def greeter(name, title='Dr', prompt='Welcome', message='Live Long and Prosper'):
    print(prompt, title, name, '-', message)
```

---

## Named Parameters
- Can select which parameters to use via the parameter names (aka named parameters).

### Example:
```python
greeter('Lloyd', message='We like Python')
greeter(name='Lloyd', message='We like Python')
greeter(message='We like Python', name='Lloyd')
```

---

## Returning Values
- Can return a value using the `return` statement.

### Example:
```python
def square(n):
    return n * n

result = square(4)
print(result)

print(square(5))

if square(3) < 15:
    print('Still less than 15')
```

---

## Returning Multiple Values
- Return a comma-separated list of values.

### Example:
```python
def swap(a, b):
    return b, a

a = 2
b = 3

x, y = swap(a, b)
print(x, ':', y)

z = swap(a, b)
print(z)
```

---

## Arbitrary Parameter Lists
- Variable number of arguments, marked with an asterisk (*).

### Example:
```python
def greeter(*names):
    for name in names:
        print('Welcome', name)
        
greeter('John', 'Denise', 'Phoebe', 'Adam', 'Gryff', 'Natalia')
```

---

## Example Built-in Functions
- `sum` function takes a list and an (optional) initial value.

### Example:
```python
data = [1, 3, 5, 2, 7, 4, 10]
result = sum(data)
print(f'sum of data: {result}')

result = sum(data, 10)
print(f'sum of data (initial value 10): {result}')

result = sum(data, start=10)
print(f'sum of data (start=10): {result}')
```

---

## Questions?


