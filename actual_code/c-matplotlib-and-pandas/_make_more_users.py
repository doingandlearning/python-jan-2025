import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define the number of new rows to add
num_rows = 50

# Define possible departments
departments = ["HR", "IT", "Finance", "Marketing", "Sales"]

# Generate random user data
new_data = []
for _ in range(num_rows):
    new_data.append({
        "Name": fake.name(),
        "Age": random.randint(20, 60),
        "City": fake.city(),
        "Salary": random.randint(40000, 120000),
        "Department": random.choice(departments)
    })

# Convert to DataFrame
df_new = pd.DataFrame(new_data)

# Read the existing CSV file
csv_filename = "users.csv"
df_existing = pd.read_csv(csv_filename)

# Append new data
df_combined = pd.concat([df_existing, df_new], ignore_index=True)

# Save back to CSV
df_combined.to_csv(csv_filename, index=False)

print(f"Added {num_rows} new rows to '{csv_filename}' successfully!")
