"""
This script is a simple yet effective demonstration of creating visually appealing scatter plots with Matplotlib in Python.
By customizing the marker styles and sizes, it shows how to make distinct and informative scatter plots.
This kind of plot is particularly useful for comparing two or more groups of data points visually.
"""

from matplotlib import pyplot as plt, style  # Import pyplot for plotting and style for styling plots.

style.use('ggplot')  # Use the 'ggplot' style for the plots.

# Data sets for plotting.
x = [5, 6, 7, 8]  # X-axis data for the first set of points.
y = [7, 3, 8, 3]  # Y-axis data for the first set of points.

x2 = [5, 6, 7, 8]  # X-axis data for the second set of points.
y2 = [2, 9, 0, 4]  # Y-axis data for the second set of points.

# Plotting the scatter plots.
plt.scatter(x, y, color='g', label="dot1", marker='h', s=20)  # Scatter plot for the first data set with hexagon markers.
plt.scatter(x2, y2, color='b', label="dot2", marker='*', s=50)  # Scatter plot for the second data set with star markers.

# Adding plot title and labels.
plt.title("CHART TITLE")  # Title of the plot.
plt.ylabel("Y axis")  # Label for the Y-axis.
plt.xlabel("X axis")  # Label for the X-axis.

plt.legend()  # Show the legend to label data sets.

plt.show()  # Display the plot.
