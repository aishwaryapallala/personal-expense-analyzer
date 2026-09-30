
import pandas as pd

# Read the CSV file
df = pd.read_csv("data/expenses.csv")

# Display the first five rows
print(df.head()) #default first 5 
print(df.head(10)) # to print all rows
print(df["Amount"])
print(df["Amount"].sum())
