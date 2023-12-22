"""
This script showcases how to create a clear and concise line chart, ideal for comparing trends or changes over intervals.
The use of different colors and line styles makes each data set distinct, aiding in data interpretation and analysis.
"""

from matplotlib import pyplot as plt, style

style.use('ggplot')  # Apply the 'ggplot' style for a visually pleasing aesthetic.

# Sample data for plotting.
x = [5, 6, 7, 8]  # X-axis data points.
y = [7, 3, 8, 3]  # Y-axis data points for the first line.
y2 = [2, 9, 0, 4]  # Y-axis data points for the second line.

# Plotting the data.
plt.plot(x, y, 'k', linewidth=1, label="line1")  # Plot the first line in black with a label.
plt.plot(x, y2, 'y', linewidth=1, label="line2")  # Plot the second line in yellow with a label.

# Adding chart elements.
plt.title("CHART TITLE")  # Title of the chart.
plt.ylabel("Y axis")  # Label for the Y-axis.
plt.xlabel("X axis")  # Label for the X-axis.
plt.legend()  # Display a legend to label the lines.

# Display the plot.
plt.show()  # Render and display the plot.
