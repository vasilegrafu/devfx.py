import devfx.exceptions as exps
from .policy import Policy

class DQNPolicy(Policy):
    def __init__(self):
        super().__init__()

    """------------------------------------------------------------------------------------------------
    """ 
    def update(self, state, action, next_state):
        raise exps.NotImplementedError()

