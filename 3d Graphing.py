# from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


def f(i, j):
    return 50 - (i ** 2 + j ** 2)


x_intervals = np.linspace(-5, 5, 50)
y_intervals = np.linspace(-5, 5, 50)
x, y = np.meshgrid(x_intervals, y_intervals)

z = f(x, y)
print(z)
fig = plt.figure()
ax = plt.axes(projection='3d')

"""
# for contour
ax.contour3D(x, y, z, 50, cmap='binary')

# for wireframe
ax.plot_wireframe(x, y, z, color='black')

# surface
ax.plot_surface(x, y, z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')

# trisurface
ax.plot_trisurf(x, y, z,
                cmap='viridis', edgecolor='none')
"""

ax.plot_surface(x, y, z, cmap='viridis')
ax.set_xlabel('Var I')
ax.set_ylabel('Var J')
ax.set_zlabel('Value')

ax.set_title('Stochastic')

# ax.view_init(60, 35)

plt.show()
