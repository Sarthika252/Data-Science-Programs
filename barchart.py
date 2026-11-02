import matplotlib.pyplot as plt
subjects=['Python','Java','SQL','AI','ML']
marks=[85,75,90,80,70]
plt.bar(subjects, marks)

plt.title("Marks in different subjects:")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()