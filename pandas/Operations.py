import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()

# Returns unique values
df['col2'].unique()

# Returns number of unique values
df['col2'].nunique()

# Count how many times the value in 'col' shows up
df['col2'].value_counts()


# Apply functions()
def times2(x):
    return x*2


df['col2'].apply(times2)

# Remove column
del df['col1']

# ** Get column and index names: **
df.columns
df.index

# Sort by column
df.sort_values(by='col2') #inplace=False by default

# Find Null
df.isnull()

# Drop NaN
df.dropna()
