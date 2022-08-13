import matplotlib.pyplot as plt
import numpy as np

# Example
x = np.linspace(0, 5, 11)
y = x ** 2

# MATLAB style line color and style
fig, ax = plt.subplots()
ax.plot(x, x ** 2, color='#FF8C00', ls=':', lw=5, alpha=0.5)  # blue line with dots
ax.plot(x, x ** 3, lw=0.5, marker='+', markersize=10)  # green dashed line

# Plot Range
ax.set_ylim([20, 90])
ax.set_xlim([2, 5])

# Another Ex
# axes[0].plot(x, x**2, x, x**3)
# axes[0].set_title("default axes ranges")
#
# axes[1].plot(x, x**2, x, x**3)
# axes[1].axis('tight')
# axes[1].set_title("tight axes")

plt.tight_layout()
plt.show()
