import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

tips.head()

# DISTPLOT
# plt.figure()
sns.distplot(tips['total_bill'])
# sns.distplot(tips['total_bill'],kde=False,bins=30)

# JOINTPLOT
# plt.figure()
sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')
# sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')

# PAIRPLOT
# plt.figure()
sns.pairplot(tips)

# RUGPLOT
plt.figure()
sns.rugplot(tips['total_bill'])

plt.show()