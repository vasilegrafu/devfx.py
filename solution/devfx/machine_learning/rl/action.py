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

    def __get_name(self):
        return self.__name

    @property
    def name(self):
        return self.__get_name()

    """------------------------------------------------------------------------------------------------
    """
    def __set_data(self, data):
        self.__data = data

    def __get_data(self):
        return self.__data

    @property
    def data(self):
        return self.__get_data()
    
    """------------------------------------------------------------------------------------------------
    """
    @property
    def value(self):
        return self.__get_data().value

    """------------------------------------------------------------------------------------------------
    """
    def __str__(self):
        return '(' + str(self.__get_name()) + ', ' + str(self.__get_data()) + ')'   

    """------------------------------------------------------------------------------------------------
    """
    def __eq__(self, action):
        if(not core.is_instance(action, Action)):
            raise ex.ArgumentError()  

        return (self.__get_name() == action.__get_name()) and (self.__get_data() == action.__get_data())

    def __hash__(self):
        return hash(self.__get_data())
    
    """------------------------------------------------------------------------------------------------
    """
    def __setitem__(self, key, item):
        self.__get_data()[key] = item

    def __getitem__(self, key):
        return self.__get_data()[key]
