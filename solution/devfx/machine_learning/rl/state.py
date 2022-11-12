import numpy as np
import devfx.exceptions as excps
import devfx.core as core
import devfx.data_structures as ds

class State(object):
    def __init__(self, value, kind):
        self.__set_value(value=value)
        self.__set_kind(kind=kind)

    """------------------------------------------------------------------------------------------------
    """
    def __set_value(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    """------------------------------------------------------------------------------------------------
    """
    def __set_kind(self, kind):
        self.__kind = kind

    @property
    def kind(self):
        return self.__kind



    """------------------------------------------------------------------------------------------------
    """
    def __str__(self):
        return '(' + str(self.value) + ', ' + str(self.kind) + ')'

    """------------------------------------------------------------------------------------------------
    """
    def __eq__(self, state):          
        if(not core.is_instance(state, State)):
            raise excps.ArgumentError()    

        return ds.comparable(self.value) == ds.comparable(state.value) and self.kind == state.kind

    def __hash__(self):
        return hash((ds.comparable(self.value), self.kind))

