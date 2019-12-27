import tensorflow as tf

def max_pool(name,
             input,
             kernel_size=(1, 2, 2, 1),
             strides=(1, 2, 2, 1)):
    pool = tf.nn.max_pool(input=input,
                            ksize=kernel_size,
                            strides=strides,
                            padding='VALID',
                            data_format='NHWC',
                            name=f'{name}__max_pool2d')

    return pool