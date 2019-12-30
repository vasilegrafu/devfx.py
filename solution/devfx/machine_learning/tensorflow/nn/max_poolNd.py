import tensorflow as tf
import devfx.exceptions as exceps
import devfx.core as core

def max_pool(name,
             input,
             kernel_size,
             strides=None,
             padding=None,
             data_format=None):

    if (not 3 <= len(input.shape) <= 5):
        raise exceps.ArgumentError()
    N = len(input.shape) - 2

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


    pool = tf.nn.max_pool(input=input,
                          ksize=kernel_size,
                          strides=strides,
                          padding=padding,
                          data_format=data_format,
                          name=f'{name}__max_pool')

    output = pool

    return pool