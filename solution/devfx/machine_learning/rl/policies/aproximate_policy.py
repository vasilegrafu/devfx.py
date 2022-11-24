import devfx.exceptions as ex
from .policy import Policy

class AproximatePolicy(Policy):
    def __init__(self, discount_factor):
        super().__init__(discount_factor=discount_factor)

    """------------------------------------------------------------------------------------------------
    """
    def _set_model(self, model):
        raise ex.NotImplementedError()

    def _get_model(self):
        raise ex.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def _learn(self, state, action, reward, next_state):
        raise ex.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_optimal_action(self, state):
        raise ex.NotImplementedError()

