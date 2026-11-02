import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create product revenue dataset
data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Keyboard', 'Mouse'],
    'Revenue': [80000, 120000, 60000, 30000, 20000]
}

df = pd.DataFrame(data)

# Sort revenue from highest to lowest
df = df.sort_values(by='Revenue', ascending=False)

# Create three subplots
fig, axes = plt.subplots(1, 3, figsize=(17, 5))

# (a) Horizontal bar chart
axes[0].barh(df['Product'], df['Revenue'])
axes[0].invert_yaxis()
axes[0].set_title('Revenue per Product')
axes[0].set_xlabel('Revenue')
axes[0].set_ylabel('Products')

# (b) Grouped bar chart
products = ['Laptop', 'Mobile', 'Tablet', 'Keyboard']

quarter1 = [80000, 100000, 50000, 25000]
quarter2 = [100000, 120000, 60000, 30000]

x = np.arange(len(products))
width = 0.35

axes[1].bar(x - width/2, quarter1, width, label='Quarter 1')
axes[1].bar(x + width/2, quarter2, width, label='Quarter 2')

axes[1].set_title('Quarterly Revenue Comparison')
axes[1].set_xlabel('Products')
axes[1].set_ylabel('Revenue')
axes[1].set_xticks(x)
axes[1].set_xticklabels(products, rotation=30)
axes[1].legend()

# (c) Pie chart
market_share = [35, 30, 20, 10, 5]
labels = ['Laptop', 'Mobile', 'Tablet', 'Keyboard', 'Mouse']

axes[2].pie(
    market_share,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90
)

axes[2].set_title('Product Market Share')

plt.tight_layout()
plt.show()