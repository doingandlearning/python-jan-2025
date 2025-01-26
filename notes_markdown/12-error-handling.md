# Plan for Session
- Errors & Exceptions
- Exception types in Python
- Exception Handling
- `try-except` blocks
- Default Exception Handler
- `else` Clause
- `finally` block
- Raising an Exception / Error
- Defining New Exceptions / Errors

---

## Errors & Exceptions
- Exceptions and Errors are objects in Python.
- Can occur in a variety of situations:
  - File does not exist
  - Network connection fails
  - Import Error at runtime
  - Arithmetic Error (such as divide by zero)
  - Module load error
- Want to be notified about these and take appropriate action.

---

## Exception Types in Python
- Error and Exception types are classes instantiated at runtime.
- Creation is known as raising an error/exception.
- Root is the `BaseException` class, but all errors and exceptions extend `Exception`.
- No distinction in Python between errors & exceptions.
- Several subclasses of `Exception`:
  - `ArithmeticException`: numeric errors.
  - `SyntaxError`: raised when the parser encounters a syntax issue.
  - `RuntimeError`: problem encountered at runtime.

---

## Exception Handling
- Based on C++ and similar to Java.
- An exception is raised by instantiating an exception class, then thrown from where it is generated, and caught where it is handled.
- Exception handling blocks manage how exceptions are handled: `try`, `except`, `else`, `finally` blocks, and the `raise` statement.

---

## Exception Handling Example
### Example:
```python
try:
    run_calculation(6)
except ZeroDivisionError:
    print('oops')
```
- The `run_calculation` function can raise the `ZeroDivisionError`.
- Enters the `try` block. If all is okay, it runs `run_calculation` and jumps to the line after `print`.
- If `run_calculation` raises an exception, it jumps to the `except` clause and checks if the exception is a `ZeroDivisionError` (or subclass). If it is, it runs the `print` statement.

---

## Handling Multiple Exceptions
### Example:
```python
try:
    run_calculation(6)
except ZeroDivisionError:
    print('oops')
except IndexError:
    print('arrgh')
except FileNotFoundError:
    print('huh!')
except Exception:
    print('Duh!')
```
- If an error/exception is raised, Python checks each type in turn, starting with the first `except` and also checks for subclasses.

---

## Accessing the Exception Object
- Possible to access the exception object being caught.
- If multiple `except` clauses, can choose to access the exception object or not.

### Example:
```python
try:
    run_calculation(6)
except ZeroDivisionError as exp:
    print(exp)
    print('oops')
```
- Output:
  - `division by zero`
  - `oops`

---

## `else` Clause
- Can also have an optional `else` clause.
- If `else` clause is present, then it must come after all `except` clauses.
- The `else` clause is executed if and only if no exceptions were raised. If any exception was raised, the `else` clause will not be run.

### Example:
```python
try:
    my_function(6, 2)
except ZeroDivisionError as e:
    print(e)
else:
    print('Everything worked OK')
```

---

## `finally` Clause
- Optional `finally` clause.
- Last clause in the statement, must come after any `except` clauses as well as the `else` clause.
- Will always run whether an exception occurred or not.

### Example:
```python
try:
    my_function(6, 0)
except Exception:
    print('In except')
else:
    print('Everything worked OK')
finally:
    print('Always runs')
```

---

## Getting a Traceback
- The `traceback` module is used to print stack traces.
- Useful when you need to print stack traces under program control.

### Example:
```python
import traceback

try:
    print(6 / 0)
except Exception as exp:
    print('oops')
    print(exp)
    traceback.print_exc()
```
- Output:
  - `oops`
  - `division by zero`
  - `Traceback (most recent call last): ... ZeroDivisionError: division by zero`

---

## Nesting Exception Blocks
- Can nest `try-except` blocks.
- The innermost `try-except` blocks are tried first. If not handled, it propagates outwards.

---

## Raising An Exception
- An error or exception is raised using the keyword `raise`.
- The syntax is:
  ```python
  raise <Exception/Error type to raise>()
  ```

### Example:
```python
def function_bang():
    print('function_bang in')
    raise ValueError('Bang!')
    print('function_bang out')

try:
    function_bang()
except ValueError as ve:
    print(ve)
```
- Output:
  - `function_bang in`
  - `Bang!`

- Can also use shorthand form:
  ```python
  raise ValueError
  ```
- Can also re-raise the error/exception.

---

## Defining New Exceptions / Errors
- Create new exceptions by subclassing existing ones.
- Use `Exception` or a subclass of `Exception` (do not use `BaseException`).
- Creates a new `Exception` class, could have supplied more data via the `__init__` method if required.

### Example:
```python
class InvalidAgeException(Exception):
    """Valid Ages must be between 0 and 120"""

def set_age(self, value):
    print('In set_age method(', value, ')')
    if isinstance(value, int) & (value > 0 & value < 120):
        self._age = value
    else:
        raise InvalidAgeException()
```

- You should only create an exception when you need it because Stack Trace and Line Number information is added when the exception is created. Also, consider the performance overhead of exceptions.

---

## Questions?

?
