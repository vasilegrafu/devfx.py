import numpy as np
import devfx.exceptions as excs
from .policy import Policy

class AproximatePolicy(Policy):
    def __init__(self, discount_factor):
        super().__init__(discount_factor=discount_factor)

    """------------------------------------------------------------------------------------------------
    """
    def _set_model(self, model):
        raise excs.NotImplementedError()

    def _get_model(self):
        raise excs.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def _learn(self, state, action, next_state_and_reward):
        raise excs.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_optimal_action(self, state):
        raise excs.NotImplementedError()

