""" DataFrames P1 and P2 """
import pandas as pd
import numpy as np
from numpy.random import randn

np.random.seed(101)

# DatFrames are just series with shared indices
df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())
# Data  = 5 by 4 table of random numbers from standard normal distribution -3 to 3 normal
# Index and Columns as stated (.split() splits at space since no parameter is passed)

# Selection
# Column(s)
df[['W', 'Z']]
# Row
df.loc['A']
# Row by index
df.iloc[2]
# Specific index
df.loc['C', 'X']
# Subset
df.loc[['A', 'B'], ['W', 'Y']]

# Add row
df['new'] = df['W'] + df['Y']

# Remove Rows
df.drop('new', axis=1, inplace=True)  # Need this inplace to be True to actually remove the column from table
# df.drop('E', inplace=True)

# Conditional Selection
df > 0  # Bool Output

df[df > 0]  # Numerical Output

# For just one column
cond = df['W'] > 0
df[cond]

# Conditional applied on one column but applied to another
df[df['W'] > 0]['Y']

# Conditional applied on one column but applied to multiple
df[df['W'] > 0][['Y', 'X']]

# For two conditions you can use | and & with parenthesis:

df[(df['W'] > 0) & (df['Y'] > 1)]

# Reset Index (inplace = True to stay)
df.reset_index()

# More
newind = 'CA NY WY OR CO'.split()
df['States'] = newind

# Set new indices
df.set_index('States')
