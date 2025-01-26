# Plan for Session
- Obtaining a reference to a file
- File Access Modes
- Reading Files
- Writing Data to Files
- Using files and `with` statements
- Exception Handling
- Renaming and Deleting files
- Working with CSV Files

---

## Obtaining a Reference to a File
- `open()` function creates a file object that can be used to read and/or write data.
- Requires the name of the file you want to work with.
- Optionally, you can specify the access mode.

### Signature for `open` function:
```python
file_object = open(file_name, access_mode)
```
- `file_name` indicates the file to be accessed.
- `access_mode` determines the mode the file is opened in (e.g., read, write, append) in text (default) or binary modes.

---

## File Access Modes
| Mode | Description |
| --- | --- |
| `r`  | Opens a file for reading only (default). |
| `rb` | Opens a file for reading only in binary format. |
| `r+` | Opens a file for both reading and writing. Cursor at start of file. |
| `rb+`| Opens a file for both reading and writing in binary format. |
| `w`  | Opens a file for writing only. Overwrites the file if the file exists. |
| `wb` | Opens a file for writing only in binary format. Overwrites the file if the file exists. |
| `w+` | Opens a file for both writing and reading. Overwrites the existing file if the file exists. |
| `wb+`| Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. Cursor at end of file. |
| `a`  | Opens a file for appending. If the file does not exist, it creates a new file for writing. |
| `ab` | Opens a file for appending in binary format. |
| `a+` | Opens a file for both appending and reading. Cursor at end of file. |
| `ab+`| Opens a file for both appending and reading in binary format. |

---

## Reading Files
- Can read info from a file object via `read()`, `readline()`, and `readlines()` methods.
  - `read()`: returns the entire contents of the file as a single string.
  - `readline()`: returns the next line from a file.
  - `readlines()`: returns a list of all the lines in a file.
- Don’t forget to close the file object.
- Once a line is read, it won’t be read again.

### Example:
```python
# Read multiple lines of data
file = open('myfile.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line, end='')

file.close()

# Read one line of data
file = open('myfile.txt', 'r')
line_of_data = file.readline()
print(line_of_data, end='')

file.close()
```

---

## File Contents Iteration
- Often want to process the contents of a file a line at a time.
- File objects support iteration.

### Example:
```python
file = open('myfile.txt', 'r')
for line in file:
    print(line, end='')

file.close()
```

---

## Using Files and `with` Statement
- File type implements the Context Manager Protocol.
- Can use it in a `with` statement.
  - Entry behavior opens the file.
  - Exit behavior closes the file.
- Best practice/Pythonic way to open and close files.

### Example:
```python
with open('myfile.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')
```

---

## File Access Can Raise Errors
- Try accessing a file that does not exist!
- Can wrap in a `try` block.

### Example:
```python
try:
    with open('myfile2.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')
except FileNotFoundError as err:
    print('oops')
    print(err)
```
- Output:
  - `oops`
  - `[Errno 2] No such file or directory: 'myfile2.txt'`

---

## Writing Data to Files
- Use the file object’s `write()` method assuming the file was opened in write mode.
- `write` method does not add a newline character (`\n`) to the end of the line.
- Don’t forget to close the file.

### Example:
```python
print('Writing file')

try:
    with open('data.txt', 'w') as file:
        file.write('Hello My World\n')
        file.write('Working with files is easy\n')
        file.write('It is cool ...\n')
        file.write(f'{58}\n')
except Exception as exp:
    print(exp)
```

---

## Renaming and Deleting Files
- A file can be renamed using the `os.rename()` function.
  - The function takes 2 arguments: current filename and new filename.
  - Part of the Python `os` module, which provides methods that can be used to perform a range of file-processing operations.

### Example:
```python
import os

os.rename('myfileoriginalname.txt', 'myfilenewname.txt')
```

- Delete a file using `os.remove()` function.

### Example:
```python
import os

os.remove('somefilename.txt')
```

---

## Working with CSV Files
- Comma Separated Values (CSV) format is widely used for data import and export but has no well-defined standard.
- Supported by the built-in `csv` module.
  - Can read and write CSV files.
  - Supports formats used by Excel.
  - Can also support other dialects or special-purpose user-defined formats.
- Key objects are `csv.reader` and `csv.writer`.
  - For more information, see [Python CSV Documentation](https://docs.python.org/3/library/csv.html).

### Example: Writing out a CSV file
```python
import csv

try:
    print('Creating CSV file')
    with open('sample.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['She Loves You', 'Sept 1963'])
        writer.writerow(['I Want to Hold Your Hand', 'Dec 1963'])
        writer.writerow(['Can’t Buy Me Love', 'Apr 1964'])
        writer.writerow(['A Hard Day’s Night', 'July 1964'])
except Exception as exp:
    print(exp)
```

### Example: Reading from a CSV file
```python
import csv

print('Starting to read csv file')

try:
    with open('sample.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(f'{row[0]} {row[1]}')
except Exception as exp:
    print(exp)

print('Done Reading')
```
- `row` is a list.

---

## Questions?

?
