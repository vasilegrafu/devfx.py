import tensorflow as tf
import devfx.exceptions as exceps
import devfx.core as core

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
def exists_variable(model, name):
    if(not core.hasattr(object=model, name=name)):
        return False
    value = core.getattr(object=model, name=name)
    if(not core.is_instance(value, tf.Variable)):
        return False
    return True

def set_variable(model, name, variable):
    if(exists_variable(model=model, name=name)):
        raise exceps.ArgumentError()
    if(not core.is_instance(variable, tf.Variable)):
        raise exceps.ArgumentError()
    core.setattr(object=model, name=name, value=variable)

def get_variable(model, name):
    if(not exists_variable(model=model, name=name)):
        raise exceps.ArgumentError()
    variable = core.getattr(object=model, name=name)
    return variable

def remove_variable(model, name):
    if(not exists_variable(model=model, name=name)):
        raise exceps.ArgumentError()
    core.delattr(object=model, name=name)


def create_variable(model, name, shape=None, dtype=None, initializer=None, trainable=True):
    if(exists_variable(model=model, name=name)):
        raise exceps.ArgumentError()
    variable = __create_variable(name=f'{id(model)}__{name}', shape=shape, dtype=dtype, initializer=initializer, trainable=trainable)
    set_variable(model=model, name=name, variable=variable)
    return variable


def get_or_create_variable(model, name, shape=None, dtype=None, initializer=None, trainable=True):
    if(exists_variable(model=model, name=name)):
        variable = get_variable(model=model, name=name)
        return variable
    else:
        variable = create_variable(model=model, name=name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable)
        return variable

def create_or_get_variable(model, name, shape=None, dtype=None, initializer=None, trainable=True):
    return get_or_create_variable(model=model, name=name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable)


"""------------------------------------------------------------------------------------------------
"""
def get_variables(model):
    return model.variables

def get_trainable_variables(model):
    return model.trainable_variables
    
