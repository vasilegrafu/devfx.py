import numpy as np
import tensorflow as tf
from . import types
from . import tensors
from . import mathematics

"""------------------------------------------------------------------------------------------------
"""
def zeros_initializer(dtype=types.float32):
    return tf.zeros_initializer(dtype=dtype)

def ones_initializer(dtype=types.float32):
    return tf.ones_initializer(dtype=dtype)

def constant_initializer(value=0.0, dtype=types.float32):
    return tf.constant_initializer(value=value, dtype=dtype)

"""------------------------------------------------------------------------------------------------
"""
def random_uniform_initializer(min=0.0, max=None, dtype=types.float32, seed=None):
    return tf.random_uniform_initializer(minval=min, maxval=max, dtype=dtype, seed=seed)

def random_normal_initializer(mean=0.0, stddev=1.0, dtype=types.float32, seed=None):
    return tf.random_normal_initializer(mean=mean, stddev=stddev, dtype=dtype, seed=seed)

"""------------------------------------------------------------------------------------------------
"""
class XavierGlorotRandomUniformInitializer(object):
    def __init__(self, dtype=types.float32, seed=None):
        self.dtype = dtype
        self.seed = seed

    def __call__(self, shape, dtype=types.float32):
        if dtype is None:
            dtype = self.dtype
        r = types.cast(mathematics.sqrt(6.0 / (np.prod(shape[:-1]) + shape[-1])), dtype=dtype)
        return tensors.random_uniform(shape, min=-r, max=r, dtype=dtype, seed=self.seed)

    def get_config(self):
        return {"dtype": self.dtype.name,
                "seed": self.seed}
xavier_glorot_random_uniform_initializer = XavierGlorotRandomUniformInitializer


class XavierGlorotRandomNormalInitializer(object):
    def __init__(self, dtype=types.float32, seed=None):
        self.dtype = dtype
        self.seed = seed

    def __call__(self, shape, dtype=types.float32):
        if dtype is None:
            dtype = self.dtype
        mean = 0.0
        stddev = types.cast(mathematics.sqrt(2.0 / (np.prod(shape[:-1]) + shape[-1])), dtype=dtype)
        return tensors.random_normal(shape, mean=mean, stddev=stddev, dtype=dtype, seed=self.seed)

    def get_config(self):
        return {"dtype": self.dtype.name,
                "seed": self.seed}

xavier_glorot_random_normal_initializer = XavierGlorotRandomNormalInitializer


class XavierGlorotRandomTruncatedNormalInitializer(object):
    def __init__(self, dtype=types.float32, seed=None):
        self.dtype = dtype
        self.seed = seed

    def __call__(self, shape, dtype=types.float32):
        if dtype is None:
            dtype = self.dtype
        mean = 0.0
        stddev = types.cast(mathematics.sqrt(2.0/(np.prod(shape[:-1]) + shape[-1])), dtype=dtype)
        return tensors.random_truncated_normal(shape, mean=mean, stddev=stddev, dtype=dtype, seed=self.seed)

    def get_config(self):
        return {"dtype": self.dtype.name,
                "seed": self.seed}

xavier_glorot_random_truncated_normal_initializer = XavierGlorotRandomTruncatedNormalInitializer