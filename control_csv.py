import pandas as pd

# Create sample dataset
data = {
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['Rohini', 'Priti', 'Rahul', 'Sneha', 'Rohit', 'Neha'],
    'salary': [40000, '?', 60000, 45000, 'NA', 50000],
    'join_date': ['2022-01-10', '2022-03-15', '2021-06-20',
                  '2023-02-12', '2022-08-25', '2021-12-01'],
    'department': ['IT', 'HR', 'Sales', 'IT', 'Finance', 'HR']
}

# Create DataFrame and save CSV
df = pd.DataFrame(data)
df.to_csv('employee_missing.csv', index=False)

# Read only selected columns
df = pd.read_csv(
    'employee_missing.csv',
    usecols=['id', 'name', 'salary', 'join_date'],
    index_col='id',
    parse_dates=['join_date'],
    na_values=['?', 'NA'],
    nrows=5
)

# Display result
print("Selected Data:")
print(df)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())