import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib
matplotlib.use('TkAgg') #Had issues with the weyland backend for matplotlib
import matplotlib.pyplot as plt

data = pd.read_csv('Student_Scores_Data.csv')

print(data.head())

#print(data.head())

#----------DESCRIPTIVE STATS----------

print(f"Mean: {data["Score"].mean()}")

print(f"Median: {data["Score"].median()}")

print(f"Standard deviation: {data["Score"].std()}")

print(f"Variance: {data["Score"].var()}")

print(f"Range: {data["Score"].max()-data["Score"].min()}")


#--------------DATAVIS----------------

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

sns.histplot(data["Score"], bins=30, color='c', edgecolor='black',kde=True, ax=axs[0])
axs[0].set_title("Histogram of Scores")
axs[0].set_xlabel("Score")
axs[0].set_ylabel("Frequency")

sns.violinplot(data=data["Score"], ax=axs[1], color='c')
axs[1].set_title("Violin Plot of Scores")
axs[1].set_xlabel("Score")

plt.tight_layout()
plt.show()