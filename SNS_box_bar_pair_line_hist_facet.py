# Importing Seaborn

import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

# scatter-plot
print("\nSeaborn Scatterplot\n")
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()

# line-plot
print("\nSeaborn lineplot\n")
sns.lineplot(x="total_bill", y="tip", data=tips)
plt.show()

# Histogram
print("\nSeaborn Histogram\n")
sns.histplot(tips["total_bill"], bins=10)
plt.show()

# Box Plot
print("\nSeaborn boxplot\n")
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()

# Bar Plot
print("\nSeaborn barplot\n")
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()

sns.set_theme(style="whitegrid")
print("\nSeaborn boxplot setting theme 'whitegrid'\n")
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()

print("\nSeaborn pairplot\n")
sns.pairplot(tips)
plt.show()

print("\nSeaborn FacetGrid\n")
g = sns.FacetGrid(tips, col="time")
g.map(sns.histplot, "total_bill")
plt.show()