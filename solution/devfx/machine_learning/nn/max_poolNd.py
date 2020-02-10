import tensorflow as tf
import devfx.exceptions as exps
import devfx.core as core

"""------------------------------------------------------------------------------------------------
"""
def max_poolNd(name,
               input,
               kernel_size,
               strides=None,
               padding=None,
               data_format=None):
    name = name + '__max_poolNd'

    if (not 3 <= len(input.shape) <= 5):
        raise exps.ArgumentError()
    N = len(input.shape) - 2

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


    pool = tf.nn.max_pool(input=input,
                          ksize=kernel_size,
                          strides=strides,
                          padding=padding,
                          data_format=data_format,
                          name=f'{name}')

    output = pool

    return pool