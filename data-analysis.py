import pandas as pd

# Read an Excel file
df = pd.read_excel("18-nov.xls")

# Basic analysis examples
# Display first few rows
print(df.head())

# Get basic statistics
print(df.describe())

# Check data info (columns, data types, non-null values)
print(df.info())

# Get column names
print(df.columns)

# Basic calculations on specific columns
# Example: mean of a numeric column
# print(df['column_name'].mean())
