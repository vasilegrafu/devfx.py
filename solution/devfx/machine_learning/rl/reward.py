import devfx.exceptions as excps
import devfx.core as core

class Reward(object):
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
    def __eq__(self, reward):
        if(not core.is_instance(reward, Reward)):
            raise excps.ArgumentError()

        return self.value == reward.value

    def __hash__(self):
        return hash(self.value)
    
