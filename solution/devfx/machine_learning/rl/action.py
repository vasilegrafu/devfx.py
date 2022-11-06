import devfx.exceptions as excps
import devfx.core as core

class Action(object):
    def __init__(self, value, duration):
        self.__set_value(value=value)
        self.__set_duration(duration=duration)

    """------------------------------------------------------------------------------------------------
    """
    def __set_value(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    
    """------------------------------------------------------------------------------------------------
    """
    def __set_duration(self, duration):
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration


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
            raise excps.ArgumentError()
        return (action.value == self.value) and (action.duration == self.duration)

    def __hash__(self):
        return hash((self.value, self.duration))
    
