import pandas as pd

# Create sample dataset with inconsistent text
data = {
    ' Employee Name ': [' shravani ', 'PRITI', 'Rahul ', ' shravani ', 'Sneha'],
    ' CITY ': [' pune ', 'MUMBAI', 'kolhapur', ' pune ', 'PUNE'],
    ' Department ': [' it ', 'HR', 'sales', ' it ', 'Finance']
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Standardize column names to snake_case
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
)

print("\nStandardized Column Names:")
print(df.columns)

# Remove whitespace from text columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()

# Fix capitalization
df['employee_name'] = df['employee_name'].str.title()
df['city'] = df['city'].str.title()
df['department'] = df['department'].str.title()

print("\nCleaned Text Dataset:")
print(df)

# Find duplicate rows
print("\nDuplicate Rows:")
print(df[df.duplicated()])

# Count duplicate rows
print("\nNumber of Duplicates:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nDataset After Removing Duplicates:")
print(df)

# Reset index
df = df.reset_index(drop=True)

print("\nFinal Cleaned Dataset:")
print(df)