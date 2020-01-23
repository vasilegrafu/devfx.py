import devfx.exceptions as exps

class ActionPolicy(object):
    def __init__(self, environment):
        self.__set_environment(environment=environment)

    """------------------------------------------------------------------------------------------------
    """ 
    def __set_environment(self, environment):
        self.__environment = environment

    def get_environment(self):
        return self.__environment

    """------------------------------------------------------------------------------------------------
    """ 
    def get_action(self, state):
        return self._get_action(state=state)

    def _get_action(self, state):
        raise exps.NotImplementedError()

