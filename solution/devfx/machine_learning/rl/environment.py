import numpy as np
import devfx.exceptions as exps
import devfx.core as core
from .agent import Agent

class Environment(object):
    def __init__(self):
        self.__agents_container = {}

        self.running_status = core.SignalHandlers()

    """------------------------------------------------------------------------------------------------
    """ 
    def create_agent(self, id, kind, state, policy):
        agent = Agent(id=id, kind=kind, environment=self, state=state, policy=policy)
        self.__agents_container[id] = agent

    def get_agents(self):
        return [agent for agent in self.__agents_container.values()]

    def get_agent(self, id):
        if(id not in self.__agents_container):
            raise exps.ApplicationError()
        agent = self.__agents_container[id]
        return agent

    def get_other_agents(self, id):
        if(id not in self.__agents_container):
            raise exps.ApplicationError()
        other_agents = [self.__agents_container[agent_id] for agent_id in self.__agents_container.keys() if(agent_id != id)]
        return other_agents

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
    def get_next_state_and_reward(self, agent, action):
        (next_state, reward) = self._get_next_state_and_reward(agent=agent, action=action)
        return (next_state, reward)
        
    def _get_next_state_and_reward(self, agent, action):
        raise exps.NotImplementedError()


    def get_random_action(self, agent):
        return self._get_random_action(agent=agent)

    def _get_random_action(self, agent):
        raise exps.NotImplementedError()
