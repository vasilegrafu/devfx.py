import devfx.exceptions as exps
from .policy import Policy

class DQNPolicy(Policy):
    def __init__(self, discount_factor):
        super().__init__(discount_factor=discount_factor)

    """------------------------------------------------------------------------------------------------
    """ 
    def _learn(self, state, action, next_state_and_reward):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_optimal_action(self, state):
        raise exps.NotImplementedError()

