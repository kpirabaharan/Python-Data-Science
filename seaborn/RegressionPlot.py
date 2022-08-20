import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex')

# W markers
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='coolwarm',
           markers=['o', 'v'], scatter_kws={'s': 100})

# Using a grid
sns.lmplot(x="total_bill", y="tip", row="sex", col="time", data=tips)

# With aspect and size
sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', palette='coolwarm',
           aspect=0.6, height=8)

sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', palette='coolwarm',
           aspect=0.2, height=8)

plt.show()
