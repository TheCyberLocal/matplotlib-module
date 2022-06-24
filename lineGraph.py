from matplotlib import pyplot as plt, style

style.use('ggplot')
# plt.grid(True)

x = [5, 6, 7, 8]
y = [7, 3, 8, 3]

y2 = [2, 9, 0, 4]

plt.plot(x, y, 'k', linewidth=1, label="line1")
plt.plot(x, y2, 'y', linewidth=1, label="line2")

plt.title("CHART TITLE")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.legend()

plt.show()
