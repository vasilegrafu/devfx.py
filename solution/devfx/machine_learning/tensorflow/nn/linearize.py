import numpy as np
from .. import tensors

def linearize(input):
    M = input.shape[0]
    n = np.prod(input.shape[1:])
    output = tensors.reshape(input, [M, n])
    return output