import pandas as pd

# Create sample dataset
data = {
    'Date': ['2025-01-10', '2025-02-15',
             'invalid', '2025-04-20', '2025-05-25'],

    'Price': ['₹1,200', '₹2,500', '₹3,000',
              'invalid', '₹4,500'],

    'Quantity': ['10', '20', 'abc', '30', '40']
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Convert Date into datetime
df['Date'] = pd.to_datetime(
    df['Date'],
    errors='coerce'
)

# Convert Price into numeric values
df['Price'] = (
    df['Price']
    .str.replace('₹', '', regex=False)
    .str.replace(',', '', regex=False)
)

df['Price'] = pd.to_numeric(
    df['Price'],
    errors='coerce'
)

# Convert Quantity into integer-compatible numeric values
df['Quantity'] = pd.to_numeric(
    df['Quantity'],
    errors='coerce'
).astype('Int64')

print("\nDataset After Type Conversion:")
print(df)

# Extract year
df['Year'] = df['Date'].dt.year

# Extract month
df['Month'] = df['Date'].dt.month

# Extract weekday
df['Weekday'] = df['Date'].dt.day_name()

print("\nDataset After Extracting Date Information:")
print(df)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display missing values
print("\nMissing Values:")
print(df.isnull().sum())