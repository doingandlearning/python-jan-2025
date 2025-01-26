# Lab 4: Containers

The aim of this lab is to provide some experience working with the List container type in Python. This lab will provide the basis of many of the remaining labs in the course.

The goal of this module is to allow a user to enter a set of floating-point numbers which will be stored in a Python list. We will then use some of the list functions to sort the data, reverse the order of the data, make a copy of the data, remove data from it, etc.

This lab is made up of 4 steps:
1. Create a new file
2. Obtain the data
3. Print out the length of the list
4. Using list operations

## Step 1: Create a New File

For this lab, you should create a new Python file using `File > New`. From the New dialog, select the Python File option.

You can name the file anything that seems acceptable such as `app.py` or `analysis.py`. Alternatively, you could rename the existing `main.py` to `hello.py` and create a new file `main.py`.

## Step 2: Obtain the Data

For this example, we will store the temperature readings entered by the user into a list held in a variable called `readings`. For example:

```python
readings = []
```

The `while` loop used to enter the data should allow a user to enter one value at a time. The value `-1` will be used to terminate the data input.

To handle this, you could use a flag to indicate whether the user has finished entering their data. A flag is a Boolean value that will be set appropriately when they have finished entering the data.

For example:

```python
continue_to_enter_data = True
while continue_to_enter_data:
    input_string = input('Please enter a temperature reading (-1 to end): ')
    if input_string == '-1':
        continue_to_enter_data = False
    elif input_string.count('.') > 1 or not input_string.replace('.', '').isdigit():
        print('Must be a positive floating point number')
    else:
        reading = float(input_string)
        readings.append(reading)
```

### Extension Point

You could also check that the data entered is (probably) a valid floating-point number. This is a little harder in Python than might be expected. The simplest approach is to remove the dot (`.`) from the number and then check that it now only contains digits. Note we will also assume that there is only one ‘.’ allowed in a number (hence 2 and 2.3 are valid, but 2.3.2 is not). We will also limit the example to only handling positive numbers.

An example of the sort of output produced by the program is given below:

```
Please enter a temperature reading (-1 to end): 0.0
Please enter a temperature reading (-1 to end): 2.3
Please enter a temperature reading (-1 to end): 3.4
Please enter a temperature reading (-1 to end): -1.0
Must be a positive floating point number
Please enter a temperature reading (-1 to end): 3.2.2
Must be a positive floating point number
Please enter a temperature reading (-1 to end): 4.1
Please enter a temperature reading (-1 to end): 2.3
Please enter a temperature reading (-1 to end): -1
Temperature readings input: [0.0, 2.3, 3.4, 4.1, 2.3]
```

Some useful functions include:

- `input_string.count('.')` checks to see how many times a string is contained in another string.
- `input_string.replace('.', '')` replaces one substring with another substring.
- `'32'.isnumeric()` checks to see if a string only contains numbers.
- `float('3.2')` converts a string into a floating-point number if possible.

## Step 3: Print Out the Length of the List

The `len()` function is a widely used function that can obtain the length of a wide range of data types (including strings, sets, dictionaries, and lists). Use the `len()` function to print out the length of your list. For example:

```python
print(f'There are {len(readings)} readings in total')
```

## Step 4: Using List Operations

Once you have written the code to obtain the data from the user, you should try out some of the list operations. For example:

### Sorting the List

You can sort the list using the natural ordering of the values held in the list:

```python
readings.sort()
print(f'Temperature readings sorted: {readings}')
```

### Reversing the List

You can also reverse the values in a list:

```python
readings.reverse()
print(f'Temperature readings in reverse: {readings}')
```

### Counting Occurrences

You can find out how many times a value appears in a list:

```python
print(f'There are {readings.count(0.0)} zero readings')
```

In the above, we are checking to see how many times the value `0.0` appears in the `readings` list.

### Copying a List

We can also make a copy of a list and store that into another variable:

```python
readings_copy = readings.copy()
print(f'Copy of temperature readings: {readings_copy}')
```

### Appending to the List

You can add values to a list:

```python
readings_copy.append(5.5)
```

This will only affect the copy of the temperature list; it will have no effect on the original list. You can confirm this by printing both out:

```python
print(f'Temperature readings: {readings}')
print(f'Copy of temperature readings: {readings_copy}')
```

### Removing from the List

You can also remove values from the list, for example, using the `pop()` function which will either remove a value at a specific location (if it is provided with a position index value) or from the end of the list if no value is given.

```python
print(f'Popping element from end of copy list {readings_copy.pop()}')
print(f'Readings copy now contains {readings_copy}')
```

## Reference

For reference, the complete listing is:

```python
readings = []
continue_to_enter_data = True
while continue_to_enter_data:
    input_string = input('Please enter a temperature reading (-1 to end): ')
    if input_string == '-1':
        continue_to_enter_data = False
    elif input_string.count('.') > 1 or not input_string.replace('.', '').isdigit():
        print('Must be a positive floating point number')
    else:
        reading = float(input_string)
        readings.append(reading)

print(f'Temperature readings input: {readings}')
print(f'There are {len(readings)} readings in total')

readings.sort()
print(f'Temperature readings sorted: {readings}')

readings.reverse()
print(f'Temperature readings in reverse: {readings}')

print(f'There are {readings.count(0.0)} zero readings')

readings_copy = readings.copy()
print(f'Copy of temperature readings: {readings_copy}')

readings_copy.append(5.5)
print(f'Temperature readings: {readings}')
print(f'Copy of temperature readings: {readings_copy}')

print(f'Popping element from end of copy list {readings_copy.pop()}')
print(f'Readings copy now contains {readings_copy}')
```