import numpy as np
import devfx.exceptions as ex
import devfx.core as core
from .state_kind import StateKind

class Agent(object):
    def __init__(self, id, name, kind, policy):
        self.__set_id(id=id)
        self.__set_name(name=name)
        self.__set_kind(kind=kind)
        self.set_policy(policy=policy)  

    """------------------------------------------------------------------------------------------------
    """
    def __set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id
    
    """------------------------------------------------------------------------------------------------
    """
    def __set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    """------------------------------------------------------------------------------------------------
    """
    def __set_kind(self, kind):
        self.__kind = kind

    def get_kind(self):
        return self.__kind
    
    """------------------------------------------------------------------------------------------------
    """ 
    def set_environment(self, environment):
        self.__environment = environment
                
    def get_environment(self):
        return self.__environment
           
    """------------------------------------------------------------------------------------------------
    """
    def set_state(self, state):
        self.__state = state
      
    def get_state(self):
        return self.__state   
    

    def is_in_non_terminal_state(self):
        state = self.get_state()
        is_in_non_terminal_state = state.get_kind() == StateKind.NON_TERMINAL
        return is_in_non_terminal_state

    def is_in_terminal_state(self):
        state = self.get_state()
        is_in_terminal_state = state.get_kind() == StateKind.TERMINAL
        return is_in_terminal_state

    """------------------------------------------------------------------------------------------------
    """
    def set_policy(self, policy):
        self.__policy = policy

    def get_policy(self):
        return self.__policy
       

    def share_policy_from(self, agent):
        policy = agent.get_policy()
        self.set_policy(policy=policy)

    def share_policy_to(self, agent):
        agent.share_policy_from(agent=self)


    def switch_policy_with(self, agent):
        policy = agent.get_policy()
        agent.set_policy(policy=self.get_policy())
        self.set_policy(policy=policy)
        

    def transfer_policy_from(self, agent):
        policy = agent.get_policy()
        agent.set_policy(policy=None)
        self.set_policy(policy=policy)

    def transfer_policy_to(self, agent):
        agent.transfer_policy_from(agent=self)
       
    """------------------------------------------------------------------------------------------------
    """ 
    def do_action(self, action=None):   
        is_terminal_state = self.is_in_terminal_state()
        if(is_terminal_state):
            raise ex.ApplicationError()

        state = self.get_state()
        
        if(action is None):
            action = self.get_policy().get_action(state=state)

        if(action is None):
            return None

        (reward, next_state) = self.get_environment().get_reward_and_next_state(agent=self, action=action)

        self.set_state(state=next_state)

        transition = (state, action, (reward, next_state))

        self.get_policy().log_transition(transition=transition)
        
        return transition
