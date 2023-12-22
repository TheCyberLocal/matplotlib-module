"""
This script is a simple yet effective way to visualize data distribution.
By grouping data into bins and displaying the frequency of data in each bin,
 histograms like this can provide insights into the nature of the dataset,
 such as skewness, outliers, or central tendency.
"""

from matplotlib import pyplot as plt  # Import pyplot for plotting.

# Sample data for the histogram.
population = [21, 54, 87, 9, 51, 51, 15, 51, 71, 81, 6, 62, 26, 62, 32, 24, 40]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]  # Define the range of values for each bin.

# Create a histogram.
plt.hist(population, bins, histtype='bar', rwidth=0.8)  # Plot histogram with specified bins and bar style.

# Labeling the plot.
plt.xlabel('x_label')  # Label for the x-axis.
plt.ylabel('y_label')  # Label for the y-axis.
plt.title('Plot title')  # Title of the histogram.

plt.legend()  # Optional: Add a legend if needed.

# Display the plot.
plt.show()  # Render and show the histogram.
