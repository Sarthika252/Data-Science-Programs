import pandas as pd
import json

# Create sample employee dataset
data = {
    'id': [101, 102, 103, 104],
    'name': ['Kranti', 'Shruti', 'Rahul', 'Sneha'],
    'department': ['IT', 'HR', 'Sales', 'Finance'],
    'salary': [40000, 50000, 60000, 55000]
}

df = pd.DataFrame(data)

# Save DataFrame to Excel
df.to_excel('employee.xlsx', index=False)

print("Excel file saved successfully!")

# Save DataFrame to JSON
df.to_json('employee.json', orient='records', indent=4)

print("JSON file saved successfully!")

# Read Excel file
excel_data = pd.read_excel('employee.xlsx')

print("\nData Read From Excel:")
print(excel_data)

# Read JSON file
json_data = pd.read_json('employee.json')

print("\nData Read From JSON:")
print(json_data)

# Create nested JSON data
nested_data = [
    {
        'id': 1,
        'name': 'Amit',
        'address': {
            'city': 'Kolhapur',
            'state': 'Maharashtra'
        },
        'skills': ['Python', 'SQL']
    },
    {
        'id': 2,
        'name': 'Priya',
        'address': {
            'city': 'Pune',
            'state': 'Maharashtra'
        },
        'skills': ['Java', 'Python']
    }
]

# Save nested JSON file
with open('nested_employee.json', 'w') as file:
    json.dump(nested_data, file, indent=4)

# Flatten nested JSON into a table
flat_data = pd.json_normalize(nested_data)

print("\nFlattened JSON Data:")
print(flat_data)