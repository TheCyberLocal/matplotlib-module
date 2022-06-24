from matplotlib import pyplot as plt, style

style.use('ggplot')

x = [5, 6, 7, 8]
y = [7, 3, 8, 3]

x2 = [5, 6, 7, 8]
y2 = [2, 9, 0, 4]

plt.scatter(x, y, color='g', label="dot1", marker='h', s=20)
plt.scatter(x2, y2, color='b', label="dot2", marker='*', s=50)

plt.title("CHART TITLE")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.legend()

plt.show()
