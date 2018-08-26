import numpy as np

x = np.arange(8, dtype = np.int8)

print("x ->\n", x)
print("x.strides ->", x.strides)

x.shape = (2, 4)

print("x ->\n", x)
print("x.strides ->", x.strides)