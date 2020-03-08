import devfx.exceptions as exps

class Policy(object):
    def __init__(self, discount_factor):
        self.discount_factor = discount_factor

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def discount_factor(self):
        return self.__discount_factor

    @discount_factor.setter
    def discount_factor(self, discount_factor):
        self.__discount_factor = discount_factor
        

    """------------------------------------------------------------------------------------------------
    """ 
    def learn(self, state, action, next_state, next_reward):
        self._learn(state=state, action=action, next_state=next_state, next_reward=next_reward)

    def _learn(self, state, action, next_state, next_reward):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_action(self, state):
        return self._get_action(state=state)

    def _get_action(self, state):
        raise exps.NotImplementedError()

