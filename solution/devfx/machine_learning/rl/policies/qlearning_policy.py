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



