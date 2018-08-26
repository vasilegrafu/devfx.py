import tensorflow as tf
import devfx.exceptions as exceptions
from . import execution
from . import types
from . import scopes
from . import devices


"""------------------------------------------------------------------------------------------------
"""
def Variable(dtype=types.float32, initial_value=None, expected_shape=None, validate_shape=True, name=None, trainable=True, device=None):
    if(execution.is_declarative_execution_mode_enabled()):
        if(device is None):
            variable = tf.Variable(initial_value=initial_value, dtype=dtype, expected_shape=expected_shape, validate_shape=validate_shape, name=name, trainable=trainable)
            return variable
        else:
            with devices.device(device):
                variable = tf.Variable(initial_value=initial_value, dtype=dtype, expected_shape=expected_shape, validate_shape=True, name=name, trainable=trainable)
                return variable
    elif(execution.is_imperative_execution_mode_enabled()):
        if (device is None):
            variable = tf.contrib.eager.Variable(initial_value=initial_value, dtype=dtype, validate_shape=validate_shape, name=name, trainable=trainable)
            return variable
        else:
            with devices.device(device):
                variable = tf.contrib.eager.Variable(initial_value=initial_value, dtype=dtype, validate_shape=True, name=name, trainable=trainable)
                return variable
    else:
        raise exceptions.NotSupportedError()

"""------------------------------------------------------------------------------------------------
"""
__imperative_execution_mode_variables_storage = {}

def create_variable(name, shape=None, dtype=types.float32, initializer=None, trainable=True, validate_shape=True, device=None):
    if(execution.is_declarative_execution_mode_enabled()):
        with scopes.scope(scopes.get_scope(), variables_reuse=False):
            if (device is None):
                variable = tf.get_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape)
                return variable
            else:
                with devices.device(device):
                    variable = tf.get_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape)
                    return variable
    elif(execution.is_imperative_execution_mode_enabled()):
        full_name = scopes.get_scope().name + '/' + name
        if (full_name in __imperative_execution_mode_variables_storage):
            raise exceptions.ArgumentError()
        if (device is None):
            variable = tf.get_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape)
            __imperative_execution_mode_variables_storage[full_name] = variable
            return variable
        else:
            with devices.device(device):
                variable = tf.get_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape)
                __imperative_execution_mode_variables_storage[full_name] = variable
                return variable
    else:
        raise exceptions.NotSupportedError()

def get_variable(name, shape=None, dtype=types.float32, initializer=None, trainable=True, validate_shape=True, device=None):
    if(execution.is_declarative_execution_mode_enabled()):
        with scopes.scope(scopes.get_scope(), variables_reuse=True):
            if (device is None):
                variable = tf.get_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape)
                return variable
            else:
                with devices.device(device):
                    variable = tf.get_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape)
                    return variable
    elif(execution.is_imperative_execution_mode_enabled()):
        full_name = scopes.get_scope().name + '/' + name
        if (not full_name in __imperative_execution_mode_variables_storage):
            raise exceptions.ArgumentError()
        variable = __imperative_execution_mode_variables_storage[full_name]
        return variable
    else:
        raise exceptions.NotSupportedError()

def create_or_get_variable(name, shape=None, dtype=types.float32, initializer=None, trainable=True, validate_shape=True, device=None):
    if(execution.is_declarative_execution_mode_enabled()):
        with scopes.scope(scopes.get_scope(), variables_reuse=tf.AUTO_REUSE):
            if (device is None):
                variable = tf.get_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape)
                return variable
            else:
                with devices.device(device):
                    variable = tf.get_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape)
                    return variable
    elif(execution.is_imperative_execution_mode_enabled()):
        full_name = scopes.get_scope().name + '/' + name
        if (not full_name in __imperative_execution_mode_variables_storage):
            variable = create_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape, device=device)
            return variable
        else:
            variable = get_variable(name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, validate_shape=validate_shape, device=device)
            return variable
    else:
        raise exceptions.NotSupportedError()

"""------------------------------------------------------------------------------------------------
"""
def global_variables_initializer():
    return tf.global_variables_initializer()