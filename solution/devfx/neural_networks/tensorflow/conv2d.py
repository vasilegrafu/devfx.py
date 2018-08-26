import tensorflow as tf

def conv2d(input, # [batch, in_height, in_width, in_channels]
           filter, # [filter_height, filter_width, in_channels, out_channels]
           strides=(1, 1, 1, 1),
           padding='valid',
           name=None):
    output = tf.nn.conv2d(input=input,
                          filter=filter,
                          strides=strides,
                          padding=padding,
                          data_format='NHWC',
                          name=name)
    return output # [batch, out_height, out_width, out_channels]





