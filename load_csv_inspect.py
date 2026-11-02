import pandas as pd

# Create employee dataset
data = {
    'id': [101, 102, 103, 104, 105, 106],
    'name': ['Smit', 'Priti', 'Rahul', 'Sneha', 'Rohit', 'Neha'],
    'age': [25, 28, 30, 26, 32, 29],
    'department': ['IT', 'HR', 'Sales', 'IT', 'Finance', 'Sales'],
    'salary': [40000, 50000, 60000, 45000, 55000, 48000]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Save DataFrame as CSV
df.to_csv('employee.csv', index=False)

# Load CSV file
df = pd.read_csv('employee.csv')

# Display first 3 rows
print("First 3 Rows:")
print(df.head(3))

# Display shape
print("\nShape of Dataset:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Display employees earning more than 45000
print("\nEmployees earning more than 45000:")
print(df[df['salary'] > 45000])