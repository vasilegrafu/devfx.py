import tensorflow as tf
import inspect as insp
import devfx.exceptions as exceps
import devfx.core as core
from . import initializers
from .model import Model

"""------------------------------------------------------------------------------------------------
"""
def __create_variable(name=None, shape=None, dtype=None, initializer=None, trainable=True):
    if(initializer is None):
        initializer = initializers.zeros_initializer()

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
def __exists_variable(model, name):
    if(not core.hasattr(object=model, name=name)):
        return False
    value = core.getattr(object=model, name=name)
    if(not core.is_instance(value, tf.Variable)):
        return False
    return True

def __set_variable(model, name, variable):
    if(not core.is_instance(variable, tf.Variable)):
        raise exceps.ArgumentError()
    core.setattr(object=model, name=name, value=variable)

def __get_variable(model, name):
    if(not __exists_variable(model=model, name=name)):
        raise exceps.ArgumentError()
    variable = core.getattr(object=model, name=name)
    if(not core.is_instance(variable, tf.Variable)):
        raise exceps.ArgumentError()
    return variable

def __remove_variable(model, name):
    if(not __exists_variable(model=model, name=name)):
        raise exceps.ArgumentError()
    core.delattr(object=model, name=name)

"""------------------------------------------------------------------------------------------------
"""
def create_variable(name, shape=None, dtype=None, initializer=None, trainable=True, model=None):
    if(model is None):
        model = Model.current_model()
    variable = __create_variable(name=f'{name}', shape=shape, dtype=dtype, initializer=initializer, trainable=trainable)
    if(model is not None):
        __set_variable(model=model, name=name, variable=variable)
    return variable

def get_variable(name, model=None):
    if(model is None):
        model = Model.current_model()
    if(model is None):
        raise exceps.ApplicationError()
    return __get_variable(model=model, name=name)

def get_or_create_variable(name, shape=None, dtype=None, initializer=None, trainable=True, model=None):
    if(model is None):
        model = Model.current_model()
    if(model is None):
        raise exceps.ApplicationError()
    if(__exists_variable(model=model, name=name)):
        variable = __get_variable(model=model, name=name)
        return variable
    else:
        variable = __create_variable(name=name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable)
        __set_variable(model=model, name=name, variable=variable)
        return variable

def create_or_get_variable(name, shape=None, dtype=None, initializer=None, trainable=True, model=None):
    return get_or_create_variable(name=name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, model=model)

def set_variable(name, variable, model=None):
    if(model is None):
        model = Model.current_model()
    if(model is None):
        raise exceps.ApplicationError()
    return __set_variable(model=model, name=name, variable=variable)

def exists_variable(name, model=None):
    if(model is None):
        model = Model.current_model()
    if(model is None):
        raise exceps.ApplicationError()
    return __exists_variable(model=model, name=name)

def remove_variable(name, model=None):
    if(model is None):
        model = Model.current_model()
    if(model is None):
        raise exceps.ApplicationError()
    return __remove_variable(model=model, name=name)


"""------------------------------------------------------------------------------------------------
"""
def get_all_variables(model=None):
    if(model is None):
        model = Model.current_model()
    if(model is None):
        raise exceps.ApplicationError()
    return model.variables

def get_trainable_variables(model=None):
    if(model is None):
        model = Model.current_model()
    if(model is None):
        raise exceps.ApplicationError()
    return model.trainable_variables
    
