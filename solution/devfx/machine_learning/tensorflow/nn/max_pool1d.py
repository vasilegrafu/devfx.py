import tensorflow as tf
from .max_poolNd import max_poolNd

"""------------------------------------------------------------------------------------------------
"""
def max_pool1d(name,
               input,
               kernel_size=(2,),
               strides=(2,),
               padding='VALID',
               data_format='NWC'):
    """
    :param name: string
    :param input: (batch, in_width, in_channels) or (batch, in_channels, in_width)
    :param kernel_size: (dw,)
    :param strides: (dw,)
    :param padding: 'VALID' or 'SAME'
    :param data_format: 'NWC' or 'NCW'
    :return: (batch, out_width, out_channels) or (batch, out_channels, out_width)
    """

    pool = max_poolNd(name=name,
                      input=input,
                      kernel_size=kernel_size,
                      strides=strides,
                      padding=padding,
                      data_format=data_format)

    output = pool

    return output 
