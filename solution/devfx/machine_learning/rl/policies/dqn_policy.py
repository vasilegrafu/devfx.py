import devfx.exceptions as exps
from .policy import Policy

class DQNPolicy(Policy):
    def __init__(self, discount_factor):
        super().__init__(discount_factor=discount_factor)

    """------------------------------------------------------------------------------------------------
    """ 
    def _update(self, state, action, next_state, reward):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_action(self, state):
        raise exps.NotImplementedError()

