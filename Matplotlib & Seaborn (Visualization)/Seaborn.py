import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')   # built-in dataset

# Distribution
sns.histplot(tips['total_bill'], kde=True)
plt.show()

# Box plot
sns.boxplot(x='day', y='total_bill', data=tips)
plt.show()

# Correlation heatmap
sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.show()

# Pairplot (scatter matrix — gold for EDA!)
sns.pairplot(tips, hue='sex')
plt.show()