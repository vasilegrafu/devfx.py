import devfx.exceptions as exp
from ..policy import Policy

class FunctionAproximationPolicy(Policy):
    def __init__(self):
        self.__setup_model()
  
    """------------------------------------------------------------------------------------------------
    """ 
    def __setup_model(self):
        self.__model = None
   
    def __get_model(self):
        return self.__model

    """------------------------------------------------------------------------------------------------
    """ 
    def _learn(self, transitions):
        raise exp.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_optimal_action(self, state):
        raise exp.NotImplementedError()


    """------------------------------------------------------------------------------------------------
    """ 
    def _get_random_action(self, state):
        raise exp.NotImplementedError()