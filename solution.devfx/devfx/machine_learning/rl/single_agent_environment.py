import threading
import numpy as np
import random as rnd
import devfx.exceptions as exp
import devfx.core as core
from .agent import Agent
from .state_kind import StateKind

class SingleAgentEnvironment(object):
    def __init__(self):
        self.__agent = None

    """------------------------------------------------------------------------------------------------
    """    
    def setup(self, *args, **kwargs):
        return self._setup(*args, **kwargs)

    def _setup(self, *args, **kwargs):
        raise exp.NotImplementedError()


    def reset(self, *args, **kwargs):
        return self._reset(*args, **kwargs)

    def _reset(self, *args, **kwargs):
        raise exp.NotImplementedError()    
           

    """------------------------------------------------------------------------------------------------
    """ 
    def set_agent(self, agent):
        if(self.__agent is not None):
            raise exp.ApplicationError()
        
        self.__agent = agent
        agent.set_environment(environment=self)
        
        self._on_set_agent(agent=agent)
       
    def _on_set_agent(self, agent):
        raise exp.NotImplementedError()   


    def remove_agent(self, agent=None):
        if(agent is None):
            agent = self.__agent
            
        if(agent is None):
            raise exp.ApplicationError()
        
        if(agent != self.__agent):
            raise exp.ApplicationError()
        
        self.__agent = None
        agent.set_environment(environment=None)
        
        self._on_removed_agent(agent=agent)
       
    def _on_removed_agent(self, agent):
        raise exp.NotImplementedError()   


    def get_agent(self):
        return self.__agent

    def exists_agent(self):
        return self.__agent is not None
    

    def has_agent_in_undefined_state(self):
        return self.__agent.is_in_undefined_state()
        
    def has_agent_in_terminal_state(self):
        return self.__agent.is_in_terminal_state()
        
    def has_agents_in_non_terminal_state(self):
        return self.__agent.is_in_non_terminal_state()

    """------------------------------------------------------------------------------------------------
    """      
    def do_action(self, agent, action = None, log_transition=False):
        transition = agent.do_action(action=action, log_transition=log_transition)
        return transition

    """------------------------------------------------------------------------------------------------
    """  
    def generate_random_action(self, agent):
        action = self._generate_random_action(agent=agent)
        return action

    def _generate_random_action(self, agent):
        raise exp.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """    
    def do_next_transition(self, agent, action):
        is_terminal_state = agent.is_in_terminal_state()
        if(is_terminal_state):
            return None
        
        (reward, next_state) = self._do_next_transition(agent=agent, action=action)

        return (reward, next_state)
        
    def _do_next_transition(self, agent, action):
        raise exp.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def do_iteration(self, log_transition=False):
        self._do_iteration(log_transition=log_transition)

    def _do_iteration(self, log_transition=False):
        agent = self.get_agent()
        if(agent.is_in_terminal_state()):
            self.reset()
        else:
            self.do_action(agent=agent, log_transition=log_transition)

    def do_iterations(self, n, log_transition=False):
        self._do_iterations(n=n, log_transition=log_transition)

    def _do_iterations(self, n, log_transition=False):
        for i in range(0, n):
            self.do_iteration(log_transition=log_transition)

     


        



