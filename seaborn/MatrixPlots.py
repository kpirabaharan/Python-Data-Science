import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
flights = pd.read_csv('flights.csv')  # Not working

print(tips.head())
print(flights.head())

print(tips.corr())

# Heatmap
plt.figure()
sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)

print(flights.pivot_table(values='passengers',index='month',columns='year'))

plt.figure()
pvflights = flights.pivot_table(values='passengers',index='month',columns='year')
sns.heatmap(pvflights,cmap='magma',linecolor='white',linewidths=1)

# CLusterMap
plt.figure()
sns.clustermap(pvflights)

# More options to get the information a little clearer like normalization
sns.clustermap(pvflights,cmap='coolwarm',standard_scale=1)

plt.show()


