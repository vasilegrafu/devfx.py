import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

p = np.random.permutation(np.arange(0, len(a)))
print(p)
print(a[p])

print(a[0:len(a):1])
print(a[...])

