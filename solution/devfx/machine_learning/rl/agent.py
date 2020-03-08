import numpy as np
import devfx.exceptions as exps
import devfx.core as core
from .state_kind import StateKind

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
        environment = self.get_environment()
        state = environment.get_random_state(agent_kind=self.get_kind())
        self.set_state(state=state)
        
    def set_random_non_terminal_state(self):
        environment = self.get_environment()
        state = environment.get_random_non_terminal_state(agent_kind=self.get_kind())
        self.set_state(state=state)

    def set_random_terminal_state(self):
        environment = self.get_environment()
        state = environment.get_random_terminal_state(agent_kind=self.get_kind())
        self.set_state(state=state)

    def get_state(self):
        return self.__state

    def get_state_kind(self):
        agent_kind = self.get_kind()
        environment = self.get_environment()
        state = self.get_state()
        state_kind = environment.get_state_kind(agent_kind=agent_kind, state=state)
        return state_kind

    def is_in_non_terminal_state(self):
        agent_kind = self.get_kind()
        environment = self.get_environment()
        state = self.get_state()
        is_in_non_terminal_state = environment.is_in_non_terminal_state(agent_kind=agent_kind, state=state)
        return is_in_non_terminal_state

    def is_in_terminal_state(self):
        agent_kind = self.get_kind()
        environment = self.get_environment()
        state = self.get_state()
        is_in_terminal_state = environment.is_in_terminal_state(agent_kind=agent_kind, state=state)
        return is_in_terminal_state

    """------------------------------------------------------------------------------------------------
    """
    def set_policy(self, policy):
        self.__policy = policy

    def get_policy(self):
        return self.__policy

    """------------------------------------------------------------------------------------------------
    """
    def learn(self, state, action, next_state, next_reward):
        self.get_policy().learn(state=state, action=action, next_state=next_state, next_reward=next_reward)

    """------------------------------------------------------------------------------------------------
    """ 
    def do_random_action(self):
        agent_kind = self.get_kind()
        environment = self.get_environment()
        state = self.get_state()

        is_in_terminal_state = environment.is_in_terminal_state(agent_kind=agent_kind, state=state)
        if(is_in_terminal_state):
            return

        action = environment.get_random_action(agent_kind=agent_kind, state=state)
        if(action is None):
            return
        else:
            (next_state, next_reward) = environment.get_next_state_and_reward(agent_kind=agent_kind, state=state, action=action)

        self.set_state(state=next_state)

        self.learn(state=state, action=action, next_state=next_state, next_reward=next_reward)


        return (state, action, next_state, next_reward)
  
    """------------------------------------------------------------------------------------------------
    """ 
    def do_action(self):
        agent_kind = self.get_kind()
        environment = self.get_environment()
        state = self.get_state()

        is_in_terminal_state = environment.is_in_terminal_state(agent_kind=agent_kind, state=state)
        if(is_in_terminal_state):
            return

        action = self.get_policy().get_action(state=state)
        if(action is None):
            return
        else:
            (next_state, next_reward) = environment.get_next_state_and_reward(agent_kind=agent_kind, state=state, action=action)

        self.set_state(state=next_state)

        self.learn(state=state, action=action, next_state=next_state, next_reward=next_reward)

        return (state, action, next_state, next_reward)


   