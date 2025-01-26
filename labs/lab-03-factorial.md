
# Lab 3: Factorial

The aim of this lab is to allow you to use both flow of control and iteration structures in Python. To do this, we will be writing a short program to calculate the factorial of a number.

## Calculating the Factorial of a Number

You should write a program that can find the factorial of any given number.

For example, find the factorial of the number 5 (often written as 5!), which is `1 * 2 * 3 * 4 * 5` and equals 120.

The factorial is not defined for negative numbers, and the factorial of zero is 1; that is, `0! = 1`.

This lab is comprised of 7 steps:
1. Create a file
2. Add initial code
3. Validate that the user entered a non-negative integer value
4. Convert the input string to an integer
5. Add logic to perform calculations
6. Add factorial calculation
7. Run the final code

## Step 1: Create a New File

Create a new file for your factorial calculation. You can do this using `File -> New File` in your editor and name the file `factorial.py`. The `.py` extension will be added automatically.

## Step 2: Add Initial Code

Your program should ask the user to enter the number for which the factorial will be calculated. For example:

```python
print('Starting factorial calculation program')
number = input('Please input the number: ')
print(f'The number to calculate factorial for is {number}')
```

Save the file with the updated contents and then run it as you did in the earlier labs. For example, use the terminal to run the file:

```bash
python factorial.py
```

The output should be:

```
Starting factorial calculation program
Please input the number: 5
The number to calculate factorial for is 5
```

## Step 3: Validate that the User Entered a Non-Negative Integer Value

This can be done using the `isnumeric()` method available on all strings. If the user has not entered a number, notify them of this. For example:

```python
if number.isnumeric():
    print(f'The number to calculate factorial for is {number}')
else:
    print('Not an integer number')
```

Try this out and see what happens if you enter the letter "H". The output might look like:

```
Starting factorial calculation program
Please input the number: H
Not an integer number
```

## Step 4: Convert the Input String to an Integer

As you may recall, the `input()` function always returns a string. We must therefore convert it to an integer so that we can perform the factorial calculation on it.

To do this, use the `int()` function inside the `if` statement when the number is numeric. For example:

```python
if number.isnumeric():
    print(f'The number to calculate factorial for is {number}')
    num = int(number)
else:
    print('Not an integer number')
```

## Step 5: Add Logic to Perform Calculations

You should now determine:
- If the number is zero – if it is, then the answer is 1 – print this out.
- Otherwise, use a loop to generate the result and print it out.

The conditional aspect of the above program can be handled using an `if` statement (ideally with `elif` elements).

For example:

```python
if num == 0:  # Termination criteria
    print('0! factorial is 1')
else:
    # Write your code here
```

The current state of the program is now:

```python
print('Starting factorial calculation program')
number = input('Please input the number: ')
if number.isnumeric():
    print(f'The number to calculate factorial for is {number}')
    num = int(number)
    if num == 0:  # Termination criteria
        print('0! factorial is 1')
    else:
        # Loop element – write your code here
else:
    print('Not an integer number')
```

You should try to run this version to check that it does not contain any errors. You could try changing the value input to `number` to be -1 and 0 to check that each of the log statements associated with these conditions works correctly.

## Step 6: Add Factorial Calculation

Inside the last `else` block of code, you should now replace the `# write your code here` comment with a `for` loop.

The `for` loop will need to loop an appropriate number of times. For example:

```python
# Loop element
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print(f'{number}! factorial is {factorial}')
```

The final program is shown below:

```python
print('Starting factorial calculation program')
number = input('Please input the number: ')
if number.isnumeric():
    print(f'The number to calculate factorial for is {number}')
    num = int(number)
    if num == 0:  # Termination criteria
        print('0! factorial is 1')
    else:
        # Loop element
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
        print(f'{number}! factorial is {factorial}')
else:
    print('Not an integer number')
```

## Step 7: Run the Final Code

The output from the sample solution is:

```
Starting factorial calculation program
Please input the number: 5
The number to calculate factorial for is 5
5! factorial is 120
```
