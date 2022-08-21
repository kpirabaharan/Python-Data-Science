import matplotlib.pyplot as plt
import numpy as np

# Example
x = np.linspace(0, 5, 11)
y = x ** 2

# Figure Size and DPI
# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 2))

# axes[0].plot(x, y)
# axes[1].plot(y, x)

# Legends and Labels
fig, ax = plt.subplots(nrows=1, ncols=1)

# ax = fig.add_axes([0.1,0.1,0.8,0.8])

ax.plot(x, x**2, label="x**2")
ax.plot(x, x**3, label="x**3")
ax.legend(loc=0)  # loc = 0, best location for legend

# Save Figure
fig.savefig('my_picture.jpg', dpi=200)

plt.tight_layout()
plt.show()
