import numpy as np
import hashlib as hlib
import random as rnd
import devfx.exceptions as ex
import devfx.core as core

"""================================================================================================
"""
class Data(object):
    def __init__(self, value, *args, **kwargs):
        if(core.is_instance(value, Data)):
            self.__set_value(value=value.value)
        elif(core.is_instance(value, np.ndarray)):
            self.__set_value(value=value)
        else:
            self.__set_value(value=np.array(value, *args, **kwargs))

        self.__hash = int(hlib.md5(self.value.view(np.uint8)).hexdigest(), 16)

    """------------------------------------------------------------------------------------------------
    """
    def __set_value(self, value):
        self.__value = value

    def __get_value(self):
        return self.__value

    @property
    def value(self):
        return self.__get_value()

    """------------------------------------------------------------------------------------------------
    """
    def __str__(self):
        return str(self.__get_value())

    """------------------------------------------------------------------------------------------------
    """
    def __eq__(self, data):
        if(not core.is_instance(data, Data)):
            raise ex.ArgumentError()  

        return np.equal(self.__get_value(), data.__get_value()).all()
    
    def __hash__(self):
        return self.__hash

    """------------------------------------------------------------------------------------------------
    """
    def __setitem__(self, key, item):
        self.__get_value()[key] = item

    def __getitem__(self, key):
        return self.__get_value()[key]