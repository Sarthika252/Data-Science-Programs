import pandas as pd
import matplotlib.pyplot as plt

# Create sample sales dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],

    'Sales': [12000, 15000, 14000, 18000, 20000, 22000,
              19000, 25000, 23000, 27000, 30000, 32000],

    'Product': ['Laptop', 'Mobile', 'Tablet', 'Keyboard',
                'Mouse', 'Laptop', 'Mobile', 'Tablet',
                'Keyboard', 'Mouse', 'Laptop', 'Mobile']
}

df = pd.DataFrame(data)

# Create 2x2 dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# (1) Line plot
axes[0, 0].plot(
    df['Month'],
    df['Sales'],
    marker='o'
)

axes[0, 0].set_title('Monthly Sales Trend')
axes[0, 0].set_xlabel('Month')
axes[0, 0].set_ylabel('Sales')
axes[0, 0].grid(True)

# (2) Bar chart
axes[0, 1].bar(
    df['Month'],
    df['Sales']
)

axes[0, 1].set_title('Monthly Sales Bar Chart')
axes[0, 1].set_xlabel('Month')
axes[0, 1].set_ylabel('Sales')

# (3) Histogram
axes[1, 0].hist(
    df['Sales'],
    bins=6,
    edgecolor='black'
)

axes[1, 0].set_title('Sales Distribution')
axes[1, 0].set_xlabel('Sales Amount')
axes[1, 0].set_ylabel('Frequency')

# (4) Pie chart
product_sales = df.groupby('Product')['Sales'].sum()

axes[1, 1].pie(
    product_sales,
    labels=product_sales.index,
    autopct='%1.1f%%',
    startangle=90
)

axes[1, 1].set_title('Product-wise Sales Share')

# Add overall title
fig.suptitle(
    'Sales Analysis Dashboard',
    fontsize=16,
    fontweight='bold'
)

# Adjust spacing
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Save dashboard as high-resolution PNG
plt.savefig(
    'Sales_Dashboard.png',
    dpi=300,
    bbox_inches='tight'
)

# Display dashboard
plt.show()

print("Dashboard saved successfully as Sales_Dashboard.png")