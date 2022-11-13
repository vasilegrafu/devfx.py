import numpy as np
import random as rnd
import devfx.exceptions as excps
import devfx.core as core
from .data import Data

"""================================================================================================
"""
class Action(object):
    def __init__(self, name, object, *args, **kwargs):
        self.__set_name(name=name)
        self.__set_data(data=Data(object, *args, **kwargs))

    """------------------------------------------------------------------------------------------------
    """
    def __set_name(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    """------------------------------------------------------------------------------------------------
    """
    def __set_data(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @property
    def value(self):
        return self.data.value

    """------------------------------------------------------------------------------------------------
    """
    def __str__(self):
        return str(self.data)

    """------------------------------------------------------------------------------------------------
    """
    def __eq__(self, action):
        if(not core.is_instance(action, Action)):
            raise excps.ArgumentError()  

        return self.name == action.name and self.data == action.data

    def __hash__(self):
        return hash(self.data)
    
    """------------------------------------------------------------------------------------------------
    """
    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]
