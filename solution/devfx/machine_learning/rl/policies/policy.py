import pickle as pckl
import devfx.exceptions as ex

class Policy(object):
    def __init__(self):
        pass

    """------------------------------------------------------------------------------------------------
    """ 
    def _set_model(self, model):
        raise ex.NotImplementedError()

    def _get_model(self):
        raise ex.NotImplementedError()
    
    @property
    def model(self):
        return self._get_model()


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
       
    """------------------------------------------------------------------------------------------------
    """ 
    def learn(self, state, action, reward, next_state):
        self._learn(state=state, action=action, reward=reward, next_state=next_state)

    def _learn(self, state, action, reward, next_state):
        raise ex.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_action(self, state):
        return self._get_action(state=state)

    def _get_action(self, state):
        raise ex.NotImplementedError()








    