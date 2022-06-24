from matplotlib import pyplot as plt

population = [21, 54, 87, 9, 51, 51, 15, 51, 71, 81, 6, 62, 26, 62, 32, 24, 40]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
plt.hist(population, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x_label')
plt.ylabel('y_label')
plt.title('Plot title')
plt.legend()
plt.show()
