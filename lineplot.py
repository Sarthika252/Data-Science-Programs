import pandas as pd
import matplotlib.pyplot as plt

# Create sample sales dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],

    '2025': [12000, 15000, 14000, 18000, 20000, 22000,
             19000, 25000, 23000, 27000, 30000, 32000],

    '2026': [15000, 17000, 16000, 21000, 24000, 26000,
             23000, 28000, 27000, 31000, 35000, 38000]
}

df = pd.DataFrame(data)

# Find the best month of current year (2026)
best_index = df['2026'].idxmax()
best_month = df.loc[best_index, 'Month']
best_sales = df.loc[best_index, '2026']

# Plot sales trends
plt.figure(figsize=(10, 5))

plt.plot(df['Month'], df['2025'],
         marker='o', label='Sales 2025')

plt.plot(df['Month'], df['2026'],
         marker='s', label='Sales 2026')

# Annotate best month
plt.annotate(
    f'Best Month: {best_month}\nSales: {best_sales}',
    xy=(best_index, best_sales),
    xytext=(best_index - 3, best_sales + 3000),
    arrowprops=dict(arrowstyle='->')
)

# Add title, labels, grid and legend
plt.title('Monthly Sales Trend (2025-2026)')
plt.xlabel('Months')
plt.ylabel('Sales Amount')
plt.grid(True)
plt.legend()

plt.show()

# Display best month
print("Best Month:", best_month)
print("Highest Sales:", best_sales)