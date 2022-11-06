import tensorflow as tf

"""------------------------------------------------------------------------------------------------
"""
def constant_initializer(value=0):
    return tf.initializers.constant(value=value)

def zeros_initializer():
    return tf.initializers.zeros()

def ones_initializer():
    return tf.initializers.ones()

"""------------------------------------------------------------------------------------------------
"""
def identity_initializer(gain=1.0):
    return tf.initializers.identity(gain=gain)

"""------------------------------------------------------------------------------------------------
"""
def random_uniform_initializer(minval=-1e-8, maxval=+1e-8, seed=None):
    return tf.initializers.RandomUniform(minval=minval, maxval=maxval, seed=seed)

def random_normal_initializer(mean=0.0, stddev=1e-8, seed=None):
    return tf.initializers.RandomNormal(mean=mean, stddev=stddev, seed=seed)

def random_truncated_normal_initializer(mean=0.0, stddev=1e-8, seed=None):
    return tf.initializers.TruncatedNormal(mean=mean, stddev=stddev, seed=seed)

"""------------------------------------------------------------------------------------------------
"""
def random_glorot_uniform_initializer(seed=None):
    return tf.initializers.GlorotUniform(seed=seed)

def random_glorot_normal_initializer(seed=None):
    return tf.initializers.GlorotNormal(seed=seed)


