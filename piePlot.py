from matplotlib import pyplot as plt

slices = [7, 2, 1, 11]
types = ['type1', 'type2', 'type3', 'type4']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=types,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')

plt.title('Plot title')
plt.show()
