"""
The script is an excellent example of using bar charts for data comparison,
 showcasing the ease and flexibility of data visualization in Python.
The contrasting colors and widths of the bars make it easy to distinguish between the two datasets.
"""

from matplotlib import pyplot as plt, style  # Import pyplot for plotting and style for styling plots.

style.use('ggplot')  # Apply the 'ggplot' style for aesthetically pleasing plots.

# Data sets for the bar chart.
x = [2, 4, 6, 8]  # X-axis coordinates for the first set of bars.
y = [7, 3, 8, 3]  # Heights of the first set of bars.

x2 = [1, 3, 5, 7]  # X-axis coordinates for the second set of bars.
y2 = [2, 9, 0.5, 4]  # Heights of the second set of bars.

# Creating the bar charts.
plt.bar(x, y, color='b', label="line1", width=0.5)  # Plot the first set of bars in blue.
plt.bar(x2, y2, color='r', label="line2", width=0.25)  # Plot the second set of bars in red.

# Adding chart title and labels.
plt.title("CHART TITLE")  # Title of the chart.
plt.ylabel("Y axis")  # Label for the Y-axis.
plt.xlabel("X axis")  # Label for the X-axis.

plt.legend()  # Display the legend to label the bar sets.

# Display the plot.
plt.show()  # Render and display the plot.
