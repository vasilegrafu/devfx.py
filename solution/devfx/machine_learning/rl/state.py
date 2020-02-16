import devfx.exceptions as exps
import devfx.core as core
from .state_kind import StateKind

class State(object):
    def __init__(self, value, state_kind=StateKind.NON_TERMINAL):
        self.__set_value(value=value)
        self.__set_state_kind(state_kind=state_kind)

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
    def __eq__(self, state):
        if(state is None):
            return False
        if(not core.is_instance(state, State)):
            raise exps.ArgumentError()
        return state.value == self.value

    def __hash__(self):
        return hash(self.value)

    """------------------------------------------------------------------------------------------------
    """ 
    def __set_state_kind(self, state_kind):
        self.__state_kind = state_kind

    @property
    def kind(self):
        return self.__state_kind

    def is_non_terminal(self):
        return self.kind == StateKind.NON_TERMINAL

    def is_terminal(self):
        return self.kind == StateKind.TERMINAL
  
    