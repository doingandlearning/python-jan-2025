# **Case Study: Converting JSON Data to CSV**  

## **Scenario**  

You work for a team that receives **JSON data** from various sources. A client has provided a JSON file containing user data, and they need it converted into a structured CSV format for easier analysis in spreadsheet tools.  

Your job is to:  
✅ Read the JSON data from a file  
✅ Extract relevant fields  
✅ Convert the JSON data into a well-formatted CSV file  
✅ Append new data to both JSON and CSV files  

---

## **📌 Step 1: Understanding the JSON Data**  

The client has provided a file named **`users.json`**, which contains the following data:  

```json
[
    {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30, "city": "London"},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 25, "city": "New York"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "age": 35, "city": "Paris"}
]
```

The client wants a **CSV file** containing only **name, email, and city**.

---

## **📌 Step 2: Read the JSON File**  

Your first task is to **load the JSON data into Python**.

```python
import json

# Read the JSON file
json_filename = "users.json"

with open(json_filename, "r") as file:
    users = json.load(file)

# Print data for verification
print("Loaded JSON Data:", users)
```

✔️ **Check:** The data should now be stored in a Python list of dictionaries.

---

## **📌 Step 3: Convert JSON to CSV**  

Now, extract **name, email, and city** and save it as a CSV file named **`users.csv`**.

```python
import csv

csv_filename = "users.csv"

# Open CSV file for writing
with open(csv_filename, "w", newline="") as file:
    fieldnames = ["name", "email", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Write column headers

    # Write only the required fields
    for user in users:
        writer.writerow({
            "name": user["name"],
            "email": user["email"],
            "city": user["city"]
        })

print(f"CSV file '{csv_filename}' created successfully!")
```

✔️ **Check:** Open `users.csv` to verify the output. It should look like:

```
name,email,city
Alice,alice@example.com,London
Bob,bob@example.com,New York
Charlie,charlie@example.com,Paris
```

---

## **📌 Step 4: Append a New User to JSON and CSV**  

The client has provided a **new user** to be added to both `users.json` and `users.csv`:

```json
{"id": 4, "name": "David", "email": "david@example.com", "age": 40, "city": "Berlin"}
```

### **4.1 Append New Data to JSON File**  

```python
# New user data
new_user = {"id": 4, "name": "David", "email": "david@example.com", "age": 40, "city": "Berlin"}

# Read existing JSON data
with open(json_filename, "r") as file:
    existing_users = json.load(file)

# Append new user
existing_users.append(new_user)

# Write back to JSON
with open(json_filename, "w") as file:
    json.dump(existing_users, file, indent=4)

print("New user added to JSON file.")
```

✔️ **Check:** Open `users.json` to verify the new entry.

---

### **4.2 Append New Data to CSV File**  

```python
# Append new user to CSV
with open(csv_filename, "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "email", "city"])
    writer.writerow({
        "name": new_user["name"],
        "email": new_user["email"],
        "city": new_user["city"]
    })

print("New user added to CSV file.")
```

✔️ **Check:** Open `users.csv`, and it should now include:

```
name,email,city
Alice,alice@example.com,London
Bob,bob@example.com,New York
Charlie,charlie@example.com,Paris
David,david@example.com,Berlin
```

---

## **📌 Step 5: Bonus - Read CSV Back into JSON Format**
If the client later asks for the **CSV data back in JSON format**, we can **convert it back**.

```python
# Read CSV and convert back to JSON
csv_data = []

with open(csv_filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        csv_data.append(row)

# Save back to a new JSON file
with open("converted.json", "w") as file:
    json.dump(csv_data, file, indent=4)

print("CSV converted back to JSON!")
```

---

## **✅ Summary**
| **Task**                 | **Method Used** |
|--------------------------|----------------|
| Read JSON file           | `json.load()` |
| Write JSON file          | `json.dump()` |
| Read CSV file            | `csv.DictReader()` |
| Write CSV file           | `csv.DictWriter()` |
| Append to JSON file      | `json.load() → modify → json.dump()` |
| Append to CSV file       | `csv.DictWriter(file, mode="a")` |

---

## **📌 Challenges**
1️⃣ Modify the script to include the **age** field in the CSV file.  
2️⃣ Remove all users under 30 before writing the CSV file.  
3️⃣ Convert **CSV data back to JSON** but format it as a dictionary with `email` as the key.  
4️⃣ Implement error handling:  
   - Prevent **duplicate users** when appending.  
   - Handle missing fields gracefully.  

-