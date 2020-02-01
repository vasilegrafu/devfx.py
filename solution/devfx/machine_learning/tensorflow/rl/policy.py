import devfx.exceptions as exps

class Policy(object):
    def __init__(self):
        pass

    """------------------------------------------------------------------------------------------------
    """ 
    def get_action(self, state):
        return self._get_action(state=state)

    def _get_action(self, state):
        raise exps.NotImplementedError()

