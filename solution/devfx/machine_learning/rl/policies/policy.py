import devfx.exceptions as excs
from ..state_kind import StateKind

class Policy(object):
    def __init__(self, discount_factor):
        self.__discount_factor = discount_factor

    """------------------------------------------------------------------------------------------------
    """ 
    def get_discount_factor(self):
        return self.__discount_factor

    def set_discount_factor(self, discount_factor):
        self.__discount_factor = discount_factor
        
    """------------------------------------------------------------------------------------------------
    """ 
    def learn(self, state, action, next_state_and_reward):
        self._learn(state=state, action=action, next_state_and_reward=next_state_and_reward)

    def _learn(self, state, action, next_state_and_reward):
        raise excs.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_optimal_action(self, state):
        is_terminal_state = state.kind == StateKind.TERMINAL
        if(is_terminal_state):
            raise excs.ApplicationError()

        action =  self._get_optimal_action(state=state)
        return action

    def _get_optimal_action(self, state):
        raise excs.NotImplementedError()


    """------------------------------------------------------------------------------------------------
    """ 
    def copy(self):
        return self._copy()

    def _copy(self):
        raise excs.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def assign_from(self, policies):
        return self._assign_from(policies=policies)

    def _assign_from(self, policies):
        raise excs.NotImplementedError()


    