import devfx.exceptions as exps
from .policy import Policy

class QPolicy(Policy):
    def __init__(self):
        super().__init__()

        self.Q = {}

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_action(self, state):
        if(state not in self.Q):
             return None
        if(len(self.Q[state]) == 0):
            return None
            
        action = max(self.Q[state], key=lambda action: self.Q[state][action])
        return action

    """------------------------------------------------------------------------------------------------
    """ 
    def update(self, state, action, next_state, discount_factor, learning_rate):
        if(state not in self.Q):
            self.Q[state] = {}
        if(action not in self.Q[state]):
            self.Q[state][action] = 0.0

        if(next_state not in self.Q):
            self.Q[next_state] = {}
        
        if(len(self.Q[next_state]) == 0):
            error = next_state.reward - self.Q[state][action]
        else:
            next_action = max(self.Q[next_state], key=lambda action: self.Q[next_state][action])
            error = next_state.reward + discount_factor*self.Q[next_state][next_action] - self.Q[state][action]

        self.Q[state][action] = self.Q[state][action] + learning_rate*error
