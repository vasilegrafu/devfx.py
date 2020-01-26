import devfx.exceptions as exps
from .action_policy import ActionPolicy

class DQLearningActionPolicy(ActionPolicy):
    def __init__(self):
        super().__init__()

    """------------------------------------------------------------------------------------------------
    """ 
    def update(self, state, action, next_state):
        raise exps.NotImplementedError()

