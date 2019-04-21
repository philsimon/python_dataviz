import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
 
x = [21,21, 2, 4, 4, 4, 2]
num_bins = 200
n, bins, patches = plt.hist(x, num_bins, facecolor='red', alpha=1)
plt.show()