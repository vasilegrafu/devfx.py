import numpy as np
import devfx.exceptions as excps
import devfx.core as core

class State(object):
    def __init__(self, value, kind):
        self.__set_value(value=value)
        self.__set_kind(kind=kind)

    """------------------------------------------------------------------------------------------------
    """
    def __set_value(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    """------------------------------------------------------------------------------------------------
    """
    def __set_kind(self, kind):
        self.__kind = kind

    @property
    def kind(self):
        return self.__kind

    """------------------------------------------------------------------------------------------------
    """
    def __str__(self):
        return '(' + str(self.value) + ', ' + str(self.kind) + ')'

    """------------------------------------------------------------------------------------------------
    """
    def __eq__(self, state):
        if(state is None):
            return False

        if(not core.is_instance(state, State)):
            raise excps.ArgumentError()

        if(core.is_typeof(self.value, np.array) or core.is_typeof(state.value, np.array)):
            if(core.is_typeof(self.value, np.array) and core.is_typeof(state.value, np.array)):
                return self.value.array_equal(state.value) and state.kind == self.kind
            else:
                raise excps.ArgumentError()        

        return state.value == self.value and state.kind == self.kind

    def __hash__(self):
        return hash((self.value, self.kind))


    