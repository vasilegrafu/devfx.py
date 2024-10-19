import devfx.exceptions as exp
from .policy import Policy

class AproximatePolicy(Policy):
    def __init__(self):
        super().__init__()

    """------------------------------------------------------------------------------------------------
    """ 
    def _setup_model(self):
        self.__model = None
   
    def _get_model(self):
        return self.__model

    """------------------------------------------------------------------------------------------------
    """ 
    def _learn(self, transitions):
        raise exp.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_max_action(self, state):
        raise exp.NotImplementedError()

