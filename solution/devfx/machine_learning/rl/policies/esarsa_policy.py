import numpy as np
import devfx.exceptions as exps
from .policy import Policy

class ESarsaPolicy(Policy):
    def __init__(self, discount_factor, learning_rate):
        super().__init__(discount_factor=discount_factor)

        self.qtable = {}
        self.learning_rate = learning_rate

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def qtable(self):
        return self.__qtable

    @qtable.setter
    def qtable(self, qtable):
        self.__qtable = qtable

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def learning_rate(self):
        return self.__learning_rate

    @learning_rate.setter
    def learning_rate(self, learning_rate):
        self.__learning_rate = learning_rate

    """------------------------------------------------------------------------------------------------
    """ 
    def _learn(self, state, action, next_state_and_reward):
        if(state not in self.qtable):
            self.qtable[state] = {}
        if(action not in self.qtable[state]):
            self.qtable[state][action] = 0.0

        (next_state, next_reward) = next_state_and_reward

        if(next_state not in self.qtable):
            self.qtable[next_state] = {}

        qs = self.qtable[state]
        qs_next = self.qtable[next_state]
       
        if(len(qs_next) == 0):
            error = next_reward.value - qs[action]
        else:
            qs_next_mean = sum(qs_next.values())/len(qs_next)
            error = next_reward.value + self.discount_factor*qs_next_mean - qs[action]

        qs[action] = qs[action] + self.learning_rate*error

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_optimal_action(self, state):
        if(state not in self.qtable):
             return None
        if(len(self.qtable[state]) == 0):
            return None

        qs = self.qtable[state]
            
        action = max(qs, key=lambda action: qs[action])
        return action

    """------------------------------------------------------------------------------------------------
    """ 
    def _copy(self):
        policy = ESarsaPolicy(discount_factor=self.discount_factor, learning_rate=self.learning_rate)
        for state in self.qtable:
            if(state not in policy.qtable):
                policy.qtable[state] = {}
            for action in self.qtable[state]:
                policy.qtable[state][action] = self.qtable[state][action]
        return policy

        