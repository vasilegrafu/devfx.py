import pickle as pckl
import devfx.exceptions as ex
from ..state_kind import StateKind

class Policy(object):
    def __init__(self, discount_factor):
        self.__discount_factor = discount_factor

    """------------------------------------------------------------------------------------------------
    """ 
    def _set_model(self, model):
        raise ex.NotImplementedError()

    def _get_model(self):
        raise ex.NotImplementedError()


    def share_model_from(self, policy):
        model = policy._get_model()
        self._set_model(model=model)
   
    def share_model_to(self, policy):
        policy.share_model_from(policy=self)


    def switch_model_with(self, policy):
        model = policy._get_model()
        policy._set_model(model=self._get_model())
        self._set_model(model=model)


    def transfer_model_from(self, policy):
        model = policy._get_model()
        policy._set_model(model=None)
        self._set_model(model=model)

    def transfer_model_to(self, policy):
        policy.transfer_model_from(policy=self)


    def copy_model_from(self, policy):
        model = pckl.loads(pckl.dumps(policy._get_model(), protocol=pckl.HIGHEST_PROTOCOL))
        self._set_model(model=model)

    def copy_model_to(self, policy):
        policy.copy_model_from(policy=self)

    """------------------------------------------------------------------------------------------------
    """ 
    def get_discount_factor(self):
        return self.__discount_factor

    def set_discount_factor(self, discount_factor):
        self.__discount_factor = discount_factor
        
    """------------------------------------------------------------------------------------------------
    """ 
    def learn(self, state, action, reward, next_state):
        self._learn(state=state, action=action, reward=reward, next_state=next_state)

    def _learn(self, state, action, reward, next_state):
        raise ex.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_optimal_action(self, state):
        is_terminal_state = state.kind == StateKind.TERMINAL
        if(is_terminal_state):
            raise ex.ApplicationError()

        action_value = self._get_optimal_action(state=state)
        return action_value

    def _get_optimal_action(self, state):
        raise ex.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def copy(self):
        return pckl.loads(pckl.dumps(self, protocol=pckl.HIGHEST_PROTOCOL))








    