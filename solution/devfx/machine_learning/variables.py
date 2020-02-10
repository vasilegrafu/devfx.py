import tensorflow as tf
import devfx.exceptions as exps
from . import initialization

"""------------------------------------------------------------------------------------------------
"""
def create_variable(name=None, shape=None, dtype=None, initializer=None, trainable=True):
    if(initializer is None):
        initializer = initialization.zeros_initializer()

    if((shape is None) and (dtype is None)):
        initial_value = initializer()
    elif((shape is None) and (dtype is not None)):
        initial_value = initializer(dtype=dtype)
    elif((shape is not None) and (dtype is None)):
        initial_value = initializer(shape=shape)
    elif((shape is not None) and (dtype is not None)):
        initial_value = initializer(shape=shape, dtype=dtype)
    else:
        raise exps.NotSupportedError()
    
    variable = tf.Variable(name=name, initial_value=initial_value, trainable=trainable)
    return variable


