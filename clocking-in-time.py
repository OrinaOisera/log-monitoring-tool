import pandas as pd

# Read your Excel file
df = pd.read_excel("18-nov.xls")

# Sort the data by "Date And Time"
sorted_df = df.sort_values(by='Date And Time', ascending=True)

# Display the sorted results with all columns
print("\nLogs sorted from earliest clock-in:")
print(sorted_df)

# To make it more readable, let's show just a few key columns
# Assuming you have columns like 'Name' or 'Employee ID'
# Replace these column names with your actual column names
print("\nSimplified view:")
# Example: print(sorted_df[['Name', 'Date And Time', 'Status']])
