import tensorflow as tf
import devfx.exceptions as excps
import devfx.core as core
from .. import variables
from .model import Model

"""------------------------------------------------------------------------------------------------
"""
def __exists_variable(model, name):
    if(not core.hasattr(obj=model, name=name)):
        return False
    value = core.getattr(obj=model, name=name)
    if(not core.is_instance(value, tf.Variable)):
        return False
    return True

def __set_variable(model, name, variable):
    if(not core.is_instance(variable, tf.Variable)):
        raise excps.ArgumentError()
    core.setattr(obj=model, name=name, value=variable)

def __get_variable(model, name):
    if(not __exists_variable(model=model, name=name)):
        raise excps.ArgumentError()
    variable = core.getattr(obj=model, name=name)
    if(not core.is_instance(variable, tf.Variable)):
        raise excps.ArgumentError()
    return variable

def __remove_variable(model, name):
    if(not __exists_variable(model=model, name=name)):
        raise excps.ArgumentError()
    core.delattr(obj=model, name=name)

"""------------------------------------------------------------------------------------------------
"""
def create_variable(name, shape=None, dtype=None, initializer=None, trainable=True, model=None):
    if(model is None):
        model = Model.current_model()
    variable = variables.create_variable(name=f'{name}', shape=shape, dtype=dtype, initializer=initializer, trainable=trainable)
    if(model is not None):
        __set_variable(model=model, name=name, variable=variable)
    return variable

def get_variable(name, model=None):
    if(model is None):
        model = Model.current_model()
    if(model is None):
        raise excps.ApplicationError()
    return __get_variable(model=model, name=name)

def get_or_create_variable(name, shape=None, dtype=None, initializer=None, trainable=True, model=None):
    if(model is None):
        model = Model.current_model()
    if(model is None):
        raise excps.ApplicationError()
    if(__exists_variable(model=model, name=name)):
        variable = __get_variable(model=model, name=name)
        return variable
    else:
        variable = variables.create_variable(name=name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable)
        __set_variable(model=model, name=name, variable=variable)
        return variable

def create_or_get_variable(name, shape=None, dtype=None, initializer=None, trainable=True, model=None):
    return get_or_create_variable(name=name, shape=shape, dtype=dtype, initializer=initializer, trainable=trainable, model=model)

def set_variable(name, variable, model=None):
    if(model is None):
        model = Model.current_model()
    if(model is None):
        raise excps.ApplicationError()
    return __set_variable(model=model, name=name, variable=variable)

def exists_variable(name, model=None):
    if(model is None):
        model = Model.current_model()
    if(model is None):
        raise excps.ApplicationError()
    return __exists_variable(model=model, name=name)

def remove_variable(name, model=None):
    if(model is None):
        model = Model.current_model()
    if(model is None):
        raise excps.ApplicationError()
    return __remove_variable(model=model, name=name)


"""------------------------------------------------------------------------------------------------
"""
def get_all_variables(model=None):
    if(model is None):
        model = Model.current_model()
    if(model is None):
        raise excps.ApplicationError()
    return model.variables

def get_trainable_variables(model=None):
    if(model is None):
        model = Model.current_model()
    if(model is None):
        raise excps.ApplicationError()
    return model.trainable_variables
    
