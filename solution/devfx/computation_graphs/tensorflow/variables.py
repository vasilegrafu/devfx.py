import tensorflow as tf
import devfx.exceptions as exceptions
from . import execution
from . import types
from . import scopes

"""------------------------------------------------------------------------------------------------
"""
def Variable(name=None, dtype=types.float32, initial_value=None, validate_shape=True, trainable=True):
    if(execution.is_declarative_execution_mode_enabled()):
        variable = tf.Variable(initial_value=initial_value, dtype=dtype, validate_shape=validate_shape, name=name, trainable=trainable)
        return variable
    elif(execution.is_imperative_execution_mode_enabled()):
        variable = tf.contrib.eager.Variable(initial_value=initial_value, dtype=dtype, validate_shape=validate_shape, name=name, trainable=trainable)
        return variable
    else:
        raise exceptions.NotSupportedError()

"""------------------------------------------------------------------------------------------------
"""
eagerVariableStore = tf.contrib.eager.EagerVariableStore()

def create_variable(name, shape=None, dtype=types.float32, initializer=None, trainable=True, validate_shape=True):
    if(execution.is_declarative_execution_mode_enabled()):
        with scopes.scope(scopes.get_scope(), variables_reuse=False):
            variable = tf.get_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape)
            return variable
    elif(execution.is_imperative_execution_mode_enabled()):
        with eagerVariableStore.as_default():
            with scopes.scope(scopes.get_scope(), variables_reuse=False):
                variable = tf.get_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape)
                return variable
    else:
        raise exceptions.NotSupportedError()

def get_variable(name, shape=None, dtype=types.float32, initializer=None, trainable=True, validate_shape=True):
    if(execution.is_declarative_execution_mode_enabled()):
        with scopes.scope(scopes.get_scope(), variables_reuse=True):
            variable = tf.get_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape)
            return variable
    elif(execution.is_imperative_execution_mode_enabled()):
        with eagerVariableStore.as_default():
            with scopes.scope(scopes.get_scope(), variables_reuse=True):
                variable = tf.get_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape)
                return variable
    else:
        raise exceptions.NotSupportedError()

def create_or_get_variable(name, shape=None, dtype=types.float32, initializer=None, trainable=True, validate_shape=True):
    if(execution.is_declarative_execution_mode_enabled()):
        with scopes.scope(scopes.get_scope(), variables_reuse=tf.AUTO_REUSE):
            variable = tf.get_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape)
            return variable
    elif(execution.is_imperative_execution_mode_enabled()):
        with eagerVariableStore.as_default():
            with scopes.scope(scopes.get_scope(), variables_reuse=tf.AUTO_REUSE):
                variable = tf.get_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape)
                return variable
    else:
        raise exceptions.NotSupportedError()

"""------------------------------------------------------------------------------------------------
"""
def global_variables_initializer():
    return tf.global_variables_initializer()