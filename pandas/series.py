import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array(my_list)
d = {'a': 10, 'b': 20, 'c': 30}

# Series using Lists
pd.Series(data=my_list)
pd.Series(data=my_list, index=labels)
# pd.Series(my_list,labels)

# Series using NP Arrays
pd.Series(arr, labels)

# Series using dictionaries
pd.Series(d)

ser1 = pd.Series([1, 2, 3, 4], index = ['USA', 'Germany', 'USSR', 'Japan'])
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])

ser1['USA']
ser1 + ser2
# Note in Ser1 + Ser2 Indices that don't appear in both are NaN

