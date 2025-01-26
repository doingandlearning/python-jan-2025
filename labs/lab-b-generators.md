# Lab: Generators (Optional)

## Objective

Write a prime number generator.

A Prime Number is a positive whole number greater than 1 that has no other divisors except the number 1 and the number itself. That is, it can only be divided by itself and the number 1. For example, the numbers 2, 3, 5, and 7 are prime numbers as they cannot be divided by any other whole number. However, the numbers 4 and 6 are not because they can both be divided by the number 2. In addition, the number 6 can also be divided by the number 3.

## Task

You should write a program to calculate prime numbers starting from 1 up to the value input by the user.

If the user inputs a number below 2, print an error message.

### Pseudo Code

In pseudo code, you might write:

```pseudo
for I in range 2 to number
   for j in range 2 to i
       if I % j has a remainder then it's not a prime number
            break out of loop
        if it was a prime number 
              yield i
```

### Implementation

The generator should take a limit to give the maximum size of the loop you use to generate the prime numbers. You could call this function `prime_number_generator()`.

You should be able to run the following code:

```python
number = input('Please input the number:')
if number.isnumeric():
    num = int(number)
    if num <= 2:
        print('Number must be greater than 2')
    else:
        for prime in prime_number_generator(num):
            print(prime, end=' ')
else:
    print('Must be a positive integer')
```

### Example Output

If the user enters 27, then the output would be:

```
Please input the number: 27
2 3 5 7 11 13 17 19 23
```
