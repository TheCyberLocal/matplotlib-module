"""
This script is a clear example of 3D surface plotting in Python.
It calculates values using a user-defined function and visualizes these values in three dimensions.
This is useful in various fields for visualizing the relationships between two independent variables and their impact on a dependent variable.
"""

import numpy as np  # Import numpy for numerical operations.
import matplotlib.pyplot as plt  # Import matplotlib for plotting.

# Define the function to be plotted.
def f(i, j):
    return 50 - (i ** 2 + j ** 2)  # Function returns value based on i and j.

# Set the intervals for x and y.
x_intervals = np.linspace(-5, 5, 50)  # Generate 50 points between -5 and 5 for x.
y_intervals = np.linspace(-5, 5, 50)  # Generate 50 points between -5 and 5 for y.

# Create meshgrid for plotting.
x, y = np.meshgrid(x_intervals, y_intervals)  # Create a meshgrid for x and y values.

# Calculate z values using the function.
z = f(x, y)  # Apply the function to each combination of x and y.
print(z)  # Print the calculated z values.

# Set up the figure and 3D axis for plotting.
fig = plt.figure()  # Create a new figure.
ax = plt.axes(projection='3d')  # Add 3D axes to the figure.

# Plot the surface.
ax.plot_surface(x, y, z, cmap='viridis')  # Create a surface plot with viridis color map.
ax.set_xlabel('Var I')  # Label for the x-axis.
ax.set_ylabel('Var J')  # Label for the y-axis.
ax.set_zlabel('Value')  # Label for the z-axis.

ax.set_title('Stochastic')  # Title for the plot.

# ax.view_init(60, 35)  # Uncomment to set the viewing angle.

# Display the plot.
plt.show()  # Show the plot in a window.
