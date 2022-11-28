import numpy as np
import random as rnd
import devfx.exceptions as ex
import devfx.core as core
from .data import Data

class Action(object):
    def __init__(self, name, value, *args, **kwargs):
        self.__set_name(name=name)
        self.__set_data(data=Data(value, *args, **kwargs))

    """------------------------------------------------------------------------------------------------
    """
    def __set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    """------------------------------------------------------------------------------------------------
    """
    def __set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    """------------------------------------------------------------------------------------------------
    """
    def get_value(self):
        return self.get_data().get_value()

    """------------------------------------------------------------------------------------------------
    """
    def __str__(self):
        return '(' + str(self.get_name()) + ', ' + str(self.get_data()) + ')'   

    """------------------------------------------------------------------------------------------------
    """
    def __eq__(self, action):
        return (self.get_name() == action.get_name()) and (self.get_data() == action.get_data())

    def __hash__(self):
        return hash((self.get_name(), self.get_data()))
    
    """------------------------------------------------------------------------------------------------
    """
    def __setitem__(self, key, item):
        self.get_data()[key] = item

    def __getitem__(self, key):
        return self.get_data()[key]
