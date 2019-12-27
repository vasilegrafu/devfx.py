import tensorflow as tf
import devfx.exceptions as exceps
import devfx.core as core
from .. import initializers
from .. import variables

def conv(name,
         input,
         filters_n, 
         kernel_size,
         strides=None,
         padding=None,
         data_format=None,  
         kernel_initializer=None,
         bias_initializer=None,
         activation_fn=None):

    if (not 3 <= len(input.shape) <= 5):
        raise exceps.ArgumentError()
    N = len(input.shape) - 2

    if(not core.is_typeof(filters_n, int)):
        raise exceps.ArgumentError()

    if(not core.is_iterable(kernel_size)):
        raise exceps.ArgumentError()
    if(not len(kernel_size) == N):
        raise exceps.ArgumentError()

    if(strides is None):
        strides = tuple([1]*N)
    if(not core.is_iterable(strides)):
        raise exceps.ArgumentError()
    if(not len(strides) == N):
        raise exceps.ArgumentError()
        
    if(padding is None):
        padding = 'VALID'
    if(padding != 'VALID' and padding != 'SAME'):
        raise exceps.ArgumentError()

    if (data_format is None and len(input.shape) == 3):
        data_format = 'NWC'
    if (data_format is None and len(input.shape) == 4):
        data_format = 'NHWC'
    if (data_format is None and len(input.shape) == 5):
        data_format = 'NDHWC'
    if(len(data_format) != len(input.shape)):
        raise exceps.ArgumentError()
    if(len(input.shape) == 3 and (data_format != 'NWC' and data_format != 'NCW')):
        raise exceps.ArgumentError()
    if(len(input.shape) == 4 and (data_format != 'NHWC' and data_format != 'NCHW')):
        raise exceps.ArgumentError()
    if(len(input.shape) == 5 and (data_format != 'NDHWC' and data_format != 'NCDHW')):
        raise exceps.ArgumentError()
    
    if(kernel_initializer is None):
        kernel_initializer = initializers.random_glorot_normal_initializer()

    if(bias_initializer is None):
        bias_initializer = initializers.random_glorot_normal_initializer()

    if (activation_fn is None):
        activation_fn = lambda x : x
    
    weights = variables.create_or_get_variable(name=f'{name}__weights', 
                                               shape=(*kernel_size, input.shape[1 if data_format.startswith("NC") else len(input.shape) - 1], filters_n), 
                                               dtype=input.dtype, 
                                               initializer=kernel_initializer)
    
    convolution = tf.nn.convolution(input=input, 
                                    filters=weights, 
                                    strides=strides, 
                                    padding=padding,
                                    data_format=data_format,
                                    name=f'{name}__convolution') 

    bias = variables.create_or_get_variable(name=f'{name}__bias', 
                                         shape=(filters_n,), 
                                         dtype=input.dtype, 
                                         initializer=bias_initializer)

    z = convolution + bias

    output = activation_fn(z)

    return output 





