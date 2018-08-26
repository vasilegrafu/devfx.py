import tensorflow as tf

def conv1d(input, # [batch, in_width, in_channels]
           filter, # [filter_width, in_channels, out_channels]
           strides=(1, 1, 1),
           padding='valid',
           name=None):
    output = tf.nn.conv1d(value=input,
                          filters=filter,
                          stride=strides,
                          padding=padding,
                          data_format='NWC',
                          name=name)
    return output # [batch, out_width, out_channels]
