import threading
import numpy as np
import random as rnd
import devfx.exceptions as ex
import devfx.core as core
from .agent import Agent
from .state_kind import StateKind

class Environment(object):
    def __init__(self):
        self.__setup_agents_container()

    """------------------------------------------------------------------------------------------------
    """    
    def setup(self, *args, **kwargs):
        return self._setup(*args, **kwargs)

    def _setup(self, *args, **kwargs):
        pass   


    def reset(self, *args, **kwargs):
        return self._reset(*args, **kwargs)

    def _reset(self, *args, **kwargs):
        pass 
    

    def cleanup(self, *args, **kwargs):
        return self._cleanup(*args, **kwargs)

    def _cleanup(self, *args, **kwargs):
        pass 

    """------------------------------------------------------------------------------------------------
    """ 
    def __setup_agents_container(self):
        self.__agents_container = {}

    """------------------------------------------------------------------------------------------------
    """ 
    def add_agents(self, agents):
        for agent in agents:
            if(agent.get_id() in self.__agents_container):
                raise ex.ApplicationError()
            
        for agent in agents:
            self.__agents_container[agent.get_id()] = agent
            agent.set_environment(environment=self)
            
        self._on_added_agents(agents=agents)
       
    def _on_added_agents(self, agents):
        pass


    def remove_agents(self, agents=None):
        if(agents is None):
            agents = self.__agents_container
            
        for agent in agents:    
            if(agent.get_id() not in self.__agents_container):
                raise ex.ApplicationError()
            
        for agent in agents: 
            self.__agents_container.pop(agent.get_id())
            agent.set_environment(environment=None)

        self._on_removed_agents(agents=agents)
       
    def _on_removed_agents(self, agents):
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
            raise ex.ApplicationError()
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
    def do_action(self, agent, action = None, log_transition=False):
        transition = agent.do_action(action=action, log_transition=log_transition)
        return transition

    """------------------------------------------------------------------------------------------------
    """    
    def do_next_transition(self, agent, action):
        is_terminal_state = agent.is_in_terminal_state()
        if(is_terminal_state):
            return None
        
        (reward, next_state) = self._do_next_transition(agent=agent, action=action)

        return (reward, next_state)
        
    def _do_next_transition(self, agent, action):
        raise ex.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def do_iteration(self, log_transition=False):
        self._do_iteration(log_transition=log_transition)

    def _do_iteration(self, log_transition=False):
        for agent in self.get_agents():
            if(self.has_agents_in_terminal_state()):
                self.reset()
            else:
                self.do_action(agent=agent, log_transition=log_transition)


    def do_iterations(self, n, log_transition=False):
        self._do_iterations(n=n, log_transition=log_transition)

    def _do_iterations(self, n, log_transition=False):
        for i in range(0, n):
            self.do_iteration(log_transition=log_transition)

    """------------------------------------------------------------------------------------------------
    """  
    def clear_logged_transitions(self):
        agents = self.get_agents()
        for agent in agents:
            agent.clear_logged_transitions()

    def learn_from_logged_transitions(self, environment, clear_logged_transitions=True):
        to_agents = self.get_agents()
        from_agents = environment.get_agents()
        
        if(len(to_agents) != len(from_agents)):
            raise ex.ApplicationError()
        
        to_agents = sorted(to_agents, key=lambda agent: agent.get_id())
        from_agents = sorted(from_agents, key=lambda agent: agent.get_id())
        
        for (to_agent, from_agent) in zip(to_agents, from_agents):
            to_agent.learn(transitions=from_agent.get_logged_transitions())
            if(clear_logged_transitions == True):
                from_agent.clear_logged_transitions()
        


