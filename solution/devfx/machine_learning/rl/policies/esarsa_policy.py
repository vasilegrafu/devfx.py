import random as rnd
import numpy as np
import devfx.exceptions as excs
from .policy import Policy

class ESarsaPolicy(Policy):
    def __init__(self, discount_factor, learning_rate):
        super().__init__(discount_factor=discount_factor)

        self.__learning_rate = learning_rate

    """------------------------------------------------------------------------------------------------
    """ 
    def get_learning_rate(self):
        return self.__learning_rate

    def set_learning_rate(self, learning_rate):
        self.__learning_rate = learning_rate

    """------------------------------------------------------------------------------------------------
    """
    def _learn(self, state, action, next_state_and_reward):
        if(not super().has_value(state, action)):
            super().set_value(state, action, 0.0)

        (next_state, next_reward) = next_state_and_reward
        if(not super().has_state(next_state)):
            error = next_reward.value - super().get_value(state, action)
        else:
            error = next_reward.value + self.get_discount_factor()*super().get_avg_value(next_state) - super().get_value(state, action)
        super().set_value(state, action, super().get_value(state, action) + self.get_learning_rate()*error)




    