import numpy as np
import devfx.exceptions as exps
import devfx.core as core
from .agent import Agent
from .state_kind import StateKind

class Environment(object):
    def __init__(self):
        self.__agents_container = {}

        self.running_status = core.SignalHandlers()

    """------------------------------------------------------------------------------------------------
    """ 
    def create_agent(self, id, kind, state, policy):
        agent = Agent(id=id, kind=kind, environment=self, state=state, policy=policy)
        self.__agents_container[id] = agent

    def get_agents(self, kind=None):
        if(kind is None):
            agents = [agent for agent in self.__agents_container.values()]
            return agents
        else:
            agents = [agent for agent in self.__agents_container.values() if(agent.kind == kind)]
            if(len(agents) == 0):
                return None
            else:
                return agents

    def get_other_agents(self, id, kind=None):
        if(kind is None):
            agents = [agent for agent in self.__agents_container.values() if(agent.id != id)]
            return agents
        else:
            agents = [agent for agent in self.__agents_container.values() if((agent.id != id) and (agent.kind == kind))]
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


    def get_random_non_terminal_state(self, agent_kind):
        return self._get_random_non_terminal_state(agent_kind=agent_kind)

    def _get_random_non_terminal_state(self, agent_kind):
        raise exps.NotImplementedError()


    def get_random_terminal_state(self, agent_kind):
        return self._get_random_terminal_state(agent_kind=agent_kind)

    def _get_random_terminal_state(self, agent_kind):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_state_kind(self, agent_kind, state):
        return self._get_state_kind(agent_kind=agent_kind, state=state)

    def _get_state_kind(self, agent_kind, state):
        raise exps.NotImplementedError()


    def is_in_non_terminal_state(self, agent_kind, state):
        state_kind = self.get_state_kind(agent_kind=agent_kind, state=state)
        is_in_non_terminal_state = state_kind == StateKind.NON_TERMINAL
        return is_in_non_terminal_state
        
    def is_in_terminal_state(self, agent_kind, state):
        state_kind = self.get_state_kind(agent_kind=agent_kind, state=state)
        is_in_terminal_state = state_kind == StateKind.TERMINAL
        return is_in_terminal_state

    """------------------------------------------------------------------------------------------------
    """ 
    def get_next_state(self, agent_kind, state, action):
        next_state = self._get_next_state(agent_kind=agent_kind, state=state, action=action)
        return next_state
        
    def _get_next_state(self, agent_kind, state, action):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_reward(self, agent_kind, state):
        reward = self._get_reward(agent_kind=agent_kind, state=state)
        return reward
        
    def _get_reward(self, agent_kind, state):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_random_action(self, agent_kind, state):
        return self._get_random_action(agent_kind=agent_kind, state=state)

    def _get_random_action(self, agent_kind, state):
        raise exps.NotImplementedError()
