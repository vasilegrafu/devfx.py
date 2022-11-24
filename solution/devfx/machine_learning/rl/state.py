import numpy as np
import devfx.exceptions as ex
import devfx.core as core
from .data import Data

class State(object):
    def __init__(self, kind, value, *args, **kwargs):
        self.__set_kind(kind=kind)
        self.__set_data(data=Data(value, *args, **kwargs))

    """------------------------------------------------------------------------------------------------
    """
    def __set_kind(self, kind):
        self.__kind = kind

    def __get_kind(self):
        return self.__kind

    @property
    def kind(self):
        return self.__get_kind()

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
        return '(' + str(self.__get_kind()) + ', ' + str(self.__get_data()) + ')'
    
    """------------------------------------------------------------------------------------------------
    """
    def __eq__(self, state):          
        if(not core.is_instance(state, State)):
            raise ex.ArgumentError()    

        return (self.__get_kind() == state.__get_kind()) and (self.__get_data() == state.__get_data())

    def __hash__(self):
        return hash((self.__get_kind(), self.__get_data()))
    
    """------------------------------------------------------------------------------------------------
    """
    def __setitem__(self, key, item):
        self.__get_data()[key] = item

    def __getitem__(self, key):
        return self.__get_data()[key]