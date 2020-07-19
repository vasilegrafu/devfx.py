import numpy as np
import devfx.exceptions as exps
import devfx.core as core
from .agent import Agent
from .state_kind import StateKind

class Environment(object):
    def __init__(self):
        self.__agents_container = {}

    """------------------------------------------------------------------------------------------------
    """ 
    def create_agent(self, id, kind, state, policy):
        agent = Agent(id=id, kind=kind, environment=self, state=state, policy=policy)
        self.__agents_container[id] = agent

    def get_agents(self, kind=None):
        if(kind is None):
            agents = [agent for agent in self.__agents_container.values()]
        else:
            agents = [agent for agent in self.__agents_container.values() if(agent.get_kind() == kind)]
        if(len(agents) == 0):
            return None
        else:
            return agents

    def get_other_agents(self, id, kind=None):
        if(kind is None):
            agents = [agent for agent in self.__agents_container.values() if(agent.id != id)]
        else:
            agents = [agent for agent in self.__agents_container.values() if((agent.get_kind() == kind) and (agent.id != id))]
        if(len(agents) == 0):
            return None
        else:
            return agents

    def exists_agent(self, id):
        if(id not in self.__agents_container):
            return False
        return True

    def get_agent(self, id):
        if(id not in self.__agents_container):
            raise exps.ApplicationError()
        agent = self.__agents_container[id]
        return agent

    def destroy_agent(self, id):
        if(id not in self.__agents_container):
            raise exps.ApplicationError()
        self.__agents_container.pop(id)
        
    """------------------------------------------------------------------------------------------------
    """
    def get_random_state(self, agent_kind):
        return self._get_random_state(agent_kind=agent_kind)

    def _get_random_state(self, agent_kind):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_next_state_and_reward(self, agent_kind, state, action):
        is_terminal_state = state.kind == StateKind.TERMINAL
        if(is_terminal_state):
            raise exps.ApplicationError()
        
        next_state_and_reward = self._get_next_state_and_reward(agent_kind=agent_kind, state=state, action=action)
        return next_state_and_reward
        
    def _get_next_state_and_reward(self, agent_kind, state, action):
        raise exps.NotImplementedError()


    def get_next_state(self, agent_kind, state, action):
        next_state_and_reward = self.get_next_state_and_reward(agent_kind=agent_kind, state=state, action=action)
        if(next_state_and_reward is None):
            return None
        (next_state, next_reward) = next_state_and_reward
        return next_state

    def get_next_reward(self, agent_kind, state, action):
        next_state_and_reward = self.get_next_state_and_reward(agent_kind=agent_kind, state=state, action=action)
        if(next_state_and_reward is None):
            return None
        (next_state, next_reward) = next_state_and_reward
        return next_reward
        
    """------------------------------------------------------------------------------------------------
    """ 
    def get_random_action(self, agent_kind, state):
        is_terminal_state = state.kind == StateKind.TERMINAL
        if(is_terminal_state):
            raise exps.ApplicationError()

        action = self._get_random_action(agent_kind=agent_kind, state=state)
        return action

    def _get_random_action(self, agent_kind, state):
        raise exps.NotImplementedError()

