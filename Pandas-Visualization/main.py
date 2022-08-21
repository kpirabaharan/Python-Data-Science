import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df1 = pd.read_csv('df1', index_col=0)

print(df1.head())

df2 = pd.read_csv('df2')

print(df2.head())

plt.figure()
df1['A'].plot.hist(bins=30)
df2.plot.area(alpha=0.4)
df2.plot.bar(stacked=True)
df1.plot.scatter(x='A', y='B')
df2.plot.box()
plt.show(),
