import devfx.exceptions as ex
from .policy import Policy

class RandomPolicy(Policy):
    def __init__(self):
        super().__init__()

        self._set_model(model=None)
   
    """------------------------------------------------------------------------------------------------
    """ 
    def _set_model(self, model):
        self.__model = model

    def _get_model(self):
        return self.__model

    """------------------------------------------------------------------------------------------------
    """ 
    def _learn(self, state, action, reward, next_state):
        pass

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_action(self, state):
        raise ex.NotImplementedError()

