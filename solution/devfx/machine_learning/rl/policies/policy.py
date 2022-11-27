import pickle as pckl
import devfx.exceptions as ex

class Policy(object):
    def __init__(self, model):
        self.set_model(model=model)

        self.__transitions_log = []

    """------------------------------------------------------------------------------------------------
    """ 
    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    """------------------------------------------------------------------------------------------------
    """   
    def log_transition(self, transition):
        self.__transitions_log.append(transition)

    def log_transitions(self, transitions):
        for transition in transitions:
            self.log_transition(transition=transition)

    def get_logged_transitions(self, n=None):
        if(n is None):
            n = len(self.__transitions_log)
        return self.__transitions_log[0:n]

    def clear_logged_transitions(self):
        return self.__transitions_log.clear()
       
    """------------------------------------------------------------------------------------------------
    """ 
    def learn(self, transitions):
        self._learn(transitions=transitions)

    def _learn(self, transitions):
        raise ex.NotImplementedError()
    
    """------------------------------------------------------------------------------------------------
    """ 
    def learn_from_logged_transitions(self):
        self.learn(transitions=self.__transitions_log)

    """------------------------------------------------------------------------------------------------
    """ 
    def get_action(self, state):
        return self._get_action(state=state)

    def _get_action(self, state):
        raise ex.NotImplementedError()








    