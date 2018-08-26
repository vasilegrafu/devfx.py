import numpy as np

def one_hot(n, index):
    z = np.zeros(n, dtype=np.int32)
    z[index] = 1
    return z