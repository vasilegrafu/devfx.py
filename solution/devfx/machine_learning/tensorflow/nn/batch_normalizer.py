from .. import types
from .. import variables
from .. import initializers
from .. import math

class BatchNormalizer(object):
    def __init__(self, name, is_training):
        self.name = name
        self.is_training = is_training

    def __call__(self, z):
        mean = math.reduce_mean(z, axis=0)
        var = math.reduce_var(z, axis=0)
        zn = (z - mean)/math.sqrt(var + 1e-8)

        gamma = variables.create_or_get_variable(name=f'{self.name}_gamma', shape=(), dtype=types.float32, initializer=initializers.ones_initializer())
        beta = variables.create_or_get_variable(name=f'{self.name}_beta', shape=(), dtype=types.float32, initializer=initializers.zeros_initializer())

        z_shape = tuple(input.shape)
        z_M = z_shape[0]
        z_ema_shape = z_shape[1:]
        z_ema = variables.create_or_get_variable(name=f'{self.name}_ema', shape=z_ema_shape, dtype=types.float32, initializer=initializers.zeros_initializer(), trainable=false)
        z_ema.assign(z_ema*)
         
        zr = gamma*zn + beta
        return zr

batch_normalizer = BatchNormalizer