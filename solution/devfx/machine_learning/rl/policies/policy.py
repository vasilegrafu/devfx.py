import devfx.exceptions as exps
from ..state_kind import StateKind

class Policy(object):
    def __init__(self, discount_factor):
        self.discount_factor = discount_factor

    """------------------------------------------------------------------------------------------------
    """ 
    @property
    def discount_factor(self):
        return self.__discount_factor

    @discount_factor.setter
    def discount_factor(self, discount_factor):
        self.__discount_factor = discount_factor
        

    """------------------------------------------------------------------------------------------------
    """ 
    def learn(self, state, action, next_state_and_reward):
        self._learn(state=state, action=action, next_state_and_reward=next_state_and_reward)

    def _learn(self, state, action, next_state_and_reward):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_optimal_action(self, state):
        is_terminal_state = state.kind == StateKind.TERMINAL
        if(is_terminal_state):
            raise exps.ApplicationError()

        action =  self._get_optimal_action(state=state)
        return action

    def _get_optimal_action(self, state):
        raise exps.NotImplementedError()


    """------------------------------------------------------------------------------------------------
    """ 
    def copy(self):
        self._copy()

    def _copy(self):
        raise exps.NotImplementedError()
    

