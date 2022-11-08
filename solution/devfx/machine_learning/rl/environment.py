import numpy as np
import random as rnd
import devfx.exceptions as excps
import devfx.core as core
from .agent import Agent
from .state_kind import StateKind

class Environment(object):
    def __init__(self):
        self.__agents_container = {}

    """------------------------------------------------------------------------------------------------
    """ 
    def create(self, *args, **kwargs):
        self._create(*args, **kwargs)

    def _create(self, *args, **kwargs):
        raise excps.NotImplementedError()

    
    def setup(self, *args, **kwargs):
        return self._setup(*args, **kwargs)

    def _setup(self, *args, **kwargs):
        raise excps.NotImplementedError()     


    def destroy(self, *args, **kwargs):
        self._destroy(*args, **kwargs)

    def _destroy(self, *args, **kwargs):
        raise excps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def add_agent(self, agent):
        if(agent.get_id() in self.__agents_container):
            raise excps.ApplicationError()
        self.__agents_container[agent.get_id()] = agent
        self.on_added_agent(agent)

    def on_added_agent(self, agent):
        self._on_added_agent(agent=agent)
        
    def _on_added_agent(self, agent):
        raise excps.NotImplementedError()


    def remove_agent(self, agent):
        if(agent.get_id() not in self.__agents_container):
            raise excps.ApplicationError()
        self.__agents_container.pop(agent.get_id())
        self.on_removed_agent(agent)

    def on_removed_agent(self, agent):
        self._on_removed_agent(agent=agent)
        
    def _on_removed_agent(self, agent):
        raise excps.NotImplementedError()


    def get_agents(self):
        agents = [agent for (key, agent) in sorted(self.__agents_container.items())]
        return agents


    def get_agents_like(self, kind):
        agents = [agent for (key, agent) in sorted(self.__agents_container.items()) if(agent.get_kind() == kind)]
        return agents

    def get_agents_not_like(self, kind):
        agents = [agent for (key, agent) in sorted(self.__agents_container.items()) if(agent.get_kind() != kind)]
        return agents


    def exists_agent(self, id):
        if(id not in self.__agents_container):
            return False
        return True


    def get_agent(self, id):
        if(id not in self.__agents_container):
            raise excps.ApplicationError()
        agent = self.__agents_container[id]
        return agent

    def get_other_agents(self, id):
        agents = [agent for (key, agent) in sorted(self.__agents_container.items()) if(agent.get_id() != id)]
        return agents
           
    """------------------------------------------------------------------------------------------------
    """ 
    def do_iteration(self, agents=None):
        self._do_iteration(agents=agents)

    def _do_iteration(self, agents=None):
        if(any(agent.is_in_terminal_state() for agent in self.get_agents())):
            self.setup()
        else:
            if(agents is None):
                agents = self.get_agents()
            for agent in agents:
                agent.do_iteration()


    def do_iterations(self, n, agents=None):
        self._do_iterations(n=n, agents=agents)

    def _do_iterations(self, n, agents=None):
        for i in range(0, n):
            self.do_iteration(agents=agents)

    """------------------------------------------------------------------------------------------------
    """ 
    def get_next_state_and_reward(self, agent, action):
        is_terminal_state = agent.get_state().kind == StateKind.TERMINAL
        if(is_terminal_state):
            raise excps.ApplicationError()
        
        next_state_and_reward = self._get_next_state_and_reward(agent=agent, action=action)
        return next_state_and_reward
        
    def _get_next_state_and_reward(self, agent, action):
        raise excps.NotImplementedError()


    def get_next_state(self, agent, action):
        next_state_and_reward = self.get_next_state_and_reward(agent=agent, action=action)
        if(next_state_and_reward is None):
            return None
        (next_state, next_reward) = next_state_and_reward
        return next_state

    def get_next_reward(self, agent, action):
        next_state_and_reward = self.get_next_state_and_reward(agent=agent, action=action)
        if(next_state_and_reward is None):
            return None
        (next_state, next_reward) = next_state_and_reward
        return next_reward
        
    """------------------------------------------------------------------------------------------------
    """ 
    def get_available_actions(self, agent):
        is_terminal_state = agent.get_state().kind == StateKind.TERMINAL
        if(is_terminal_state):
            return None

        actions = self._get_available_actions(agent=agent)
        return actions

    def _get_available_actions(self, agent):
        raise excps.NotImplementedError()


    def get_random_action(self, agent):
        return self._get_random_action(agent=agent)

    def _get_random_action(self, agent):
        actions = self.get_available_actions(agent=agent)
        if(actions is None):
            return None
        
        action = rnd.choice(actions)
        return action


