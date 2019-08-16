import numpy as np

x = np.array([1, 2])
y = np.array([1, 2])

A = np.vstack([x, np.ones(len(x))]).T

m = np.linalg.lstsq(A, y)
print(m)