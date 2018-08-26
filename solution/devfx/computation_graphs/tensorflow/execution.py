import tensorflow as tf
import devfx.exceptions as exceptions

"""------------------------------------------------------------------------------------------------
"""
def enable_declarative_execution_mode():
    raise exceptions.NotSupportedError()

def enable_imperative_execution_mode():
    tf.enable_eager_execution()

"""------------------------------------------------------------------------------------------------
"""
def is_declarative_execution_mode_enabled():
    return not tf.executing_eagerly()

def is_imperative_execution_mode_enabled():
    return tf.executing_eagerly()