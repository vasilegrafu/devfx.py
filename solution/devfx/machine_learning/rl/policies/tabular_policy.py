import devfx.exceptions as excps

from .policy import Policy

class TabularPolicy(Policy):
    def __init__(self, discount_factor):
        super().__init__(discount_factor=discount_factor)

        self.__model = {}

    """------------------------------------------------------------------------------------------------
    """
    def _set_model(self, model):
        self.__model = model

    def _get_model(self):
        return self.__model

    """------------------------------------------------------------------------------------------------
    """
    def get_states_count(self):
        return len(self.__model)

    def get_states(self):
        return list(self.__model.keys())

    def has_states(self):
        return len(self.__model) >= 1

    def has_state(self, state):
        return state in self.__model


    def get_actions_count(self, state):
        return len(self.__model[state])

    def get_actions(self, state):
        return list(self.__model[state].keys())

    def has_actions(self, state):
        return len(self.__model[state]) >= 1

    def has_action(self, state, action):
        return action in self.__model[state]


    def set_value(self, state, action, value):
        if(state not in self.__model):
            self.__model[state] = {}
        self.__model[state][action] = value

    def get_value(self, state, action):
        return self.__model[state][action]

    def has_value(self, state, action):
        if(state not in self.__model):
            return False
        if(action not in self.__model[state]):
            return False
        return True

    def get_max_value(self, state):
        return max(self.__model[state].values())

    def get_min_value(self, state):
        return min(self.__model[state].values())

    def get_avg_value(self, state):
        return sum(self.__model[state].values())/len(self.__model[state])


    """------------------------------------------------------------------------------------------------
    """ 
    def _learn(self, state, action, next_state, next_reward):
        raise excps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """
    def _get_optimal_action(self, state):
        if(not self.has_state(state=state)):
             return (None, None)
        if(not self.has_actions(state=state)):
             return (None, None)

        action = max(self.get_actions(state=state), key=lambda action: self.get_value(state=state, action=action))
        value = self.get_value(state=state, action=action)
        return (action, value)



