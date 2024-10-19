import random as rnd
import devfx.exceptions as exp

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
    def get_sav_iterator(self):
        states1 = self.get_model()[1].get_states()
        states2 = self.get_model()[2].get_states()
        states = [state for state in states1 if state in states2]
        for state in states:
            actions1 = self.get_model()[1].get_actions(state=state)
            actions2 = self.get_model()[2].get_actions(state=state)
            actions = [action for action in actions1 if action in actions2]
            for action in actions:
                value1 = self.get_model()[1].get_value(state=state, action=action)
                value2 = self.get_model()[2].get_value(state=state, action=action)
                value = (value1 + value2)/2.0
                yield (state, action, value)

    """------------------------------------------------------------------------------------------------
    """ 
    def _learn(self, transitions):
        raise exp.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """
    def _get_max_action(self, state):
        is_terminal_state = state.is_terminal()
        if(is_terminal_state):
            return None

        model1 = self.get_model()[1]
        model2 = self.get_model()[2]

        if(not model1.has_state(state=state)):
            return None
        if(not model1.has_actions(state=state)):
            return None
        if(not model2.has_state(state=state)):
            return None
        if(not model2.has_actions(state=state)):
            return None

        actions1 = model1.get_actions(state=state)
        actions2 = model2.get_actions(state=state)
        actions = [action for action in actions1 if action in actions2]
        if(len(actions) == 0):
            return None

        action = max(actions, key=lambda action: (model1.get_value(state=state, action=action) + model2.get_value(state=state, action=action))/2.0)
        return action

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_action(self, state):
        is_terminal_state = state.is_terminal()
        if(is_terminal_state):
            return None

        model1 = self.get_model()[1]
        model2 = self.get_model()[2]

        actions1 = model1.get_actions(state=state)
        actions2 = model2.get_actions(state=state)
        actions = [action for action in actions1 if action in actions2]
        if(len(actions) == 0):
            return None

        random_action = rnd.choice(actions)
        return random_action

                


