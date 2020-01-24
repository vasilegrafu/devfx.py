import devfx.exceptions as exps
from .action_policy import ActionPolicy

class QLearningActionPolicy(ActionPolicy):
    def __init__(self):
        super().__init__()

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_action(self, state):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def update(self, state, action, reward):
        return self._update(state=state, action=action, reward=reward)

    def _update(self, state, action, reward):
        raise exps.NotImplementedError()

