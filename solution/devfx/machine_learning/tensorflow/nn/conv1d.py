from .convNd import convNd

"""------------------------------------------------------------------------------------------------
"""
def conv1d(name,
           input, 
           filters_n, 
           kernel_size, 
           strides=(1,),
           padding='VALID', 
           data_format='NWC', 
           kernel_initializer=None,
           bias_initializer=None,
           activation_fn=None,
           input_normalizer=None,
           z_normalizer=None,
           output_normalizer=None): 
    """
    :param name: string
    :param filters_n: number
    :param input: (batch, in_width, in_channels) or (batch, in_channels, in_width)
    :param kernel_size: (dw,)
    :param strides: (dw,)
    :param kernel_initializer: initializer
    :param bias_initializer: initializer
    :param padding: 'VALID' or 'SAME'
    :param data_format: 'NWC' or 'NCW'
    :return: (batch, out_width, out_channels) or (batch, out_channels, out_width)
    """

    conv = convNd(name=name,
                  input=input,
                  filters_n=filters_n,
                  kernel_size=kernel_size,
                  strides=strides,
                  padding=padding,
                  data_format=data_format,  
                  kernel_initializer=kernel_initializer,
                  bias_initializer=bias_initializer,
                  activation_fn=activation_fn,
                  input_normalizer=input_normalizer,
                  z_normalizer=z_normalizer,
                  output_normalizer=output_normalizer)

    output = conv

    return output 