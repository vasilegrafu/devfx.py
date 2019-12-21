import tensorflow as tf
from .. import types
from .. import initializers
from .. import variables

def conv2d(name,
           input,
           filters,
           kernel_size,
           strides=(1, 1, 1, 1),
           padding=[[0, 0], [0, 0], [0, 0], [0, 0]],
           data_format='NHWC',  
           dtype=types.float32,
           kernel_initializer=None,
           bias_initializer=None,
           activation_fn=None):

    if(kernel_initializer is None):
        kernel_initializer = initializers.random_glorot_normal_initializer()

    if(bias_initializer is None):
        bias_initializer = initializers.random_glorot_normal_initializer()

    if (activation_fn is None):
        activation_fn = lambda x : x
    
    input_shape = tuple(input.shape)
    w_shape = (kernel_size[0], kernel_size[1], input_shape[3], filters)
    b_shape = (input_shape[3], filters)

    w = variables.create_or_get_variable(name=f'{name}_w', shape=w_shape, dtype=dtype, initializer=kernel_initializer)
    b = variables.create_or_get_variable(name=f'{name}_b', shape=b_shape, dtype=dtype, initializer=bias_initializer)

    filters = w + b

    # [batch, out_height, out_width, out_channels]
    z = tf.nn.conv2d(input=input,  # [batch, in_height, in_width, in_channels]
                     filters=filters, # [filter_height, filter_width, in_channels, out_channels]
                     strides=strides, 
                     padding=padding,
                     data_format=data_format)

    output = activation_fn(z)

    return output 





