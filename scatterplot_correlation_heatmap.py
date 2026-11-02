import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Create sample student dataset
data = {
    'Study_Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Exam_Score': [35, 40, 45, 50, 60, 65, 70, 80, 85, 95],
    'Attendance': [60, 65, 70, 75, 80, 85, 90, 95, 80, 98],
    'Assignments': [2, 3, 3, 4, 5, 5, 6, 7, 8, 10]
}

df = pd.DataFrame(data)

# Create scatter plot
plt.figure(figsize=(9, 5))

scatter = plt.scatter(
    df['Study_Hours'],
    df['Exam_Score'],
    c=df['Attendance'],
    cmap='viridis',
    s=100
)

# Add trend line
m, b = np.polyfit(
    df['Study_Hours'],
    df['Exam_Score'],
    1
)

plt.plot(
    df['Study_Hours'],
    m * df['Study_Hours'] + b,
    linestyle='--',
    label='Trend Line'
)

plt.colorbar(scatter, label='Attendance (%)')

plt.title('Study Hours vs Exam Score')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.legend()
plt.grid(True)

plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 5))

correlation = df.corr(numeric_only=True)

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    linewidths=0.5,
    fmt='.2f'
)

plt.title('Correlation Heatmap')
plt.show()

# Display correlation values
print("Correlation Matrix:")
print(correlation)