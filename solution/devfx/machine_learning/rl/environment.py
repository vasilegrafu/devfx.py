import numpy as np
import devfx.exceptions as exps
import devfx.core as core
from .agent import Agent

class Environment(object):
    def __init__(self):
        self.set_agents(agents=[])

        self.training_agent_status = core.SignalHandlers()

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

    """------------------------------------------------------------------------------------------------
    """
    @property
    def training_agent_status(self):
        return self.__training_agent_status

    @training_agent_status.setter
    def training_agent_status(self, signal_handlers):
        self.__training_agent_status = signal_handlers


    class TrainingParameters(object):
        def __init__(self):
            self.agent = None
            self.action_count = None
            self.action_number = None
            self.epsilon = None

        @property
        def action_count(self):
            return self.__action_count

        @action_count.setter
        def action_count(self, value):
            self.__action_count = value


        @property
        def action_number(self):
            return self.__action_number

        @action_number.setter
        def action_number(self, value):
            self.__action_number = value


        @property
        def epsilon(self):
            return self.__epsilon

        @epsilon.setter
        def epsilon(self, value):
            self.__epsilon = value


    def train(self, action_count, epsilon):
        training_parameters = Environment.TrainingParameters()
        training_parameters.action_count = action_count
        training_parameters.action_number = 0
        training_parameters.epsilon = epsilon

        while(training_parameters.action_number < training_parameters.action_count):
            for agent in self.get_agents():
                if(agent.get_state().is_non_terminal()):
                    rv = np.random.uniform(size=1)
                    if(rv <= training_parameters.epsilon):
                        agent.do_random_action()
                    else:
                        agent.do_action()
                else:
                    agent.set_state(state=self.get_random_non_terminal_state())

                training_parameters.action_number += 1
                self.training_status(source=self, signal_args=core.SignalArgs(training_parameters=training_parameters, agent=agent))