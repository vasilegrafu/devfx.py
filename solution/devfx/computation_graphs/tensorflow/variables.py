import tensorflow as tf
import devfx.exceptions as exceps
from . import types

"""------------------------------------------------------------------------------------------------
"""
def create_variable(shape, dtype=None, initializer=None, trainable=True, name=None):
    if(dtype is None):
        initial_value = initializer(shape=shape)
    else:
        initial_value = initializer(shape=shape, dtype=dtype)
    variable = tf.Variable(initial_value=initial_value, trainable=trainable, name=name)
    return variable

"""------------------------------------------------------------------------------------------------
"""
__persistent_variables_storage = {}
def create_persistent_variable(model, name, shape, dtype=None, initializer=None, trainable=True):
    if(id(model) not in __persistent_variables_storage):
        __persistent_variables_storage[id(model)] = {}
    if(name in __persistent_variables_storage[id(model)]):
        raise exceps.ArgumentError()
    __persistent_variables_storage[id(model)][name] = create_variable(shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, name=name)
    variable = __persistent_variables_storage[id(model)][name]
    return variable

def get_or_create_persistent_variable(model, name, shape, dtype=None, initializer=None, trainable=True):
    model_id = id(model)
    if(model_id not in __persistent_variables_storage):
        __persistent_variables_storage[model_id] = {}
    if(name not in __persistent_variables_storage[model_id]):
        __persistent_variables_storage[model_id][name] = create_variable(shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, name=name)
    variable = __persistent_variables_storage[model_id][name]
    return variable

def get_persistent_variable(model, name):
    if(id(model) not in __persistent_variables_storage):
        raise exceps.ArgumentError()
    if(name not in __persistent_variables_storage[id(model)]):
        raise exceps.ArgumentError()
    variable = __persistent_variables_storage[id(model)][name]
    return variable

def exists_persistent_variable(model, name):
    if(id(model) not in __persistent_variables_storage):
        raise exceps.ArgumentError()
    if(name in __persistent_variables_storage[id(model)]):
        return True
    else:
        return False

def remove_persistent_variable(model, name):
    if(id(model) not in __persistent_variables_storage):
        raise exceps.ArgumentError()
    del __persistent_variables_storage[id(model)][name]


def get_persistent_variables(model):
    if(id(model) not in __persistent_variables_storage):
        raise exceps.ArgumentError()
    return list(__persistent_variables_storage[id(model)].values())

def remove_persistent_variables(model):
    if(id(model) not in __persistent_variables_storage):
        raise exceps.ArgumentError()
    del __persistent_variables_storage[id(model)]
    
