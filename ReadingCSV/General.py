#Reading CSV Files

import numpy as np

data = np.genfromtxt('Downloads/IPL Sample CSV/Team.csv', delimiter=',', skip_header=1)
print(data)