import tensorflow as tf
import devfx.exceptions as exceps
from . import types

"""------------------------------------------------------------------------------------------------
"""
def Variable(name=None, initial_value=None, dtype=types.float32, validate_shape=True, trainable=True):
    variable = tf.Variable(initial_value=initial_value, trainable=trainable, validate_shape=validate_shape, name=name, dtype=dtype)
    return variable

