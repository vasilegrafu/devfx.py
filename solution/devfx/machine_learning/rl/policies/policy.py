import pickle as pckl
import devfx.exceptions as ex

class Policy(object):
    def __init__(self):
        self._setup_model()

    """------------------------------------------------------------------------------------------------
    """ 
    def _setup_model(self):
        raise ex.NotImplementedError()

    def get_model(self):
        return self._get_model()
    
    def _get_model(self):
        raise ex.NotImplementedError()
      
    """------------------------------------------------------------------------------------------------
    """ 
    def learn(self, transitions):
        self._learn(transitions=transitions)

    def _learn(self, transitions):
        raise ex.NotImplementedError()
    
    """------------------------------------------------------------------------------------------------
    """ 
    def get_action(self, state):
        return self._get_action(state=state)

    def _get_action(self, state):
        raise ex.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_random_action(self, state):
        return self._get_action(state=state)

    def _get_random_action(self, state):
        raise ex.NotImplementedError()
    








    