from . import conv

def conv2d(name,
           input, # [batch, in_width, in_channels] or [batch, in_channels, in_width]
           filters_n, # number
           kernel_size, # (dw, )
           strides=(1,),
           padding='VALID', # 'VALID' or 'SAME'
           data_format='NWC', # 'NWC' or 'NCW'
           kernel_initializer=None,
           bias_initializer=None,
           activation_fn=None): # [batch, out_width, out_channels] or [batch, out_channels, out_width]

    convolution = conv.conv(name=name,
                            input=input,
                            filters_n=filters_n,
                            kernel_size=kernel_size,
                            strides=strides,
                            padding=padding,
                            data_format=data_format,  
                            kernel_initializer=kernel_initializer,
                            bias_initializer=bias_initializer,
                            activation_fn=activation_fn)

    output = convolution

    return output 
