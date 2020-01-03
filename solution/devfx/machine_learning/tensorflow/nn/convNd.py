import tensorflow as tf
import devfx.exceptions as exceps
import devfx.core as core
from .. import initializers
from .. import variables
from . import normalization

def conv(name,
         input,
         filters_n, 
         kernel_size,
         strides=None,
         padding=None,
         data_format=None,  
         kernel_initializer=None,
         bias_initializer=None,
         activation_fn=None,
         normalize_input=False,
         normalize_z=False,
         normalize_output=False):

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

    if(normalize_input):
        input = normalization.normalize(name=f'{name}__convNd__normalize_input', input=input)
    
    w = variables.create_or_get_variable(name=f'{name}__convNd__w', 
                                         shape=(*kernel_size, input.shape[1 if data_format.startswith("NC") else len(input.shape) - 1], filters_n), 
                                         dtype=input.dtype, 
                                         initializer=kernel_initializer)
    
    conv = tf.nn.convolution(input=input, 
                             filters=w, 
                             strides=strides, 
                             padding=padding,
                             data_format=data_format,
                             name=f'{name}__convNd') 

    b = variables.create_or_get_variable(name=f'{name}__convNd__b', 
                                         shape=(filters_n,), 
                                         dtype=input.dtype, 
                                         initializer=bias_initializer)

    z = conv + b

    if(normalize_z):
        z = normalization.normalize(name=f'{name}__convNd__normalize_z', input=z)

    output = activation_fn(z)

    if(normalize_output):
        output = normalization.normalize(name=f'{name}__convNd__normalize_output', input=output)

    return output 





