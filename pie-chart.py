"""
This script is ideal for visually representing portions of a whole, such as market shares or survey results.
The use of different colors, shadows, and the 'explode' feature makes the chart more informative and visually appealing.
Pie charts like this are commonly used in presentations and reports for their clarity and immediate impact.
"""

from matplotlib import pyplot as plt  # Import the pyplot module from matplotlib for plotting.

# Data for the pie chart.
slices = [7, 2, 1, 11]  # The size of each slice.
types = ['type1', 'type2', 'type3', 'type4']  # Labels for each slice.
cols = ['c', 'm', 'r', 'b']  # Colors for each slice.

# Creating the pie chart.
plt.pie(slices,
        labels=types,  # Assign labels to slices.
        colors=cols,  # Assign colors to slices.
        startangle=90,  # Start the pie chart at a 90-degree angle.
        shadow=True,  # Add a shadow for a 3D effect.
        explode=(0, 0.1, 0, 0),  # 'Explode' a slice out of the chart.
        autopct='%1.1f%%')  # Show percentage values in the chart.

plt.title('Plot title')  # Title of the plot.

plt.show()  # Display the plot.
