import tensorflow as tf
import devfx.exceptions as exceps
from . import types

"""------------------------------------------------------------------------------------------------
"""
def __create_variable(name=None, shape=None, dtype=None, initializer=None, trainable=True):
    if((shape is None) and (dtype is None)):
        initial_value = initializer()
    elif((shape is None) and (dtype is not None)):
        initial_value = initializer(dtype=dtype)
    elif((shape is not None) and (dtype is None)):
        initial_value = initializer(shape=shape)
    elif((shape is not None) and (dtype is not None)):
        initial_value = initializer(shape=shape, dtype=dtype)
    else:
        raise exceps.NotSupportedError()
    variable = tf.Variable(name=name, initial_value=initial_value, trainable=trainable)
    return variable

"""------------------------------------------------------------------------------------------------
"""
__variables_storage = {}
__variables_storage['default'] = {}

def exists_variable(name, partition='default'):
    if(partition not in __variables_storage):
        raise exceps.ArgumentError()
    if(name in __variables_storage[partition]):
        return True
    else:
        return False


def create_variable(name, partition='default', shape=None, dtype=None, initializer=None, trainable=True):
    if(partition not in __variables_storage):
        __variables_storage[partition] = {}
    if(name in __variables_storage[partition]):
        raise exceps.ArgumentError()
    __variables_storage[partition][name] = __create_variable(name=f'{partition}__{name}', shape=shape, dtype=dtype, initializer=initializer, trainable=trainable)
    variable = __variables_storage[partition][name]
    return variable

def get_variable(name, partition='default'):
    if(partition not in __variables_storage):
        raise exceps.ArgumentError()
    if(name not in __variables_storage[partition]):
        raise exceps.ArgumentError()
    variable = __variables_storage[partition][name]
    return variable

def get_or_create_variable(name, partition='default', shape=None, dtype=None, initializer=None, trainable=True):
    if(exists_variable(name=name, partition=partition)):
        variable = get_variable(name=name, partition=partition)
        return variable
    else:
        variable = create_variable(name=name, partition=partition, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable)
        return variable

def remove_variable(name, partition='default'):
    if(partition not in __variables_storage):
        raise exceps.ArgumentError()
    del __variables_storage[partition][name]


def get_variables(partition='default'):
    if(partition not in __variables_storage):
        raise exceps.ArgumentError()
    return list(__variables_storage[partition].values())

def remove_variables(partition='default'):
    if(partition not in __variables_storage):
        raise exceps.ArgumentError()
    if(partition == 'default'):
        for name in  __variables_storage[partition]:
            del __variables_storage[partition][name]
    else:
        del __variables_storage[partition]
    
