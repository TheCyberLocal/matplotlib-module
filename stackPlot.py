"""
This script is a straightforward example of creating a stack plot using Matplotlib,
 a popular Python library for data visualization.
The plot presents four different datasets as stacked areas,
 making it easy to visualize how each part contributes to the whole over the defined steps.
The script is particularly useful for comparing multiple datasets visually.
"""

from matplotlib import pyplot as plt  # Import the pyplot module from matplotlib for plotting.

steps = [1, 2, 3, 4, 5]  # Define the x-axis intervals.

# Define four datasets.
set1 = [1, 2, 3, 1, 3]
set2 = [1, 3, 3, 2, 3]
set3 = [1, 2, 3, 4, 2]
set4 = [1, 1, 3, 1, 3]

# Plot empty lines for creating the legend.
plt.plot([], [], color='k', label='type4', linewidth=5)  # Legend entry for set4.
plt.plot([], [], color='r', label='type3', linewidth=5)  # Legend entry for set3.
plt.plot([], [], color='c', label='type2', linewidth=5)  # Legend entry for set2.
plt.plot([], [], color='m', label='type1', linewidth=5)  # Legend entry for set1.

# Create the stack plot.
plt.stackplot(steps, set1, set2, set3, set4, colors=['m', 'c', 'r', 'k'])

# Labeling the axes and setting the plot title.
plt.xlabel('x_label')  # Label for the x-axis.
plt.ylabel('y_label')  # Label for the y-axis.
plt.title('Plot title')  # Title for the plot.

# Display the legend.
plt.legend()  # Show the legend on the plot.

# Display the plot.
plt.show()  # Render the plot.
