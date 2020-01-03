from . import convNd

def conv2d(name,
           input, 
           filters_n, 
           kernel_size, 
           strides=(1, 1), 
           padding='VALID', 
           data_format='NHWC', 
           kernel_initializer=None,
           bias_initializer=None,
           activation_fn=None,
           normalize_input=False,
           normalize_z=False,
           normalize_output=False): 
    """
    :param name: string
    :param filters_n: number
    :param input: (batch, in_height, in_width, in_channels) or (batch, in_channels, in_height, in_width)
    :param kernel_size: (dh, dw)
    :param strides: (dh, dw)
    :param kernel_initializer: initializer
    :param bias_initializer: initializer
    :param padding: 'VALID' or 'SAME'
    :param data_format: 'NHWC' or 'NCHW'
    :return: (batch, out_height, out_width, out_channels) or (batch, out_channels, out_height, out_width)
    """

    conv = convNd.conv(name=name,
                       input=input,
                       filters_n=filters_n,
                       kernel_size=kernel_size,
                       strides=strides,
                       padding=padding,
                       data_format=data_format,  
                       kernel_initializer=kernel_initializer,
                       bias_initializer=bias_initializer,
                       activation_fn=activation_fn,
                       normalize_input=normalize_input,
                       normalize_z=normalize_z,
                       normalize_output=normalize_output)

    output = conv

    return output 




