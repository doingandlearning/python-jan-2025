# Lab: Fetch, Parse, and Save Data from an API

In this lab, you'll use the `requests` library to retrieve data from a public API, parse the data, and save it as a JSON file. This lab will help reinforce your skills in working with APIs, JSON, and file handling.

---

## Objectives

1. Use `requests` to fetch data from an API.
2. Parse the JSON response and extract specific information.
3. Write the parsed data to a JSON file.

---

### Setup

Ensure you have the `requests` library installed. You can install it via pip if needed:

```bash
pip install requests
```

---

## Step 1: Fetch Data from an API

We'll use the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/) for this lab, which provides placeholder data for testing. Let's fetch a list of posts.

### Task

1. Import the `requests` module.
2. Use `requests.get()` to fetch data from the endpoint: `https://jsonplaceholder.typicode.com/posts`.
3. Check the response status and print an error if the request fails.
4. Print the JSON data to understand the structure.

### Example Code

```python
import requests

# Define the API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Fetch data from the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON data
    print("Data fetched successfully.")
else:
    print(f"Failed to fetch data: {response.status_code}")
    data = []  # Set data to an empty list if request failed
```

### Expected Output

You should see "Data fetched successfully." if the request was successful. To see the structure of the data, print the first item:

```python
print(data[0])  # Print the first post to examine its structure
```

---

## Step 2: Parse the Data

Now that we have the data, let's parse it and select only specific fields to save. For each post, we'll keep:

- `userId`
- `id`
- `title`
- `body`

### Task

1. Use a list comprehension to create a list of dictionaries.
2. Each dictionary should contain only the `userId`, `id`, `title`, and `body` fields.

### Example Code

```python
# Parse and filter data
filtered_data = [
    {
        "userId": post["userId"],
        "id": post["id"],
        "title": post["title"],
        "body": post["body"]
    }
    for post in data
]

# Print a sample of the filtered data
print(filtered_data[0])  # Print the first post to check the structure
```

---

## Step 3: Write the Data to a JSON File

With the parsed data ready, we’ll now save it to a JSON file on the local file system.

### Task

1. Import the `json` module.
2. Write `filtered_data` to a file named `posts.json`.
3. Use `indent=4` for pretty formatting in the JSON file.

### Example Code

```python
import json

# Write the filtered data to a JSON file
with open("posts.json", "w") as file:
    json.dump(filtered_data, file, indent=4)

print("Data saved to posts.json")
```

---

## Step 4: Verify the Output

1. Open the `posts.json` file in a text editor to confirm that the data is correctly formatted.
2. You should see JSON data with the fields `userId`, `id`, `title`, and `body` for each post.

---

## Full Example Code

Here's the complete code for the lab:

```python
import requests
import json

# Step 1: Fetch Data from the API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON data
    print("Data fetched successfully.")
else:
    print(f"Failed to fetch data: {response.status_code}")
    data = []

# Step 2: Parse and Filter Data
filtered_data = [
    {
        "userId": post["userId"],
        "id": post["id"],
        "title": post["title"],
        "body": post["body"]
    }
    for post in data
]

# Step 3: Write the Data to a JSON File
with open("posts.json", "w") as file:
    json.dump(filtered_data, file, indent=4)

print("Data saved to posts.json")
```

---

## Summary

In this lab, you:

1. Fetched data from an API using `requests`.
2. Parsed and filtered specific fields from the JSON response.
3. Wrote the filtered data to a local JSON file.

This workflow is common when working with APIs and allows you to retrieve, process, and store data effectively. You can try modifying the API endpoint to explore other data (e.g., `https://jsonplaceholder.typicode.com/users`) or further manipulate the data before saving it.

---

# Extensions

### Extension 1: Error Handling for Robustness

1. **Handle Connection Errors**: Wrap the API request in a `try-except` block to handle network issues gracefully.
   ```python
   try:
       response = requests.get(url)
       response.raise_for_status()  # Raises an HTTPError for bad responses
   except requests.exceptions.RequestException as e:
       print(f"Error fetching data: {e}")
       data = []  # Set data to an empty list if request fails
   ```

2. **Handle JSON Parsing Errors**: Use a `try-except` block when parsing JSON data to manage cases where the response might not be valid JSON.
   ```python
   try:
       data = response.json()
   except json.JSONDecodeError:
       print("Error decoding JSON data.")
       data = []
   ```

### Extension 2: Fetch and Save Data in CSV Format

Save the data as a CSV file instead of JSON, which can be useful for spreadsheet applications.

1. Import the `csv` module.
2. Define headers and write each post as a row.

```python
import csv

# Define the headers
headers = ["userId", "id", "title", "body"]

# Write to CSV file
with open("posts.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(filtered_data)

print("Data saved to posts.csv")
```

### Extension 3: Fetch Additional Data and Combine It

Fetch data from a second endpoint (e.g., `https://jsonplaceholder.typicode.com/users`) and combine it with the post data. For example, you could add the user’s name to each post.

1. Fetch user data.
2. Create a dictionary mapping `userId` to `username`.
3. Add the username to each post before saving.

```python
# Fetch user data
user_response = requests.get("https://jsonplaceholder.typicode.com/users")
user_data = user_response.json()

# Map userId to username
user_map = {user["id"]: user["username"] for user in user_data}

# Add username to each post
for post in filtered_data:
    post["username"] = user_map.get(post["userId"], "Unknown")
```

### Extension 4: Schedule Data Fetching with `time.sleep`

To simulate periodic fetching, use `time.sleep` to request data every few seconds or minutes.

```python
import time

while True:
    # Your data fetching code here
    print("Fetching data...")
    # Process and save data
    time.sleep(300)  # Wait 5 minutes before fetching again
```

### Extension 5: Create a JSON Backup

Before each new data fetch, create a backup of the existing `posts.json` file by renaming it with a timestamp. This allows you to keep older data while fetching fresh data.

```python
import os
import shutil
from datetime import datetime

# Create a timestamped backup if posts.json exists
if os.path.exists("posts.json"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    shutil.copy("posts.json", f"posts_backup_{timestamp}.json")
    print(f"Backup created: posts_backup_{timestamp}.json")
```



