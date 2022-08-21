import numpy as np
import pandas as pd

df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]})

# Drop all rows with NaN data
df.dropna()

# Drop all rows with NaN data
df.dropna(axis=1)

# Drop rows with at least # of NaN
df.dropna(thresh=2)

# Fill NaN with some value
df.fillna(value='FILL VALUE')

# Fill NaN value of row/column with mean of row/column
df['A'].fillna(value=df['A'].mean())
