import pickle as pckl
import devfx.exceptions as exp

class Policy(object):
    def __init__(self):
        self._setup_model()

    """------------------------------------------------------------------------------------------------
    """ 
    def _setup_model(self):
        raise exp.NotImplementedError()

    def get_model(self):
        return self._get_model()
    
    def _get_model(self):
        raise exp.NotImplementedError()
      
    """------------------------------------------------------------------------------------------------
    """ 
    def learn(self, transitions):
        self._learn(transitions=transitions)

    def _learn(self, transitions):
        raise exp.NotImplementedError()
    
    """------------------------------------------------------------------------------------------------
    """ 
    def get_max_action(self, state):
        return self._get_max_action(state=state)

    def _get_max_action(self, state):
        raise exp.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_random_action(self, state):
        return self._get_random_action(state=state)

    def _get_random_action(self, state):
        raise exp.NotImplementedError()
    








    