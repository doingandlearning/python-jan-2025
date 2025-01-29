# **Lab: Working with Files, CSV, and JSON in Python**
**Objective:**  
By the end of this lab, you'll be able to:
1. Read, write, and append to text files.
2. Read and write CSV files using `csv.reader` and `csv.DictReader`.
3. Read, write, and append to JSON files.

---

## **📌 Part 1: Reading, Writing, and Appending to Text Files**
### **Task 1: Write to a text file**
- Create a file named `notes.txt` and write three lines of text.

```python
filename = "notes.txt"

# Writing to a text file
with open(filename, "w") as file:
    file.write("This is the first line.\n")
    file.write("Python is great for file handling.\n")
    file.write("Let's learn how to work with files!\n")

print(f"{filename} created successfully!")
```

### **Task 2: Read from the text file**
- Open `notes.txt` and print its contents.

```python
# Reading from a text file
with open(filename, "r") as file:
    content = file.read()

print("File Contents:\n", content)
```

### **Task 3: Append to the text file**
- Add two more lines to `notes.txt`.

```python
# Appending to a text file
with open(filename, "a") as file:
    file.write("Appending a new line.\n")
    file.write("File handling in Python is easy!\n")

print("Lines appended successfully!")
```

---

## **📌 Part 2: Working with CSV Files**
### **Task 4: Writing CSV using `csv.writer`**
- Create a file named `data.csv` with columns: `name, age, city`.

```python
import csv

csv_filename = "data.csv"

# Data to write
data = [
    ["Alice", 30, "London"],
    ["Bob", 25, "New York"],
    ["Charlie", 35, "Paris"]
]

# Writing to a CSV file using csv.writer
with open(csv_filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city"])  # Header row
    writer.writerows(data)  # Writing multiple rows

print(f"{csv_filename} created successfully!")
```

### **Task 5: Reading CSV using `csv.reader`**
- Open `data.csv` and read the contents.

```python
# Reading CSV using csv.reader
with open(csv_filename, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### **Task 6: Writing CSV using `csv.DictWriter`**
- Create a file named `data_dict.csv` using `csv.DictWriter`.

```python
dict_csv_filename = "data_dict.csv"

data_dict = [
    {"name": "Alice", "age": 30, "city": "London"},
    {"name": "Bob", "age": 25, "city": "New York"},
    {"name": "Charlie", "age": 35, "city": "Paris"}
]

# Writing to CSV using DictWriter
with open(dict_csv_filename, "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_dict)

print(f"{dict_csv_filename} created successfully!")
```

### **Task 7: Reading CSV using `csv.DictReader`**
- Open `data_dict.csv` using `csv.DictReader`.

```python
# Reading CSV using DictReader
with open(dict_csv_filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

---

## **📌 Part 3: Working with JSON Files**
### **Task 8: Writing JSON Data**
- Create a JSON file `data.json` containing the same information as `data_dict.csv`.

```python
import json

json_filename = "data.json"

# Writing to JSON
with open(json_filename, "w") as file:
    json.dump(data_dict, file, indent=4)

print(f"{json_filename} created successfully!")
```

### **Task 9: Reading JSON Data**
- Read `data.json` and print its contents.

```python
# Reading JSON
with open(json_filename, "r") as file:
    json_data = json.load(file)

print("JSON Data:", json_data)
```

### **Task 10: Appending Data to JSON**
- Append a new record to `data.json`.

```python
# New data to append
new_person = {"name": "David", "age": 40, "city": "Berlin"}

# Read existing data
with open(json_filename, "r") as file:
    existing_data = json.load(file)

# Modify data
existing_data.append(new_person)

# Write back updated JSON
with open(json_filename, "w") as file:
    json.dump(existing_data, file, indent=4)

print("New data appended to JSON!")
```

---

## **🛠 Challenges**
🔹 Modify `notes.txt` to remove all lines that contain "Python".  
🔹 Modify `data.csv` to replace all occurrences of `"Bob"` with `"Robert"`.  
🔹 Convert `data.json` to a dictionary where names are keys and store the records inside.

