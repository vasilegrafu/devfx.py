import numpy as np
import hashlib as hlib
import devfx.exceptions as excps
import devfx.core as core

class comparable(object):
    def __init__(self, value):
        self.__set_value(value)

    """------------------------------------------------------------------------------------------------
    """
    def __set_value(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    """------------------------------------------------------------------------------------------------
    """
    def __eq__(self, comparable):
        if(core.is_instance(self.value, np.ndarray) or core.is_instance(comparable.value, np.ndarray)):
            if(core.is_instance(self.value, np.ndarray) and core.is_instance(comparable.value, np.ndarray)):
                return np.array_equal(self.value, comparable.value)
            else:
                raise excps.ArgumentError()        
        else:
            return self.value == comparable.value

    def __hash__(self):
        if(core.is_instance(self.value, np.ndarray)):
            return int(hlib.sha1(self.value.view(np.uint8)).hexdigest(), 16)
        else:
            try:
                return hash(self.value)
            except:
                pass




