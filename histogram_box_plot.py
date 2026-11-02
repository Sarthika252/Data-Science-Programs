import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create sample exam score dataset
data = {
    'Class A': [45, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    'Class B': [40, 50, 55, 60, 65, 70, 75, 80, 85, 90],
    'Class C': [50, 60, 65, 70, 75, 80, 85, 90, 95, 100]
}

df = pd.DataFrame(data)

# Select scores for histogram
scores = df['Class A']

# Calculate mean
mean_score = scores.mean()

# Create two subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# (a) Histogram
axes[0].hist(scores, bins=5, edgecolor='black')

# Draw vertical mean line
axes[0].axvline(
    mean_score,
    linestyle='--',
    linewidth=2,
    label=f'Mean = {mean_score}'
)

axes[0].set_title('Distribution of Exam Scores')
axes[0].set_xlabel('Exam Scores')
axes[0].set_ylabel('Frequency')
axes[0].legend()
axes[0].grid(axis='y')

# (b) Box plot
axes[1].boxplot(
    [df['Class A'], df['Class B'], df['Class C']],
    tick_labels=['Class A', 'Class B', 'Class C']
)

axes[1].set_title('Comparison of Three Classes')
axes[1].set_xlabel('Classes')
axes[1].set_ylabel('Exam Scores')
axes[1].grid(axis='y')

plt.tight_layout()
plt.show()

print("Mean Score of Class A:", mean_score)