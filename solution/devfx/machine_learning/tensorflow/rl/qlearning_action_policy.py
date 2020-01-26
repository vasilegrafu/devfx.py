import devfx.exceptions as exps
from .action_policy import ActionPolicy

class QLearningActionPolicy(ActionPolicy):
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
        action = max(self.Q[state], key=lambda k: self.Q[state][k])
        return action

    """------------------------------------------------------------------------------------------------
    """ 
    def update(self, state, action, next_state, alpha, gamma):
        if(state not in self.Q):
            self.Q[state] = {}
        if(action not in self.Q[state]):
            self.Q[state][action] = 0.0

        if(next_state not in self.Q):
            self.Q[next_state] = {}
        
        if(self.get_action(state=next_state) is None):
            next_state_action = None
        else:
            next_state_action = max(self.Q[next_state], key=lambda k: self.Q[next_state][k])
        error = next_state.reward + gamma*(self.Q[next_state][next_state_action] if(next_state_action is not None) else 0.0) - self.Q[state][action]
        self.Q[state][action] += self.Q[state][action] + alpha*error
