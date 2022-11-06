from .max_poolNd import max_poolNd

"""------------------------------------------------------------------------------------------------
"""
def max_pool2d(name,
               input,
               kernel_size=(2, 2),
               strides=(2, 2),
               padding='VALID',
               data_format='NHWC'):
    """
    :param name: string
    :param input: (batch, in_height, in_width, in_channels) or (batch, in_channels, in_height, in_width)
    :param kernel_size: (dh, dw)
    :param strides: (dh, dw)
    :param padding: 'VALID' or 'SAME'
    :param data_format: 'NHWC' or 'NCHW'
    :return: (batch, out_height, out_width, out_channels) or (batch, out_channels, out_height, out_width)
    """

    pool = max_poolNd(name=name,
                      input=input,
                      kernel_size=kernel_size,
                      strides=strides,
                      padding=padding,
                      data_format=data_format)

    output = pool

    return output 
