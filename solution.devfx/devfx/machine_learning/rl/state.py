import numpy as np
import devfx.exceptions as exp
import devfx.core as core
from .state_kind import StateKind
from .data import Data

class State(object):
    def __init__(self, kind, value, *args, **kwargs):
        self.__set_kind(kind=kind)
        self.__set_data(data=Data(value, *args, **kwargs))

    """------------------------------------------------------------------------------------------------
    """
    def __set_kind(self, kind):
        self.__kind = kind

    def get_kind(self):
        return self.__kind
    
    def is_undefined(self):
        is_undefined = self.get_kind() == StateKind.UNDEFINED
        return is_undefined

    def is_non_terminal(self):
        is_non_terminal = self.get_kind() == StateKind.NON_TERMINAL
        return is_non_terminal

    def is_terminal(self):
        is_terminal = self.get_kind() == StateKind.TERMINAL
        return is_terminal

    """------------------------------------------------------------------------------------------------
    """
    def __set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
    
    """------------------------------------------------------------------------------------------------
    """
    def get_value(self):
        return self.get_data().get_value()

    def get_hash(self):
        return hash((self.get_name(), self.get_data()))
    
    """------------------------------------------------------------------------------------------------
    """
    def __str__(self):
        return '(' + str(self.get_kind()) + ', ' + str(self.get_data()) + ')'
    
    """------------------------------------------------------------------------------------------------
    """
    def __eq__(self, state):          
        return (self.get_kind() == state.get_kind()) and (self.get_data() == state.get_data())

    def __hash__(self):
        return hash((self.get_kind(), self.get_data()))
    
    """------------------------------------------------------------------------------------------------
    """
    def __setitem__(self, key, item):
        self.get_data()[key] = item

    def __getitem__(self, key):
        return self.get_data()[key]

    """------------------------------------------------------------------------------------------------
    """
    def copy(self):
        return State(kind=self.get_kind(), value=self.get_data().copy())


class UndefinedState(State):
    def __init__(self, *args, **kwargs):
        super().__init__(kind=StateKind.UNDEFINED, value=None, *args, **kwargs) 

class NonTerminalState(State):
    def __init__(self, value, *args, **kwargs):
        super().__init__(kind=StateKind.NON_TERMINAL, value=value, *args, **kwargs)

class TerminalState(State):
    def __init__(self, value, *args, **kwargs):
        super().__init__(kind=StateKind.TERMINAL, value=value, *args, **kwargs)