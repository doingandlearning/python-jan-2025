# Lab: Errors and Exceptions

In this lab, we’ll explore how to handle errors in Python using `try-except` blocks, and define a custom exception for specific error conditions.

## Objectives

1. Observe how Python behaves with unhandled errors.
2. Use a `try-except` block to handle errors gracefully.
3. Define a custom exception and raise it in specific cases.

---

## Task 1: Run and Handle a Simple Error

In this task, you’ll observe how Python reacts to an unhandled error. Then, you’ll modify the code to handle the error with a `try-except` block.

### Step 1: Run Code That Fails

Write and run the following code, which tries to divide a number by zero (an illegal operation):

```python
# Division by zero - this will cause an error
result = 10 / 0
print("Result:", result)
```

### Step 2: Observe the Error

When you run this code, you should see an error similar to:

```
ZeroDivisionError: division by zero
```

### Step 3: Wrap in a `try-except` Block

Now, modify the code to handle this error:

```python
try:
    result = 10 / 0
    print("Result:", result)
except ZeroDivisionError as e:
    print("Caught an error:", e)
```

### Step 4: Observe the Difference

With the `try-except` block, the program should catch the error and print a friendly message instead of crashing.

**Expected Output**:

```
Caught an error: division by zero
```

---

## Task 2: Create and Use a Custom Exception

Now that you understand how `try-except` works, you’ll create a custom exception and use it in a function to validate input values.

### Step 1: Define a Custom Exception

Define a new exception class called `InvalidInputError`:

```python
class InvalidInputError(Exception):
    """Raised when an invalid input is provided."""
    
    def __init__(self, value, message="Invalid input provided"):
        self.value = value
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message}: {self.value}"
```

### Step 2: Implement `try-except` and Raise the Custom Exception

1. Write a function, `process_input(value)`, that processes an input value.
2. Check if the value is a positive integer. If it’s not, raise `InvalidInputError` with the invalid value.
3. Wrap the function call in a `try-except` block to catch and handle the custom error.

```python
def process_input(value):
    if not isinstance(value, int) or value <= 0:
        raise InvalidInputError(value, "Input must be a positive integer")
    print(f"Processing value: {value}")

# Main program
try:
    process_input(-5)  # Test with an invalid value
except InvalidInputError as e:
    print(e)
```

### Step 3: Run the Code

Run the script. If the input is invalid, it should raise `InvalidInputError` and display a message indicating the problem.

**Expected Output**:

```
Input must be a positive integer: -5
```

