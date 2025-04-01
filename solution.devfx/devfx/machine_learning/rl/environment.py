import threading
import numpy as np
import random as rnd
import devfx.exceptions as exp
import devfx.core as core
from .agent import Agent
from .state_kind import StateKind

class Environment(object):
    def __init__(self):
        self.__agents_container = {}

    """------------------------------------------------------------------------------------------------
    """    
    def setup(self, *args, **kwargs):
        raise exp.NotImplementedError()   

    def reset(self, *args, **kwargs):
        raise exp.NotImplementedError() 
    

    """------------------------------------------------------------------------------------------------
    """ 
    def install_agents(self, agents):
        for agent in agents:
            if(agent.get_id() in self.__agents_container):
                raise exp.ApplicationError()
            
        for agent in agents:
            self.__agents_container[agent.get_id()] = agent
            agent.set_environment(environment=self)
            
        self._on_installed_agents(agents=agents)
       
    def _on_installed_agents(self, agents):
        pass


    def uninstall_agents(self, agents):
        for agent in agents:    
            if(agent.get_id() not in self.__agents_container):
                raise exp.ApplicationError("You try to uninstall an agent that is not installed.")
            
        for agent in agents: 
            self.__agents_container.pop(agent.get_id())
            agent.set_environment(environment=None)

        self._on_uninstalled_agents(agents=agents)
       
    def _on_uninstalled_agents(self, agents):
        pass


    def get_agents(self):
        agents = [agent for agent in self.__agents_container.values()]
        return agents

    def get_agents_cycler(self):
        def get_agents_cycler(self):
            while(True):
                agents = [agent for agent in self.__agents_container.values()]
                for agent in agents:
                    yield agent  
        agents_iter = core.ObjectStorage.intercept(self, 'agents_iter', lambda: get_agents_cycler(self=self))
        return agents_iter
    
    def exists_agent(self, id):
        return id in self.__agents_container

    def get_agent(self, id):
        if(id not in self.__agents_container):
            raise exp.ApplicationError()
        agent = [agent for agent in self.__agents_container.values() if(agent.get_id() == id)][0]
        return agent

    def get_agents_others_than(self, id):
        agents = [agent for agent in self.__agents_container.values() if(agent.get_id() != id)]
        return agents


    def get_agents_of_kind(self, kind):
        agents = [agent for agent in self.__agents_container.values() if(agent.get_kind() == kind)]
        return agents

    def get_agents_not_of_kind(self, kind):
        agents = [agent for agent in self.__agents_container.values() if(agent.get_kind() != kind)]
        return agents


    def has_agents_in_undefined_state(self):
        has_agents_in_undefined_state = any(agent.is_in_undefined_state() for agent in self.__agents_container.values())
        return has_agents_in_undefined_state
        
    def has_agents_in_terminal_state(self):
        has_agents_in_terminal_state = any(agent.is_in_terminal_state() for agent in self.__agents_container.values())
        return has_agents_in_terminal_state
    
    def has_agents_in_non_terminal_state(self):
        has_agents_in_non_terminal_state = any(agent.is_in_non_terminal_state() for agent in self.__agents_container.values())
        return has_agents_in_non_terminal_state


    """------------------------------------------------------------------------------------------------
    """  
    def generate_random_action(self, agent):
        raise exp.NotImplementedError()
    
    """------------------------------------------------------------------------------------------------
    """
    def do_next_transition(self, agent, action):
        raise exp.NotImplementedError()


    """------------------------------------------------------------------------------------------------
    """ 
    def do_action(self, log_transition=False):
        if(self.has_agents_in_terminal_state()):
            self.reset()
        else:
            agent = next(self.get_agents_cycler())
            agent.do_action(log_transition=log_transition)

    def do_actions(self, n, log_transition=False):
        for i in range(0, n):
            self.do_action(log_transition=log_transition)

    """------------------------------------------------------------------------------------------------
    """ 
    def do_iteration(self, log_transition=False):
        for agent in self.get_agents():
            if(self.has_agents_in_terminal_state()):
                self.reset()
            else:
                agent.do_action(log_transition=log_transition)

    def do_iterations(self, n, log_transition=False):
        for i in range(0, n):
            self.do_iteration(log_transition=log_transition)



        


