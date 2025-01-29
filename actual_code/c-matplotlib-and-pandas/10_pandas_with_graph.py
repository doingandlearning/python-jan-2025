import matplotlib.pyplot as plt
import pandas as pd

# Read the users.csv file

csv_filename = "users.csv"

df = pd.read_csv(csv_filename)

# import io
# import pandas as pd
# import msoffcrypto
#
# passwd = 'xyz'
#
# decrypted_workbook = io.BytesIO()
# with open(path_to_your_file, 'rb') as file:
#     office_file = msoffcrypto.OfficeFile(file)
#     office_file.load_key(password=passwd)
#     office_file.decrypt(decrypted_workbook)
#
# df = pd.read_excel(decrypted_workbook, sheet_name='abc')





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