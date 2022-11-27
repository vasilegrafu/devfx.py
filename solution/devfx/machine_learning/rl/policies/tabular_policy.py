import devfx.exceptions as ex

from .policy import Policy

class TabularPolicy(Policy):
    def __init__(self):
        super().__init__(model={})
  
    """------------------------------------------------------------------------------------------------
    """
    @property
    def iter(self):
        for state in self.get_model():
            for action in self.get_model()[state]:
                value = self.get_model()[state][action]    
                yield (state, action, value)

    """------------------------------------------------------------------------------------------------
    """
    def get_states_count(self):
        return len(self.get_model())

    def get_states(self):
        return list(self.get_model().keys())

    def has_states(self):
        return len(self.get_model()) >= 1

    def has_state(self, state):
        return state in self.get_model()


    def get_actions_count(self, state):
        return len(self.get_model()[state])

    def get_actions(self, state):
        return list(self.get_model()[state].keys())

    def has_actions(self, state):
        return len(self.get_model()[state]) >= 1

    def has_action(self, state, action):
        return action in self.get_model()[state]


    def set_value(self, state, action, value):
        if(state not in self.get_model()):
            self.get_model()[state] = {}
        self.get_model()[state][action] = value

    def get_value(self, state, action):
        return self.get_model()[state][action]

    def has_value(self, state, action):
        if(state not in self.get_model()):
            return False
        if(action not in self.get_model()[state]):
            return False
        return True

    def get_max_value(self, state):
        return max(self.get_model()[state].values())

    def get_min_value(self, state):
        return min(self.get_model()[state].values())

    def get_avg_value(self, state):
        return sum(self.get_model()[state].values())/len(self.get_model()[state])


    """------------------------------------------------------------------------------------------------
    """ 
    def _learn(self, transitions):
        raise ex.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """
    def _get_action(self, state):
        raise ex.NotImplementedError()
                


