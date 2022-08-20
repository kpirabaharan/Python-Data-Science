import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips')

# barplot
sns.barplot(x='sex',y='total_bill',data=tips)
# sns.barplot(x='sex',y='total_bill',data=tips, estimator=np.std)

# countplot
plt.figure()
sns.countplot(x='sex',data=tips)

# boxplot
plt.figure()
# sns.boxplot(x="day", y="total_bill", data=tips,palette='rainbow')
sns.boxplot(x="day", y="total_bill", data=tips,palette='rainbow', hue='smoker')

#violinplot
plt.figure()
sns.violinplot(x="day", y="total_bill", data=tips,palette='rainbow')

# Stripplot
plt.figure()
strip = sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)

# Swarmplot
plt.figure()
sns.swarmplot(x="day", y="total_bill", data=tips)

# Combine violin and swarm
plt.figure()
sns.violinplot(x="tip", y="day", data=tips,palette='rainbow')
sns.swarmplot(x="tip", y="day", data=tips,color='black',size=3)

# FactorPlot (GENERIC PLOT, specify kind to one of above plots)
plt.figure()
sns.catplot(x='sex',y='total_bill',data=tips,kind='bar')

plt.show()