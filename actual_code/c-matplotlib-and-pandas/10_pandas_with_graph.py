import matplotlib.pyplot as plt
import pandas as pd

# Read the users.csv file

csv_filename = "users.csv"

df = pd.read_csv(csv_filename)



# Group the data by department and get the average salary

grouped_data = df.groupby("Department")["Salary"].mean()



# Plot the grouped data

plt.figure(figsize=(10, 6))

grouped_data.plot(kind="bar")



# Customize the plot

plt.title("Average Salary by Department")

plt.xlabel("Department")

plt.ylabel("Average Salary (£)")

plt.xticks(rotation=45)

plt.grid(axis="y", linestyle="--", alpha=0.7)



# Show the plot

plt.show()