import numpy as np

import numpy.linalg as alg
a = np.array([[1, 1, 1], [-1/3, 1, 0], [0, -1/3, 1]])
b = np.array([2970, 180, 130])
x = np.dot(alg.inv(a), b)
print("%4.0f р., %4.0f р., %4.0f р." % (x[0], x[1], x[2]))