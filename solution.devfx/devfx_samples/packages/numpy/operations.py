import numpy as np

x = np.arange(8, dtype = np.int8)
print("x ->", x)

x = np.append(x, [7, 6, 5, 4, 3, 2, 1, 0])
print("x ->", x)

x = np.delete(x, [10])
print("x ->", x)

x = np.insert(x, [10], [10])
print("x ->", x)

i = np.searchsorted(x, 2)
print("i ->", i)
x = np.insert(x, [i], [10])
print("x ->", x)

x = x[np.argsort(x)]
print("x ->", x)


a = np.array([1, 2, 3, 4])
for index, x in np.ndenumerate(a):
    print(index[0], x)

a = np.array([[1, 2], [3, 4]])
for index, x in np.ndenumerate(a):
    print(index, x)