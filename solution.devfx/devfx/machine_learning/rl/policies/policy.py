import devfx.exceptions as exp

class Policy(object):
    """------------------------------------------------------------------------------------------------
    """ 
    def learn(self, transitions):
        self._learn(transitions=transitions)

    def _learn(self, transitions):
        raise exp.NotImplementedError()
    
    """------------------------------------------------------------------------------------------------
    """ 
    def get_optimal_action(self, state):
        return self._get_optimal_action(state=state)

    def _get_optimal_action(self, state):
        raise exp.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_random_action(self, state):
        return self._get_random_action(state=state)

    def _get_random_action(self, state):
        raise exp.NotImplementedError()
    








    