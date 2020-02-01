import devfx.exceptions as exps
from .agent import Agent

class Environment(object):
    def __init__(self):
        self.set_agents(agents=[])

    """------------------------------------------------------------------------------------------------
    """ 
    def set_agents(self, agents):
        self.__agents = agents

    def get_agents(self):
        return self.__agents

    """------------------------------------------------------------------------------------------------
    """
    def get_random_state(self):
        return self._get_random_state()

    def _get_random_state(self):
        raise exps.NotImplementedError()


    def get_random_non_terminal_state(self):
        return self._get_random_non_terminal_state()

    def _get_random_non_terminal_state(self):
        raise exps.NotImplementedError()


    def get_random_terminal_state(self):
        return self._get_random_terminal_state()

    def _get_random_terminal_state(self):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def get_next_state(self, state, action):
        next_state = self._get_next_state(state=state, action=action)
        return next_state
        
    def _get_next_state(self, state, action):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """
    def get_random_action(self, state):
        return self._get_random_action(state=state)

    def _get_random_action(self, state):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """
    def create_agent(self, agent_type, *args, **kwargs):
        agent = agent_type(environment=self, *args, **kwargs)
        self.get_agents().append(agent)
        return agent

    def destroy_agent(self, agent):
        self.get_agents().remove(agent)
        agent.set_environment(environment=None)
        



