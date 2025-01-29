# **Case Study: Converting JSON Data to CSV**  

## **Scenario**  

You work for a team that receives **JSON data** from various sources. A client has provided a JSON file containing user data, and they need it converted into a structured CSV format for easier analysis in spreadsheet tools.  

Your job is to:  
✅ Read the JSON data from a file  
✅ Extract relevant fields  
✅ Convert the JSON data into a well-formatted CSV file  
✅ Append new data to both JSON and CSV files  
✅ Convert the CSV data back to JSON  

---

## **📌 Steps to Complete the Task**  

### **Step 1: Read the JSON File**  
- The client has provided a file named **`users.json`**, which contains a list of users with fields like `id`, `name`, `email`, `age`, and `city`.  
- Open the file and **load the data into a Python object**.  
- Hint: Use the `json` module and `json.load()` to read the file.  

### **Step 2: Convert JSON to CSV**  
- Extract only the **name, email, and city** fields from each user.  
- Write this structured data to a **CSV file** called `users.csv`.  
- Hint: Use the `csv.DictWriter` class and specify column names before writing.  

### **Step 3: Append a New User to JSON and CSV**  
- The client has provided **a new user** to be added to both `users.json` and `users.csv`.  
- First, **append the user to the JSON file**, ensuring the format stays valid.  
- Next, **append the same user to the CSV file**, keeping the structure consistent.  
- Hint:  
  - Read the JSON file into a list, append the new data, and write it back.  
  - Open the CSV file in **append mode** (`"a"`) and add the new user without overwriting the existing data.  

### **Step 4: Convert the CSV Back to JSON**  
- Suppose the client later asks for the **CSV data to be converted back into JSON format**.  
- Read the CSV file and store the data in a list of dictionaries.  
- Save this data as **`converted.json`**.  
- Hint: Use `csv.DictReader()` to read the CSV file and `json.dump()` to write it back as JSON.  

---

## **💻 Implementation: Writing the Code**  

### **Step 1: Read the JSON File**  

```python
import json

# Read the JSON file
json_filename = "users.json"

with open(json_filename, "r") as file:
    users = json.load(file)

# Print data for verification
print("Loaded JSON Data:", users)
```

---

### **Step 2: Convert JSON to CSV**  

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

---

### **Step 3: Append a New User to JSON and CSV**  

#### **3.1 Append New Data to JSON File**  

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

#### **3.2 Append New Data to CSV File**  

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

---

### **Step 4: Convert the CSV Back to JSON**  

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

---

