from matplotlib import pyplot as plt
import numpy as np


x, y = np.loadtxt(r'filepath',
                  unpack=True,
                  delimiter=',')

plt.plot(x, y, label='loaded from file')

plt.show()
