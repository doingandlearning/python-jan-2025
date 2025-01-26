### Lab: Practicing Loops in Python

#### Objective
Learn to use `for` and `while` loops to perform repetitive tasks and control program flow.

---

### Task 1: Counting with `while` Loop

Write a `while` loop that counts from 1 to 10 and prints each number.

**Steps**:
1. Initialize a variable `counter` to 1.
2. Use a `while` loop to keep printing `counter` while it’s less than or equal to 10.
3. Increment `counter` by 1 each time.

**Example Output**:
```
1
2
3
...
10
```

---

### Task 2: Sum of Numbers with `for` Loop

Write a `for` loop that calculates the sum of numbers from 1 to 100.

**Steps**:
1. Initialize a variable `total_sum` to 0.
2. Use a `for` loop to iterate over the range from 1 to 100.
3. Add each number to `total_sum`.
4. Print `total_sum` at the end.

**Example Output**:
```
Sum of numbers from 1 to 100 is: 5050
```

---

### Task 3: Multiplication Table

Write a `for` loop to print the multiplication table for a number provided by the user.

**Steps**:
1. Ask the user for a number.
2. Use a `for` loop to print the product of the user's number with numbers 1 through 10.

**Example Output (if user inputs 5)**:
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

---

### Task 4: Guess the Secret Number (Using `while`)

Create a simple game where the user must guess a secret number.

**Steps**:
1. Set a secret number (e.g., `secret_number = 7`).
2. Use a `while` loop to keep asking the user for a guess until they get it right.
3. If the user guesses correctly, print “Congratulations! You guessed it!” and exit the loop.
4. If they guess incorrectly, prompt them to try again.

**Example Output**:
```
Guess the secret number: 3
Wrong, try again.
Guess the secret number: 7
Congratulations! You guessed it!
```
