import numpy as np
import random as rnd
import devfx.exceptions as excps
import devfx.core as core
from .data import Data

"""================================================================================================
"""
class Action(object):
    def __init__(self, name, value, *args, **kwargs):
        self.__set_name(name=name)
        self.__set_data(data=Data(value, *args, **kwargs))

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

    def __get_data(self):
        return self.__data

    @property
    def value(self):
        return self.__get_data().value

    """------------------------------------------------------------------------------------------------
    """
    def __str__(self):
        return str(self.data)

    """------------------------------------------------------------------------------------------------
    """
    def __eq__(self, action):
        if(not core.is_instance(action, Action)):
            raise excps.ArgumentError()  

        return self.name == action.name and self.__get_data() == action.__get_data()

    def __hash__(self):
        return hash(self.__get_data())
    
    """------------------------------------------------------------------------------------------------
    """
    def __setitem__(self, key, value):
        self.__get_data()[key] = value

    def __getitem__(self, key):
        return self.__get_data()[key]
