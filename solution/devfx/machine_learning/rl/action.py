import numpy as np
import random as rnd
import devfx.exceptions as excps
import devfx.core as core
import devfx.data_structures as ds

"""================================================================================================
"""
class Action(object):
    def __init__(self, value):
        self.__set_value(value=value)


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
        return str(self.value)

    """------------------------------------------------------------------------------------------------
    """
    def __eq__(self, action):
        if(not core.is_instance(action, Action)):
            raise excps.ArgumentError()  

        return ds.comparable(self.value) == ds.comparable(action.value)

    def __hash__(self):
        return hash(ds.comparable(self.value))
    

