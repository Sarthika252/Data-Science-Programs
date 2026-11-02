import pandas as pd
import numpy as np

# Create sample dataset
data = {
    'Name': ['Sanika', 'Priyanka', 'Rahul', 'Sneha', 'Rohit', 'Neha'],
    'Age': [25, np.nan, 30, 28, np.nan, 35],
    'City': ['Pune', 'Mumbai', np.nan, 'Pune', np.nan, 'Kolhapur'],
    'Salary': [30000, 40000, np.nan, 60000, np.nan, 80000]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Count missing values
print("\nMissing Values Count:")
print(df.isnull().sum())

# Calculate percentage of missing values
print("\nMissing Values Percentage:")
print((df.isnull().sum() / len(df)) * 100)

# Fill Age with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill City with mode
df['City'] = df['City'].fillna(df['City'].mode()[0])

# Fill Salary using interpolation
df['Salary'] = df['Salary'].interpolate(method='linear')

print("\nDataset After Filling Missing Values:")
print(df)

# Demonstrate dropna with threshold
# Keep rows having at least 3 non-missing values
df_drop = pd.DataFrame(data)

result = df_drop.dropna(thresh=3)

print("\nDataset After dropna(thresh=3):")
print(result)