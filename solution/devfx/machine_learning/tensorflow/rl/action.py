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
    def __eq__(self, state):
        if(not core.is_instance(state, Action)):
            raise exps.ArgumentError()
        return state.value == self.value

    def __hash__(self):
        return hash(self.value)
    
