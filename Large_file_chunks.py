import pandas as pd
import numpy as np

# Create a dataset with 1 million rows
n = 1000000

data = {
    'id': range(1, n + 1),
    'city': np.random.choice(
        ['Kolhapur', 'Pune', 'Mumbai', 'Nashik'],
        size=n
    ),
    'sales': np.random.randint(100, 5000, size=n)
}

df = pd.DataFrame(data)

# Save dataset as CSV
df.to_csv('large_sales.csv', index=False)

print("1 Million rows CSV file created successfully!")

# Read CSV in chunks of 200000 rows
chunk_size = 200000

total_sales = {}

for chunk in pd.read_csv('large_sales.csv', chunksize=chunk_size):

    # Calculate sales city-wise for each chunk
    city_sales = chunk.groupby('city')['sales'].sum()

    # Add sales to the final result
    for city, sales in city_sales.items():

        if city in total_sales:
            total_sales[city] += sales
        else:
            total_sales[city] = sales

# Convert result into DataFrame
result = pd.DataFrame(
    list(total_sales.items()),
    columns=['City', 'Total Sales']
)

# Display final result
print("\nTotal Sales Per City:")
print(result)

# Display total rows processed
print("\nTotal Rows Processed:", n)