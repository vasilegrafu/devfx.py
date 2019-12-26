import numpy as np
from .. import tensors

def linearize(input):
    input_shape = tuple(input.shape)
    M = input_shape[0]
    n = np.prod(input_shape[1:])
    output = tensors.reshape(input, [M, n])
    return output