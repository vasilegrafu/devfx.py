import tensorflow as tf
import devfx.exceptions as exps
import devfx.core as core
from .. import initialization
from ..sl import variables

"""------------------------------------------------------------------------------------------------
"""
def convNd(name,
           input,
           filters_n, 
           kernel_size,
           strides=None,
           padding=None,
           data_format=None,  
           kernel_initializer=None,
           bias_initializer=None,
           activation_fn=None,
           input_normalizer=None,
           z_normalizer=None,
           output_normalizer=None):

    name = name + '__convNd'

    if (not 3 <= len(input.shape) <= 5):
        raise exps.ArgumentError()
    N = len(input.shape) - 2

    if(not core.is_typeof(filters_n, int)):
        raise exps.ArgumentError()

    if(not core.is_iterable(kernel_size)):
        raise exps.ArgumentError()
    if(not len(kernel_size) == N):
        raise exps.ArgumentError()

    if(strides is None):
        strides = tuple([1]*N)
    if(not core.is_iterable(strides)):
        raise exps.ArgumentError()
    if(not len(strides) == N):
        raise exps.ArgumentError()
        
    if(padding is None):
        padding = 'VALID'
    if(padding != 'VALID' and padding != 'SAME'):
        raise exps.ArgumentError()

    if (data_format is None and len(input.shape) == 3):
        data_format = 'NWC'
    if (data_format is None and len(input.shape) == 4):
        data_format = 'NHWC'
    if (data_format is None and len(input.shape) == 5):
        data_format = 'NDHWC'
    if(len(data_format) != len(input.shape)):
        raise exps.ArgumentError()
    if(len(input.shape) == 3 and (data_format != 'NWC' and data_format != 'NCW')):
        raise exps.ArgumentError()
    if(len(input.shape) == 4 and (data_format != 'NHWC' and data_format != 'NCHW')):
        raise exps.ArgumentError()
    if(len(input.shape) == 5 and (data_format != 'NDHWC' and data_format != 'NCDHW')):
        raise exps.ArgumentError()
    
    if(kernel_initializer is None):
        kernel_initializer = initialization.random_glorot_normal_initializer()

    if(bias_initializer is None):
        bias_initializer = initialization.random_glorot_normal_initializer()

    if (activation_fn is None):
        activation_fn = lambda x : x

    if(input_normalizer is not None):
        input = input_normalizer(name=f'{name}__normalize_input', input=input)
    
    w = variables.create_or_get_variable(name=f'{name}__w', 
                                         shape=(*kernel_size, input.shape[1 if data_format.startswith("NC") else len(input.shape) - 1], filters_n), 
                                         dtype=input.dtype, 
                                         initializer=kernel_initializer)
    
    conv = tf.nn.convolution(input=input, 
                             filters=w, 
                             strides=strides, 
                             padding=padding,
                             data_format=data_format,
                             name=f'{name}') 

    b = variables.create_or_get_variable(name=f'{name}__b', 
                                         shape=(filters_n,), 
                                         dtype=input.dtype, 
                                         initializer=bias_initializer)

    z = conv + b

    if(z_normalizer is not None):
        z = z_normalizer(name=f'{name}__normalize_z', input=z)

    output = activation_fn(z)

    if(output_normalizer is not None):
        output = output_normalizer(name=f'{name}__normalize_output', input=output)

    return output 





