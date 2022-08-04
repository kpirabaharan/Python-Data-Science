import pandas as pd

# Create dataframe
data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

# Group by company
byComp = df.groupby('Company')

# Then we can call methods on the byComp object
byComp.mean()
byComp.sum()
byComp.std()
# Note for max it took the max name and max num and they dont match
byComp.max()
byComp.describe()
byComp.describe().transpose()
byComp.describe().transpose()['GOOG']

