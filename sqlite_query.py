import pandas as pd
import sqlite3

# Create employee dataset
data = {
    'id': [101, 102, 103, 104],
    'name': ['Rohit', 'Shanti', 'Rahul', 'Sneha'],
    'department': ['IT', 'HR', 'Sales', 'Finance'],
    'salary': [40000, 50000, 60000, 55000]
}

df = pd.DataFrame(data)

# Create SQLite database connection
conn = sqlite3.connect('company.db')

# Store DataFrame in SQLite database
df.to_sql(
    'employees',
    conn,
    if_exists='replace',
    index=False
)

print("Data stored in SQLite database successfully!")

# Write SQL query
query = "SELECT * FROM employees WHERE salary > 45000"

# Read data using SQL query
result = pd.read_sql(query, conn)

# Display result
print("\nEmployees with salary greater than 45000:")
print(result)

# Close database connection
conn.close()