import numpy as np
import devfx.exceptions as ex
import devfx.core as core

class Agent(object):
    def __init__(self, id, name, kind, policy):
        self.__set_id(id=id)
        self.__set_name(name=name)
        self.__set_kind(kind=kind)
        self.__set_policy(policy=policy)  

        self.__setup_transitions_log()

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
    def __set_policy(self, policy):
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
    

    def is_in_undeifned_state(self):
        state = self.get_state()
        is_undefined_state = state.is_undefined()
        return is_undefined_state
    
    def is_in_non_terminal_state(self):
        state = self.get_state()
        is_non_terminal_state = state.is_non_terminal()
        return is_non_terminal_state

    def is_in_terminal_state(self):
        state = self.get_state()
        is_terminal_state = state.is_terminal()
        return is_terminal_state
      
    """------------------------------------------------------------------------------------------------
    """ 
    def do_action(self, action=None, log_transition=False):   
        is_in_terminal_state = self.is_in_terminal_state()
        if(is_in_terminal_state):
            return None

        state = self.get_state()
        
        if(action is None):
            action = self.get_policy().get_action(state=state)

        if(action is None):
            return None

        reward_and_next_state = self.get_environment().do_next_transition(agent=self, action=action)
        
        if(reward_and_next_state is None):
            return None

        (reward, next_state) = reward_and_next_state

        self.set_state(state=next_state)

        transition = (state, action, (reward, next_state))

        if(log_transition == True):
            self.log_transition(transition=transition)
        
        return transition

    """------------------------------------------------------------------------------------------------
    """ 
    def learn(self, transitions):
        self.get_policy().learn(transitions=transitions)

    """------------------------------------------------------------------------------------------------
    """ 
    def __setup_transitions_log(self):
        self.__transitions_log = []

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

    def learn_from_logged_transitions(self):
        self.get_policy().learn(transitions=self.__transitions_log)