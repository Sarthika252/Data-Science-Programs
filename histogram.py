import seaborn as sns
from matplotlib import pyplot as plt
marks=[45, 50, 55, 60, 60, 65, 70, 75, 80, 90]
sns.histplot(marks, bins=5, kde=True, color="skyblue")
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()