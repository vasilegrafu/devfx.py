from .. import variables
from .. import initializers
from .. import math

def dense(name,
          input,
          n,
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
    input_item_shape = input.shape[1:]

    w_shape = [n, *input.shape[1:]]
    b_shape = [n]

    w = variables.create_or_get_variable(name=f'{name}__w', shape=w_shape, dtype=input.dtype, initializer=initializer)
    b = variables.create_or_get_variable(name=f'{name}__b', shape=b_shape, dtype=input.dtype, initializer=initializer)

    # z: mj,ij->mi + b
    axes_1 = list(range(len(input.shape))[1:])
    axes_2 = list(range(len(w_shape))[1:])
    z = math.tensordot(input, w, axes=(axes_1, axes_2)) + b

    z = normalizer(z)

    output = activation_fn(z)

    return output