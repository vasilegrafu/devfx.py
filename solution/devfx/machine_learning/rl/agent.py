import numpy as np
import devfx.exceptions as exps
import devfx.core as core

class Agent(object):
    def __init__(self, id, kind, environment, state, policy):
        self.__set_id(id=id)
        self.__set_kind(kind=kind)
        self.__set_environment(environment=environment)
        self.set_state(state=state)
        self.set_policy(policy=policy)

    """------------------------------------------------------------------------------------------------
    """
    def __set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    """------------------------------------------------------------------------------------------------
    """
    def __set_kind(self, kind):
        self.__kind = kind

    def get_kind(self):
        return self.__kind

    """------------------------------------------------------------------------------------------------
    """ 
    def __set_environment(self, environment):
        self.__environment = environment
                
    def get_environment(self):
        return self.__environment
        
    """------------------------------------------------------------------------------------------------
    """
    def set_state(self, state):
        self.__state = state

    def set_random_state(self):
        self.set_state(state=self.get_environment().get_random_state(agent_kind=self.get_kind()))
        
    def set_random_non_terminal_state(self):
        self.set_state(state=self.get_environment().get_random_non_terminal_state(agent_kind=self.get_kind()))
        
    def set_random_terminal_state(self):
        self.set_state(state=self.get_environment().set_random_terminal_state(agent_kind=self.get_kind()))

    def get_state(self):
        return self.__state

    """------------------------------------------------------------------------------------------------
    """
    def set_policy(self, policy):
        self.__policy = policy

    def get_policy(self):
        return self.__policy

    """------------------------------------------------------------------------------------------------
    """ 
    def do_random_action(self):
        environment = self.get_environment()

        state = self.get_state()
        if(state.is_terminal()):
            return

        policy = self.get_policy()

        action = environment.get_random_action(agent=self)
        if(action is None):
            return
        else:
            (next_state, reward) = environment.get_next_state_and_reward(agent=self, action=action)

        self.set_state(state=next_state)

        policy.update(state=state, action=action, next_state=next_state, reward=reward)

        return (state, action, next_state, reward)
  
    """------------------------------------------------------------------------------------------------
    """ 
    def do_action(self):
        environment = self.get_environment()

        state = self.get_state()
        if(state.is_terminal()):
            return

        policy = self.get_policy()
       
        action = policy.get_action(state=state)
        if(action is None):
            return
        else:
            (next_state, reward) = environment.get_next_state_and_reward(agent=self, action=action)

        self.set_state(state=next_state)

        policy.update(state=state, action=action, next_state=next_state, reward=reward)

        return (state, action, next_state, reward)


   