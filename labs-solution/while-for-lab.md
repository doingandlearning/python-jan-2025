### Task 1: Counting with `while` Loop

```python
counter = 1
while counter <= 10:
    print(counter)
    counter += 1
```

**Explanation**:
- The `counter` variable starts at 1.
- The `while` loop runs as long as `counter` is less than or equal to 10.
- Each loop iteration prints `counter` and then increments it by 1.

---

### Task 2: Sum of Numbers with `for` Loop

```python
total_sum = 0
for num in range(1, 101):
    total_sum += num
print(f"Sum of numbers from 1 to 100 is: {total_sum}")
```

**Explanation**:
- `total_sum` is initialized to 0 to accumulate the sum.
- The `for` loop iterates over each number from 1 to 100 (inclusive).
- Each number is added to `total_sum`, and the final sum is printed at the end.

---

### Task 3: Multiplication Table

```python
number = int(input("Enter a number for the multiplication table: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
```

**Explanation**:
- The user inputs a number to generate its multiplication table.
- The `for` loop iterates from 1 to 10.
- In each iteration, it multiplies the user-provided number by `i` and prints the result.

---

### Task 4: Guess the Secret Number (Using `while`)

```python
secret_number = 7

while True:
    guess = int(input("Guess the secret number: "))
    if guess == secret_number:
        print("Congratulations! You guessed it!")
        break  # Exit the loop when the correct number is guessed
    else:
        print("Wrong, try again.")
```

**Explanation**:
- The `while` loop runs indefinitely until the user guesses the secret number.
- If the guess matches `secret_number`, a success message is printed, and `break` is used to exit the loop.
- If the guess is incorrect, the user is prompted to try again.
