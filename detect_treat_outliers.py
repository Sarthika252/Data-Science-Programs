import pandas as pd
import numpy as np

# Create sample salary dataset
data = {
    'Employee': ['Tara', 'Prisha', 'Rahul', 'Sneha',
                 'Rohit', 'Neha', 'Kiran', 'Pooja',
                 'Raj', 'Anjali'],

    'Salary': [25000, 30000, 28000, 35000, 40000,
               32000, 45000, 38000, 50000, 200000]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Calculate Q1 and Q3
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Calculate lower and upper limits
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

# Identify outliers
outliers = df[
    (df['Salary'] < lower_limit) |
    (df['Salary'] > upper_limit)
]

print("\nDetected Outliers:")
print(outliers)

# Version 1: Remove outliers
df_removed = df[
    (df['Salary'] >= lower_limit) &
    (df['Salary'] <= upper_limit)
]

print("\nDataset After Removing Outliers:")
print(df_removed)

# Version 2: Cap outliers
df_capped = df.copy()

df_capped['Salary'] = df_capped['Salary'].clip(
    lower=lower_limit,
    upper=upper_limit
)

print("\nDataset After Capping Outliers:")
print(df_capped)

# Version 3: Create outlier flag column
df_flagged = df.copy()

df_flagged['Outlier_Flag'] = np.where(
    (df_flagged['Salary'] < lower_limit) |
    (df_flagged['Salary'] > upper_limit),
    'Outlier',
    'Normal'
)

print("\nDataset With Outlier Flag:")
print(df_flagged)