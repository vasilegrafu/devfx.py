import numpy as np
import devfx.exceptions as excps
import devfx.core as core
from .data import Data

class State(object):
    def __init__(self, kind, object, *args, **kwargs):
        self.__set_kind(kind=kind)
        self.__set_data(data=Data(object, *args, **kwargs))


    """------------------------------------------------------------------------------------------------
    """
    def __set_kind(self, kind):
        self.__kind = kind

    @property
    def kind(self):
        return self.__kind


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
        return '(' + str(self.kind) + ', ' + str(self.data) + ')'

    """------------------------------------------------------------------------------------------------
    """
    def __eq__(self, state):          
        if(not core.is_instance(state, State)):
            raise excps.ArgumentError()    

        return self.kind == state.kind and self.data == state.data

    def __hash__(self):
        return hash((self.kind, self.data))

    """------------------------------------------------------------------------------------------------
    """
    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]