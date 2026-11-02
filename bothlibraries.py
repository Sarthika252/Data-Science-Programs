import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.DataFrame({
    "Hours":[1,2,3,4,5,6],
    "Marks":[35,45,50,65,75,90]
})

sns.set_theme(style="whitegrid")
fig,axes = plt.subplots(1,2,figsize=(10,4))

axes[0].plot(df["Hours"],df["Marks"],marker='o')
axes[0].set_title("Hours vs Marks")
axes[0].set_xlabel("Study Hours")
axes[0].set_ylabel("Marks")


sns.scatterplot(x="Hours",y="Marks",data=df,ax=axes[1],s=100
                )
axes[1].set_title("Scatter Plot of Hours vs Marks")
plt.tight_layout()
plt.show()
  