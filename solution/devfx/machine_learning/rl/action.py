import devfx.exceptions as exps
import devfx.core as core

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
        if(action is None):
            return False
        if(not core.is_instance(action, Action)):
            raise exps.ArgumentError()
        return action.value == self.value

    def __hash__(self):
        return hash(self.value)
    
