import tensorflow as tf
import devfx.machine_learning.tensorflow as ml

def max_poolingNd(N,
                  name,
                  input,
                  pool_size,
                  strides,
                  padding):
    with cg.scope(name):
        if(N == 1):
            max_pooling_fn = tf.layers.max_pooling1d
        elif(N == 2):
            max_pooling_fn = tf.layers.max_pooling2d
        elif(N == 3):
            max_pooling_fn = tf.layers.max_pooling3d
        else:
            raise NotImplementedError()

        pool = max_pooling_fn(inputs=input,
                              pool_size=pool_size,
                              strides=strides,
                              padding=padding)
        return pool