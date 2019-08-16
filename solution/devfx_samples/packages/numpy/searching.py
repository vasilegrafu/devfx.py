import numpy as np

print("----------------------------------------------------------------")
print("Search sorted")
print("----------------------------------------------------------------")
a = np.array([2, 4, 6, 8, 10])

i = np.searchsorted(a, 1)
print(i)

i = np.searchsorted(a, 2)
print(i)

i = np.searchsorted(a, 3)
print(i)

i = np.searchsorted(a, 10)
print(i)

i = np.searchsorted(a, 11)
print(i)