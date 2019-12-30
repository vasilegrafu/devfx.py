import tensorflow as tf
from . import max_poolNd

def max_pool3d(name,
               input,
               kernel_size=(2, 2, 2),
               strides=(2, 2, 2),
               padding='VALID',
               data_format='NDHWC'):
    """
    :param name: string
    :param input: (batch, in_depth, in_height, in_width, in_channels) or (batch, in_channels, in_depth, in_height, in_width)
    :param kernel_size: (dd, dh, dw)
    :param strides: (dd, dh, dw)
    :param padding: 'VALID' or 'SAME'
    :param data_format: 'NDHWC' or 'NCDHW'
    :return: (batch, out_depth, out_height, out_width, out_channels) or (batch, out_channels, out_depth, out_height, out_width)
    """

    pool = max_poolNd.max_pool(name=name,
                               input=input,
                               kernel_size=kernel_size,
                               strides=strides,
                               padding=padding,
                               data_format=data_format)

    output = pool

    return output 
