import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.csv')

# PairGrid
# Just the grid
sns.PairGrid(iris)

# Then you map to the grid
g = sns.PairGrid(iris)
g.map(plt.scatter)

# Different types of plots for diagonals
# Map to upper,lower, and diagonal
g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

# PairPlot (simpler)
sns.pairplot(iris,hue='species',palette='rainbow')

# Facetplot
tips = sns.load_dataset('tips')
# g = sns.FacetGrid(tips, col="time",  row="smoker")
# g = g.map(plt.hist, "total_bill")

g = sns.FacetGrid(tips, col="time",  row="smoker",hue='sex')
g = g.map(plt.scatter, "total_bill", "tip").add_legend()

# Jointgrid
h = sns.JointGrid(x="total_bill", y="tip", data=tips)
h = h.plot(sns.regplot, sns.distplot)

plt.show()

