import matplotlib.pyplot as plt
import numpy as np
from random import sample

# Example
x = np.linspace(0, 5, 11)
y = x ** 2

# Scatter
plt.figure()
plt.scatter(x, y)

# Histogram
data = sample(range(1, 1000), 100)
plt.figure()
plt.hist(data)

# Rectangular box plot
plt.figure()
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data, vert=True, patch_artist=True)

plt.show()
