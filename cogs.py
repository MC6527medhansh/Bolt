import pandas as pd
import numpy as np

# Load the expenses data
df = pd.read_csv('datasets/expenses.csv')

# Filter for expense transactions only
expenses = df[df['Transaction_Type'] == 'Expense']

# Calculate total for each expense category
expenses['Absolute_Amount'] = expenses['Amount'].abs()  # Convert negative amounts to positive
expense_by_category = expenses.groupby('Category')['Absolute_Amount'].sum().reset_index()

# Print the expense categories and their totals
print("Expense Categories:")
print(expense_by_category)

# Define which categories are part of COGS for this service business
cogs_categories = ['Ambulance Call', 'Staff Salary']

# Calculate COGS
cogs_expenses = expense_by_category[expense_by_category['Category'].isin(cogs_categories)]
total_cogs = cogs_expenses['Absolute_Amount'].sum()

# Calculate total revenue
revenues = df[df['Transaction_Type'] == 'Revenue']
total_revenue = revenues['Amount'].sum()

# Calculate COGS as percentage of revenue
cogs_percentage = (total_cogs / total_revenue) * 100

cogs_percentag_per_net_rev = (total_cogs / -2773853) * 100

# Calculate each COGS component as percentage of total COGS
cogs_expenses['Percentage_of_COGS'] = (cogs_expenses['Absolute_Amount'] / total_cogs) * 100

# Calculate each COGS component as percentage of revenue
cogs_expenses['Percentage_of_Revenue'] = (cogs_expenses['Absolute_Amount'] / total_revenue) * 100

# Print results
print("\nCOGS Analysis:")
print(f"Total COGS: ${total_cogs:,.2f}")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"COGS as percentage of revenue: {cogs_percentage:.1f}%")
print(f"COGS as percentage of net rev: {cogs_percentag_per_net_rev:.1f}%")

print("\nCOGS Component Breakdown:")
print(cogs_expenses[['Category', 'Absolute_Amount', 'Percentage_of_COGS', 'Percentage_of_Revenue']].to_string(index=False))

# Calculate gross profit and margin
gross_profit = total_revenue - total_cogs
gross_profit_margin = (gross_profit / total_revenue) * 100

print("\nProfitability Analysis:")
print(f"Gross Profit: ${gross_profit:,.2f}")
print(f"Gross Profit Margin: {gross_profit_margin:.2f}%")
