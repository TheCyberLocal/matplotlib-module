from matplotlib import pyplot as plt, style

style.use('ggplot')

x = [2, 4, 6, 8]
y = [7, 3, 8, 3]

x2 = [1, 3, 5, 7]
y2 = [2, 9, 0.5, 4]

plt.bar(x, y, color='b', label="line1", width=0.5)
plt.bar(x2, y2, color='r', label="line2", width=0.25)

plt.title("CHART TITLE")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.legend()

plt.show()
