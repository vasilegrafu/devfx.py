import tensorflow as tf

def conv3d(input, # [batch, in_depth, in_height, in_width, in_channels]
           filter, # [filter_depth, filter_height, filter_width, in_channels, out_channels]
           strides=(1, 1, 1, 1, 1),
           padding='valid',
           name=None):
    output = tf.nn.conv3d(input=input,
                          filter=filter,
                          strides=strides,
                          padding=padding,
                          data_format='NDHWC',
                          name=name)
    return output # [batch, out_depth, out_height, out_width, out_channels]

