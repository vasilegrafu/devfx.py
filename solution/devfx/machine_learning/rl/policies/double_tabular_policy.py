import random as rnd
import devfx.exceptions as ex

from .policy import Policy
from .tabular_model import TabularModel

class DoubleTabularPolicy(Policy):
    def __init__(self):
        super().__init__()
  
    """------------------------------------------------------------------------------------------------
    """ 
    def _setup_model(self):
        self.__model = { 1 : TabularModel(), 2 : TabularModel() }
   
    def _get_model(self):
        return self.__model

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
    
        action_values1 = self.get_model()[1].get_action_values_or_none(state)
        action_values2 = self.get_model()[2].get_action_values_or_none(state)

        if((action_values1 is None) or (action_values2 is None)):
            return None
        
        actions = action_values1.keys() & action_values2.keys()

        action = max(actions, key=lambda action: action_values1[action] + action_values2[action])
        return action

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_action(self, state):
        random_action = rnd.choice(self.get_model().get_actions(state=state))
        return random_action

                


