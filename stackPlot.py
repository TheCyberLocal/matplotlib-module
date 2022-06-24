from matplotlib import pyplot as plt

steps = [1, 2, 3, 4, 5]

set1 = [1, 2, 3, 1, 3]
set2 = [1, 3, 3, 2, 3]
set3 = [1, 2, 3, 4, 2]
set4 = [1, 1, 3, 1, 3]

plt.plot([], [], color='m', label='type1', linewidth=5)
plt.plot([], [], color='c', label='type2', linewidth=5)
plt.plot([], [], color='r', label='type3', linewidth=5)
plt.plot([], [], color='k', label='type4', linewidth=5)

plt.stackplot(steps, set1, set2, set3, set4, colors=['m', 'c', 'r', 'k'])

plt.xlabel('x_label')
plt.ylabel('y_label')
plt.title('Plot title')
plt.legend()
plt.show()
