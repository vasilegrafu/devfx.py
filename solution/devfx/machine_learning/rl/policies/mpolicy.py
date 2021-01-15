import pickle as pkl
import devfx.exceptions as excs
from ..state_kind import StateKind

class MPolicy(object):
    def __init__(self, policies=None):
        self.__policies = policies

    """------------------------------------------------------------------------------------------------
    """ 
    def set_policies(self, policies):
        self.__policies = policies

    def get_policies(self):
        return self.__policies
          
    """------------------------------------------------------------------------------------------------
    """ 
    def learn(self, state, action, next_state_and_reward):
        if(self.__policies is None):
            return
        else:
            for policy in self.__policies:
                policy.learn(state=state, action=action, next_state_and_reward=next_state_and_reward)

    """------------------------------------------------------------------------------------------------
    """ 
    def get_optimal_action(self, state):
        if(self.__policies is None):
            return (None, None)
        else:
            actions_values = [policy.get_optimal_action(state=state) for policy in self.__policies]
            actions_values = [(action, value) for (action, value) in actions_values if(action is not None)]
            if(len(actions_values) == 0):
                return (None, None)
            else:
                return max(actions_values, key = lambda action_value: action_value[1])         

    """------------------------------------------------------------------------------------------------
    """ 
    def copy(self):
        if(self.__policies is None):
            return None
        else:
            return [policy.copy() for policy in self.__policies]








    