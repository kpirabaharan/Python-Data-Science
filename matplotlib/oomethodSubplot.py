import matplotlib.pyplot as plt
import numpy as np

# Example
x = np.linspace(0, 5, 11)
y = x ** 2

# Subplot
# Use similar to plt.figure() except use tuple unpacking to grab fig and axes
fig3, axes3 = plt.subplots(nrows=1, ncols=2)

# Now use the axes object to add stuff to plot
axes3[0].plot(x, y, 'r')
axes3[1].plot(y, x, 'r')
for ax in axes3:
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

