import devfx.exceptions as exps
from .action_policy import ActionPolicy

class RandomActionPolicy(ActionPolicy):
    def __init__(self, environment):
        super().__init__()
        self.set_environment(environment=environment)

    """------------------------------------------------------------------------------------------------
    """ 
    def set_environment(self, environment):
        self.__environment = environment

    def get_environment(self):
        return self.__environment

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_action(self, state):
        action = self.get_environment().get_random_action(state=state)
        return action