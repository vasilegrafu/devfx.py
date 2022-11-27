import devfx.exceptions as ex
from .policy import Policy

class RandomPolicy(Policy):
    def __init__(self):
        super().__init__(model=None)
  
    """------------------------------------------------------------------------------------------------
    """ 
    def _learn(self, transitions):
        pass

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_action(self, state):
        raise ex.NotImplementedError()

