from .. import variables
from .. import initializers
from .. import math

def dense(name,
          input,
          n,
          dtype=None,
          initializer=None,
          normalizer=None,
          activation_fn=None):

    # parameters
    if(initializer is None):
        initializer = initializers.random_glorot_normal_initializer()

    if(normalizer is None):
        normalizer = lambda x : x

    if (activation_fn is None):
        activation_fn = lambda x : x

    # algorithm
    input_shape = tuple(input.shape)
    input_m = input_shape[0]
    input_item_shape = input_shape[1:]

    w_shape = [n, *input_item_shape]
    b_shape = [n]

    w = variables.create_or_get_variable(name=f'{name}_w', shape=w_shape, dtype=dtype, initializer=initializer)
    b = variables.create_or_get_variable(name=f'{name}_b', shape=b_shape, dtype=dtype, initializer=initializer)

    # z: mj,ij->mi + b
    axes_1 = list(range(len(input_shape))[1:])
    axes_2 = list(range(len(w_shape))[1:])
    z = math.tensordot(input, w, axes=(axes_1, axes_2)) + b

    z = normalizer(z)

    output = activation_fn(z)

    return output