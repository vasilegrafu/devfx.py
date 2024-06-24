import random as rnd
import devfx.exceptions as excs

from .policy import Policy
from .tabular_model import TabularModel

class TabularPolicy(Policy):
    def __init__(self):
        super().__init__()
  
    """------------------------------------------------------------------------------------------------
    """ 
    def _setup_model(self):
        self.__model = TabularModel()
   
    def _get_model(self):
        return self.__model
  
    """------------------------------------------------------------------------------------------------
    """
    def get_sav_iterator(self):
        return self.get_model().get_sav_iterator()

    """------------------------------------------------------------------------------------------------
    """ 
    def _learn(self, transitions):
        raise ex.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """
    def _get_max_action(self, state):
        is_terminal_state = state.is_terminal()
        if(is_terminal_state):
            return None
    
        action = self.get_model().get_max_action(state=state)
        return action

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_action(self, state):
        is_terminal_state = state.is_terminal()
        if(is_terminal_state):
            return None

        random_action = self.get_model().get_random_action(state=state)
        return random_action

                


