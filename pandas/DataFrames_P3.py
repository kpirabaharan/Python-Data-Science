""" DataFrames P3 """
import pandas as pd
import numpy as np

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))
# zip pairs an item in one list with the same index item in the other list
# list makes it into a list

# Multi Index
hier_index = pd.MultiIndex.from_tuples(hier_index)

# Make a DF with MultiIndex
df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])

# Selection
df.loc['G1']
df.loc['G1'].loc[2]

df.index.names = ['Groups', 'Num']

# or use xs which can skip levels of indices
df.xs(1, level='Num')
