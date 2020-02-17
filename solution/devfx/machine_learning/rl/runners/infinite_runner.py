import numpy as np
import devfx.exceptions as exps
import devfx.core as core
from ..agent import Agent

class Runner(object):
    def __init__(self, agents):
        self.__set_agents(agents=agents)

        self.running_status = core.SignalHandlers()

    """------------------------------------------------------------------------------------------------
    """ 
    def __set_agents(self, agents):
        self.__agents = agents
                
    def get_agents(self):
        return self.__agents

    """------------------------------------------------------------------------------------------------
    """
    @property
    def running_status(self):
        return self.__running_status

    @running_status.setter
    def running_status(self, signal_handlers):
        self.__running_status = signal_handlers


    class RunningCancellationToken(object):
        def __init__(self):
            self.__is_cancellation_requested = False

        def request_cancellation(self, condition=None):
            if (condition is None):
                self.__is_cancellation_requested = True
            elif (condition is not None):
                if(condition):
                    self.__is_cancellation_requested = True
            else:
                raise exps.NotSupportedError()

        def is_cancellation_requested(self):
            return (self.__is_cancellation_requested == True)


    class RunningParameters(object):
        def __init__(self):
            self.agent = None
            self.action_count = None
            self.action_number = None
            self.randomness = None

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
        def randomness(self):
            return self.__randomness

        @randomness.setter
        def randomness(self, value):
            self.__randomness = value


        @property
        def cancellation_token(self):
            return self.__cancellation_token

        @cancellation_token.setter
        def cancellation_token(self, value):
            self.__cancellation_token = value


    def run(self, randomness=1.0, action_count=None):
        running_parameters = Runner.RunningParameters()
        running_parameters.action_count = action_count if(action_count is not None) else 1024**4
        running_parameters.action_number = 0
        running_parameters.randomness = randomness
        running_parameters.cancellation_token = Runner.RunningCancellationToken()

        while((not running_parameters.cancellation_token.is_cancellation_requested()) and (running_parameters.action_number < running_parameters.action_count)):
            for agent in self.get_agents():
                if(agent.get_state().is_non_terminal()):
                    rv = np.random.uniform(size=1)
                    if(rv <= running_parameters.randomness):
                        agent.do_random_action()
                    else:
                        agent.do_action()
                else:
                    agent.set_random_non_terminal_state()

                running_parameters.action_number += 1
                self.running_status(source=self, signal_args=core.SignalArgs(running_parameters=running_parameters, agent=agent))
