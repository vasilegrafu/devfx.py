import devfx.exceptions as excs
import devfx.core as core

class Reward(object):
    def __init__(self, value):
        self.__set_value(value=value)

    """------------------------------------------------------------------------------------------------
    """
    def __set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    """------------------------------------------------------------------------------------------------
    """
    def __str__(self):
        return str(self.get_value())

    """------------------------------------------------------------------------------------------------
    """
    def __eq__(self, reward):
        return self.get_value() == reward.get_value()

    def __hash__(self):
        return hash(self.get_value())
    
