import devfx.exceptions as exps
from .action_policy import ActionPolicy

class VLearningActionPolicy(ActionPolicy):
    def __init__(self):
        super().__init__()

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_action(self, state):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def update(self, state, reward):
        return self._update(state=state, reward=reward)

    def _update(self, state, reward):
        raise exps.NotImplementedError()

