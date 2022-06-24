from matplotlib import pyplot as plt, style

'''
pre-coded colors:
white:w
red:r
yellow:y
blue:b
green:g
cyan:c
magenta:m
black:k
circle:o
square:s
pentagon:p
hexagons:h
diamonds:d
vector:v upside_down triangle
x_mark:x

red, blue, green, yellow...
color='#hex_color'
'''

# style.use [ggplot, grayscale, dark_background]
# plt.grid(True)

style.use('ggplot')


x = []
y = []
x2 = []
y2 = []

plt.plot(x, y, 'k', linewidth=1, label="line1")
plt.plot(x2, y2, 'y', linewidth=1, label="line2")

plt.scatter(x, y, color='g', label="dot1", marker='h', s=20)
plt.scatter(x2, y2, color='b', label="dot2", marker='*', s=50)

plt.bar(x, y, color='b', label="line1", width=0.5)
plt.bar(x2, y2, color='r', label="line2", width=0.25)

population = [21, 54, 87, 9, 51, 51, 15, 51, 71, 81, 6, 62, 26, 62, 32, 24, 40]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
plt.hist(population, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x_label')
plt.ylabel('y_label')
plt.title('Plot title')
plt.legend()
plt.show()
