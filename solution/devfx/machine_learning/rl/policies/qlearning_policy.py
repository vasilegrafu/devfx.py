import devfx.exceptions as ex

from .tabular_policy import TabularPolicy
from ..state_kind import StateKind

class QLearningPolicy(TabularPolicy):
    def __init__(self, discount_factor, learning_rate):
        super().__init__()

        self.__set_discount_factor(discount_factor=discount_factor)
        self.__set_learning_rate(learning_rate=learning_rate)

    """------------------------------------------------------------------------------------------------
    """ 
    def __set_discount_factor(self, discount_factor):
        self.__discount_factor = discount_factor

    def __get_discount_factor(self):
        return self.__discount_factor

    @property
    def discount_factor(self):
        return self.__get_discount_factor()

    """------------------------------------------------------------------------------------------------
    """ 
    def __set_learning_rate(self, learning_rate):
        self.__learning_rate = learning_rate

    def __get_learning_rate(self):
        return self.__learning_rate

    @property
    def learning_rate(self):
        return self.__get_learning_rate()

    """------------------------------------------------------------------------------------------------
    """
    def _learn(self, state, action, reward, next_state):
        if(not super().has_value(state, action)):
            super().set_value(state, action, 0.0)

        if(not super().has_state(next_state)):
            error = reward.value - super().get_value(state, action)
        else:
            error = reward.value + self.__get_discount_factor()*super().get_max_value(next_state) - super().get_value(state, action)
        value = super().get_value(state, action) + self.__get_learning_rate()*error
        super().set_value(state, action, value)
          
    """------------------------------------------------------------------------------------------------
    """
    def _get_action(self, state):
        is_terminal_state = state.kind == StateKind.TERMINAL
        if(is_terminal_state):
            raise ex.ApplicationError()
    
        if(not self.has_state(state=state)):
             return None
        if(not self.has_actions(state=state)):
             return None

        action = max(self.get_actions(state=state), key=lambda action: self.get_value(state=state, action=action))
        return action


