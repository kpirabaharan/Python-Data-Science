import matplotlib.pyplot as plt
import numpy as np

# %matplotlib inline to see plots

# Example
x = np.linspace(0, 5, 11)
y = x ** 2

# Functional Method

# Plot Commands
plt.figure(1)
plt.plot(x, y, 'r')  # r = color red
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('Title Here')

# Multiple Plots on Same Canvas
# plt.subplot(nrows, ncols, plot_number)
plt.figure(2)
plt.subplot(1, 2, 1)
plt.plot(x, y, 'r--')  # Red Dashed
plt.subplot(1, 2, 2)
plt.plot(y, x, 'g*-')  # Green Star Dashed
plt.show()