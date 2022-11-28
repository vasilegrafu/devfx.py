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
            agents = self.get_agents()
            
        for agent in agents:    
            if(agent.get_id()not in self.__agents_container):
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
    

    def exists_agent(self, id):
        return id in self.__agents_container

    
    def get_agent(self, id):
        if(id not in self.__agents_container):
            raise ex.ApplicationError()
        agent = self.__agents_container[id]
        return agent

    def get_agents_others_than(self, id):
        agents = [agent for agent in self.__agents_container.values() if(agent.get_id()!= id)]
        return agents


    def get_agents_of_kind(self, kind):
        agents = [agent for agent in self.__agents_container.values() if(agent.get_kind() == kind)]
        return agents

    def get_agents_not_of_kind(self, kind):
        agents = [agent for agent in self.__agents_container.values() if(agent.get_kind() != kind)]
        return agents

    """------------------------------------------------------------------------------------------------
    """ 
    def do_iteration(self, agents=None, log_transition=False):
        self._do_iteration(agents=agents, log_transition=log_transition)

    def _do_iteration(self, agents=None, log_transition=False):
        if(agents is None):
            agents = self.get_agents()
    
        if(any(agent.is_in_terminal_state() for agent in agents)):
            self.reset()
        else:
            for agent in agents:
                agent.do_action(log_transition=log_transition)

    def do_iterations(self, n, agents=None, log_transition=False):
        self._do_iterations(n=n, agents=agents, log_transition=log_transition)

    def _do_iterations(self, n, agents=None, log_transition=False):
        for i in range(0, n):
            self.do_iteration(agents=agents, log_transition=log_transition)

    """------------------------------------------------------------------------------------------------
    """    
    def do_action(self, agent, action):
        is_terminal_state = agent.is_in_terminal_state()
        if(is_terminal_state):
            raise ex.ApplicationError()
        
        (reward, next_state) = self._do_action(agent=agent, action=action)

        return (reward, next_state)
        
    def _do_action(self, agent, action):
        raise ex.NotImplementedError()



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
        


