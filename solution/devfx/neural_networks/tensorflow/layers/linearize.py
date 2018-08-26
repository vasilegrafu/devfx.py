import numpy as np
import devfx.computation_graphs.tensorflow as cg

def linearize(input):
    input_shape = tuple([_.value for _ in input.shape])
    M = input_shape[0]
    n = np.prod(input_shape[1:])
    output = cg.reshape(input, [M, n])
    return output