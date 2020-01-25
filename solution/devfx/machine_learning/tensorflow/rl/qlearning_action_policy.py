import devfx.exceptions as exps
from .action_policy import ActionPolicy

class QLearningActionPolicy(ActionPolicy):
    def __init__(self):
        super().__init__()

    """------------------------------------------------------------------------------------------------
    """ 
    def update(self, state, action, next_state, next_state_reward):
        return self._update(state=state, action=action, next_state=next_state, next_state_reward=next_state_reward)

    def _update(self, state, action, next_state, next_state_reward):
        raise exps.NotImplementedError()

