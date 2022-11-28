import devfx.exceptions as ex

from .tabular_policy import TabularPolicy
from ..state_kind import StateKind

class QLearningPolicy(TabularPolicy):
    def __init__(self, discount_factor, learning_rate):
        super().__init__()

        self.set_discount_factor(discount_factor=discount_factor)
        self.set_learning_rate(learning_rate=learning_rate)

    """------------------------------------------------------------------------------------------------
    """ 
    def set_discount_factor(self, discount_factor):
        self.__discount_factor = discount_factor

    def get_discount_factor(self):
        return self.__discount_factor

    """------------------------------------------------------------------------------------------------
    """ 
    def set_learning_rate(self, learning_rate):
        self.__learning_rate = learning_rate

    def get_learning_rate(self):
        return self.__learning_rate

    """------------------------------------------------------------------------------------------------
    """
    def _learn(self, transitions):
        for transition in transitions:
            (state, action, (reward, next_state)) = transition

            if(not super().has_value(state, action)):
                super().set_value(state, action, 0.0)

            if(not super().has_state(next_state)):
                error = reward.get_value() - super().get_value(state, action)
            else:
                error = reward.get_value() + self.get_discount_factor()*super().get_max_value(next_state) - super().get_value(state, action)
            value = super().get_value(state, action) + self.get_learning_rate()*error
            super().set_value(state, action, value)
          
    """------------------------------------------------------------------------------------------------
    """
    def _get_action(self, state):
        is_terminal_state = state.is_terminal()
        if(is_terminal_state):
            return None
    
        if(not self.has_state(state=state)):
             return None
        if(not self.has_actions(state=state)):
             return None

        action = max(self.get_actions(state=state), key=lambda action: self.get_value(state=state, action=action))
        return action


