import devfx.exceptions as ex
import devfx.core as core

class Reward(object):
    def __init__(self, value):
        self.__set_value(value=value)

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
    def __eq__(self, reward):
        if(not core.is_instance(reward, Reward)):
            raise ex.ArgumentError()

        return self.__get_value() == reward.__get_value()

    def __hash__(self):
        return hash(self.__get_value())
    
