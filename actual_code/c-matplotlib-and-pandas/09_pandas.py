import pandas as pd

df = pd.read_csv("users.csv")

# print(df.head())
# print(df.tail())
# print(df.describe())

# print(df[["Name", "Age"]])
# print(df[df["Age"] > 30])
# print(df.head())
# df["Age"] = df["Age"] + 1
# print(df.head())

# print(df["Age"].quantile(0.9))
# print(df.groupby("Age")["Salary"].mean())