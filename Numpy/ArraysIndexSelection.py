# Numpy Code, Run in Python Console

import numpy as np

my_list = [1, 2, 3]

np.array(my_list)

np.arange(0, 10)

# Linearly interpolated array
np.linspace(0, 5, 101)

# Create a List
arr = np.arange(20)

# Reshape
arr.reshape(5, 4)

# Slicing
arr[3:10]

# Broadcast
arr[1:5] = 100

# Selection
arr > 10
# New List after Selection
arr[arr > 10]