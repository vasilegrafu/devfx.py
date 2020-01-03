from .. import variables
from .. import initializers
from .. import math
from . import normalization

def dense(name,
          input,
          n,
          initializer=None,
          activation_fn=None,
          normalize_input=False,
          normalize_z=False,
          normalize_output=False):

    if(initializer is None):
        initializer = initializers.random_glorot_normal_initializer()

    if (activation_fn is None):
        activation_fn = lambda x : x

    if(normalize_input):
        input = normalization.normalize(name=f'{name}__dense__normalize_input', input=input)

    w = variables.create_or_get_variable(name=f'{name}__dense__w', shape=[n, *input.shape[1:]], dtype=input.dtype, initializer=initializer)
    b = variables.create_or_get_variable(name=f'{name}__dense__b', shape=[n], dtype=input.dtype, initializer=initializer)
    
    axes_1 = list(range(len(input.shape))[1:])
    axes_2 = list(range(len(w.shape))[1:])
    z = math.tensordot(input, w, axes=(axes_1, axes_2)) + b

    if(normalize_z):
        z = normalization.normalize(name=f'{name}__dense__normalize_z', input=z)

    output = activation_fn(z)

    if(normalize_output):
        output = normalization.normalize(name=f'{name}__dense__normalize_output', input=output)

    return output