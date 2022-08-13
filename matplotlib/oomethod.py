import matplotlib.pyplot as plt
import numpy as np

# Example
x = np.linspace(0, 5, 11)
y = x ** 2

# OO Method
# First Example
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # Left, Bottom, Width, Height 0.1 = 10%
axes.plot(x, y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')

# Second Example
fig2 = plt.figure()
axes1 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])  # main axes
axes2 = fig2.add_axes([0.2, 0.5, 0.4, 0.3])  # inset axes

# Larger Figure Axes 1
axes1.plot(x, y, 'b')
axes1.set_xlabel('X_label_axes2')
axes1.set_ylabel('Y_label_axes2')
axes1.set_title('Axes 2 Title')

# Insert Figure Axes 2
axes2.plot(y, x, 'r')
axes2.set_xlabel('X_label_axes2')
axes2.set_ylabel('Y_label_axes2')
axes2.set_title('Axes 2 Title')

plt.tight_layout()
plt.show()



