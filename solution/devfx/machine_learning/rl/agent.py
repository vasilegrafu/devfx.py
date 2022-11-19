import numpy as np
import devfx.exceptions as excps
import devfx.core as core
from .state_kind import StateKind

class Agent(object):
    def __init__(self, id, name, kind, environment, state=None, policy=None, iteration_randomness=0.0):
        self.__set_id(id=id)
        self.__set_name(name=name)
        self.__set_kind(kind=kind)
        self.__set_environment(environment=environment)
        self.set_state(state=state)
        self.set_policy(policy=policy)
        self.set_iteration_randomness(iteration_randomness=iteration_randomness)

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
    def __set_environment(self, environment):
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
        is_in_non_terminal_state = state.kind == StateKind.NON_TERMINAL
        return is_in_non_terminal_state

    def is_in_terminal_state(self):
        state = self.get_state()
        is_in_terminal_state = state.kind == StateKind.TERMINAL
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
        policy = self.get_policy()
        agent.set_policy(policy=policy)


    def switch_policy_with(self, agent):
        policy = agent.get_policy()
        agent.set_policy(policy=self.get_policy())
        self.set_policy(policy=policy)
        

    def transfer_policy_from(self, agent):
        policy = agent.get_policy()
        agent.set_policy(policy=None)
        self.set_policy(policy=policy)

    def transfer_policy_to(self, agent):
        policy = self.get_policy()
        self.set_policy(policy=None)
        agent.set_policy(policy=policy)


    def copy_policy_from(self, agent):
        policy = agent.get_policy().copy()
        self.set_policy(policy=policy)

    def copy_policy_to(self, agent):
        policy = self.get_policy().copy()
        agent.set_policy(policy=policy)

    """------------------------------------------------------------------------------------------------
    """
    def learn(self, state, action, reward, next_state):
        self.get_policy().learn(state=state, action=action, reward=reward, next_state=next_state)

    """------------------------------------------------------------------------------------------------
    """ 
    def do_action(self, action):
        environment = self.get_environment()
        (state, action, (reward, next_state)) = environment.do_action(agent=self, action=action)
        return (state, action, (reward, next_state))

    def do_random_action(self):
        environment = self.get_environment()
        (state, action, (reward, next_state)) = environment.do_random_action(agent=self)
        return (state, action, (reward, next_state))
 
    def do_optimal_action(self):
        environment = self.get_environment()
        (state, action, (reward, next_state)) = environment.do_optimal_action(agent=self)
        return (state, action, (reward, next_state))

    """------------------------------------------------------------------------------------------------
    """
    def set_iteration_randomness(self, iteration_randomness):
        self.__iteration_randomness = iteration_randomness

    def get_iteration_randomness(self):
        return self.__iteration_randomness




   