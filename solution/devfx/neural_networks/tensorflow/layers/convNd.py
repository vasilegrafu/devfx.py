import tensorflow as tf
import devfx.computation_graphs.tensorflow as cg
from .. import initialization

def convNd(N,
           name,
           input,
           filters,
           kernel_size,
           strides,
           padding,
           kernel_initializer=None,
           bias_initializer=None,
           normalizer=None,
           activation_fn=None):
    with cg.scope(name):
        # parameters
        if(kernel_initializer is None):
            kernel_initializer = initialization.xavier_glorot_random_truncated_normal_initializer(dtype=input.dtype)

        if(bias_initializer is None):
            bias_initializer = initialization.zeros_initializer(dtype=input.dtype)

        if(normalizer is None):
            normalizer = lambda x : x

        if (activation_fn is None):
            activation_fn = lambda x : x

        # algorithm
        if(N == 1):
            conv_fn = tf.layers.conv1d
        elif(N == 2):
            conv_fn = tf.layers.conv2d
        elif(N == 3):
            conv_fn = tf.layers.conv3d
        else:
            raise NotImplementedError()

        z = conv_fn(inputs=input,
                    filters=filters,
                    kernel_size=kernel_size,
                    strides=strides,
                    padding=padding,
                    activation=activation_fn,
                    kernel_initializer=kernel_initializer,
                    bias_initializer=bias_initializer)

        z = normalizer(z)

        output = activation_fn(z)

        return output




