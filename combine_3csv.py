import pandas as pd

# Create January sales data
jan_data = {
    'Product': ['Laptop', 'Mobile', 'Tablet'],
    'Sales': [50000, 30000, 20000]
}

# Create February sales data
feb_data = {
    'Product': ['Laptop', 'Mobile', 'Tablet'],
    'Sales': [60000, 35000, 25000]
}

# Create March sales data
mar_data = {
    'Product': ['Laptop', 'Mobile', 'Tablet'],
    'Sales': [55000, 40000, 30000]
}

# Convert data into DataFrames
jan_df = pd.DataFrame(jan_data)
feb_df = pd.DataFrame(feb_data)
mar_df = pd.DataFrame(mar_data)

# Save each month's data into separate CSV files
jan_df.to_csv('January.csv', index=False)
feb_df.to_csv('February.csv', index=False)
mar_df.to_csv('March.csv', index=False)

print("Three monthly CSV files created successfully!")

# Read all three CSV files
jan = pd.read_csv('January.csv')
feb = pd.read_csv('February.csv')
mar = pd.read_csv('March.csv')

# Add source column to identify the month
jan['Source'] = 'January'
feb['Source'] = 'February'
mar['Source'] = 'March'

# Combine all DataFrames
combined_df = pd.concat(
    [jan, feb, mar],
    ignore_index=True
)

# Display combined dataset
print("\nCombined Monthly Sales Data:")
print(combined_df)

# Save combined data into a new CSV file
combined_df.to_csv('Combined_Sales.csv', index=False)

print("\nCombined CSV file saved successfully!")