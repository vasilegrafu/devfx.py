import numpy as np
import random as rnd
import devfx.exceptions as excps
import devfx.core as core

"""================================================================================================
"""
class Action(object):
    def __init__(self, name, value):
        self.__set_name(name=name)
        self.__set_value(value=value)

    """------------------------------------------------------------------------------------------------
    """
    def __set_name(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


    """------------------------------------------------------------------------------------------------
    """
    def __set_value(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value


    """------------------------------------------------------------------------------------------------
    """
    def __str__(self):
        return '(' + str(self.name) + ', ' + str(self.value) + ')'

    """------------------------------------------------------------------------------------------------
    """
    def __eq__(self, action):
        if(action is None):
            return False

        if(not core.is_instance(action, Action)):
            raise excps.ArgumentError()

        if(core.is_typeof(self.value, np.array) or core.is_typeof(action.value, np.array)):
            if(core.is_typeof(self.value, np.array) and core.is_typeof(action.value, np.array)):
                return action.name == self.name and self.value.array_equal(action.value)
            else:
                raise excps.ArgumentError()      

        return action.name == self.name and action.value == self.value

    def __hash__(self):
        return hash((self.name, self.value))
    

"""================================================================================================
"""
class DiscreteActionValuesGenerator(object):
    def __init__(self, name, values):
        self.__set_name(name=name)
        self.__set_values(values=values)

    """------------------------------------------------------------------------------------------------
    """
    def __set_name(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


    """------------------------------------------------------------------------------------------------
    """
    def __set_values(self, values):
        self.__values = values

    @property
    def values(self):
        return self.__values


    """------------------------------------------------------------------------------------------------
    """
    def get_random(self):
        value = rnd.choice(self.values)
        return value


"""================================================================================================
"""
class ContinousActionValuesGenerator(object):
    def __init__(self, name, values):
        self.__set_name(name=name)
        self.__set_values(values=values)

    """------------------------------------------------------------------------------------------------
    """
    def __set_name(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


    """------------------------------------------------------------------------------------------------
    """
    def __set_values(self, values):
        self.__values = values

    @property
    def values(self):
        return self.__values


    """------------------------------------------------------------------------------------------------
    """
    def get_random(self):
        value = rnd.uniform(self.values)
        return value
    
