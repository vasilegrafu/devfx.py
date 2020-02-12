import devfx.exceptions as exps
from .agent import Agent

class Environment(object):
    def __init__(self):
        self.set_agents(agents=[])

    """------------------------------------------------------------------------------------------------
    """ 
    def set_agents(self, agents):
        self.__agents = agents

    def get_agents(self, filter=None):
        if(filter is None):
            return self.__agents
        else:
            return [agent for agent in self.__agents if(filter(agent))] 

    """------------------------------------------------------------------------------------------------
    """
    def create_agent(self, name, state, policy=None):
        agent = Agent(name=name, environment=self, state=state, policy=policy)
        self.get_agents().append(agent)
        return agent

    def create_agent_of_type(self, agent_type, name, state, policy=None):
        agent = agent_type(name=name, environment=self, state=state, policy=policy)
        self.get_agents().append(agent)
        return agent 

    def destroy_agent(self, agent):
        self.get_agents().remove(agent)
        agent.set_environment(environment=None)

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


        



