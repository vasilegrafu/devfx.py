import devfx.exceptions as excps
from .policy import Policy

class AproximatePolicy(Policy):
    def __init__(self, discount_factor):
        super().__init__(discount_factor=discount_factor)

    """------------------------------------------------------------------------------------------------
    """
    def _set_model(self, model):
        raise excps.NotImplementedError()

    def _get_model(self):
        raise excps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def _learn(self, state, action, next_state, next_reward):
        raise excps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_optimal_action(self, state):
        raise excps.NotImplementedError()

