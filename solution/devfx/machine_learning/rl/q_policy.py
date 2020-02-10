import devfx.exceptions as exps
from .policy import Policy

class QPolicy(Policy):
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
    def _update(self, state, action, next_state):
        if(state not in self.qtable):
            self.qtable[state] = {}
        if(action not in self.qtable[state]):
            self.qtable[state][action] = 0.0

        if(next_state not in self.qtable):
            self.qtable[next_state] = {}
        
        if(len(self.qtable[next_state]) == 0):
            error = next_state.reward - self.qtable[state][action]
        else:
            next_action = max(self.qtable[next_state], key=lambda action: self.qtable[next_state][action])
            error = next_state.reward + self.discount_factor*self.qtable[next_state][next_action] - self.qtable[state][action]

        self.qtable[state][action] = self.qtable[state][action] + self.learning_rate*error

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_action(self, state):
        if(state not in self.qtable):
             return None
        if(len(self.qtable[state]) == 0):
            return None
            
        action = max(self.qtable[state], key=lambda action: self.qtable[state][action])
        return action