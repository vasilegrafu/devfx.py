import pickle as pkl
import devfx.exceptions as excps
from ..state_kind import StateKind

class Policy(object):
    def __init__(self, discount_factor):
        self.__discount_factor = discount_factor

    """------------------------------------------------------------------------------------------------
    """ 
    def _set_model(self, model):
        raise excps.NotImplementedError()

    def _get_model(self):
        raise excps.NotImplementedError()


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
        model = pkl.loads(pkl.dumps(policy._get_model(), protocol=pkl.HIGHEST_PROTOCOL))
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
    def learn(self, state, action, next_state_and_reward):
        self._learn(state=state, action=action, next_state_and_reward=next_state_and_reward)

    def _learn(self, state, action, next_state_and_reward):
        raise excps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_optimal_action(self, state):
        is_terminal_state = state.kind == StateKind.TERMINAL
        if(is_terminal_state):
            raise excps.ApplicationError()

        (action, value) =  self._get_optimal_action(state=state)
        return (action, value)

    def _get_optimal_action(self, state):
        raise excps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def copy(self):
        return pkl.loads(pkl.dumps(self, protocol=pkl.HIGHEST_PROTOCOL))








    