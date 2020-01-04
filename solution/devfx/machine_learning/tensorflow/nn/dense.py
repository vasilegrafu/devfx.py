from .. import variables
from .. import initialization
from .. import math
from . import normalization

"""------------------------------------------------------------------------------------------------
"""
def dense(name,
          input,
          n,
          initializer=None,
          activation_fn=None,
          input_normalizer=None,
          z_normalizer=None,
          output_normalizer=None):

    name = name + '__dense'

    if(initializer is None):
        initializer = initialization.random_glorot_normal_initializer()

    if (activation_fn is None):
        activation_fn = lambda x : x

    if(input_normalizer is not None):
        input = input_normalizer(name=f'{name}__normalize_input', input=input)

    w = variables.create_or_get_variable(name=f'{name}__w', shape=[n, *input.shape[1:]], dtype=input.dtype, initializer=initializer)
    b = variables.create_or_get_variable(name=f'{name}__b', shape=[n], dtype=input.dtype, initializer=initializer)
    
    axes_1 = list(range(len(input.shape))[1:])
    axes_2 = list(range(len(w.shape))[1:])
    z = math.tensordot(input, w, axes=(axes_1, axes_2)) + b

    if(z_normalizer is not None):
        z = z_normalizer(name=f'{name}__normalize_z', input=z)

    output = activation_fn(z)

    if(output_normalizer is not None):
        output = output_normalizer(name=f'{name}__normalize_output', input=output)

    return output