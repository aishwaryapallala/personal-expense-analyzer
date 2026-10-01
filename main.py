import pandas as pd

# Load expense data
df = pd.read_csv("data/expenses.csv")

print("===== EXPENSE ANALYZER =====")

# Display all expenses
print("\nAll Expenses:")
print(df)

# Total spending
total_expense = df["Amount"].sum()
print("\nTotal Expense: ₹", total_expense)

# Average spending
average_expense = df["Amount"].mean()
print("Average Expense: ₹", average_expense)

# Highest expense
highest_expense = df["Amount"].max()
print("Highest Expense: ₹", highest_expense)

# Lowest expense
lowest_expense = df["Amount"].min()
print("Lowest Expense: ₹", lowest_expense)

# Spending by category
category_expenses = df.groupby("Category")["Amount"].sum()
category_expenses = category_expenses.sort_values(ascending=False)

print("\nSpending by Category:")
print(category_expenses)

# Most expensive transaction
most_expensive = df.loc[df["Amount"].idxmax()]

print("\nMost Expensive Transaction:")
print(most_expensive)

# Expenses above 500Rs
large_expenses = df[df["Amount"] > 500]

print("\nExpenses Above ₹500:")
print(large_expenses)

#No of transactions
number_of_transactions = len(df)
print("Number of Transactions:", number_of_transactions)
