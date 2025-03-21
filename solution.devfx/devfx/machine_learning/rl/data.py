import numpy as np
import hashlib as hlib
import random as rnd
import devfx.exceptions as exp
import devfx.core as core

class Data(object):
    def __init__(self, value, *args, **kwargs):
        self.__setup_value(value, *args, **kwargs)
        self.__calculate_hash()

    """------------------------------------------------------------------------------------------------
    """
    def __setup_value(self, value, *args, **kwargs):
        match value:
            case Data():
                self.__value = value.value.copy()
            case np.ndarray():
                self.__value = value.copy()
            case list():
                self.__value = np.array(value, *args, **kwargs)           
            case tuple():
                self.__value = np.array(value, *args, **kwargs)  
            case _:
                raise exp.NotSupportedError()      

    def get_value(self):
        return self.__value

    """------------------------------------------------------------------------------------------------
    """
    def __calculate_hash(self):
        self.__hash = int(hlib.md5(self.get_value().view(np.uint8)).hexdigest(), 16)

    """------------------------------------------------------------------------------------------------
    """
    def __str__(self):
        return str(self.get_value())

    """------------------------------------------------------------------------------------------------
    """
    def __eq__(self, data):
        return np.equal(self.get_value(), data.get_value()).all()
    
    def __hash__(self):
        return self.__hash

    """------------------------------------------------------------------------------------------------
    """
    def __setitem__(self, key, item):
        self.get_value()[key] = item
        self.__calculate_hash()

    def __getitem__(self, key):
        return self.get_value()[key]

    """------------------------------------------------------------------------------------------------
    """
    def copy(self):
        return Data(value=self.get_value().copy())