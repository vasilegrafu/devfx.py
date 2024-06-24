import devfx.exceptions as excs
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
        raise excs.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_max_action(self, state):
        raise excs.NotImplementedError()

