import devfx.exceptions as exps
from .action_policy import ActionPolicy

class RandomActionPolicy(ActionPolicy):
    def __init__(self, environment):
        super().__init__(environment=environment)

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_action(self, state):
        action = super().get_environment().get_random_action(state=state)
        return action