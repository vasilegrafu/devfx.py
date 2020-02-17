import numpy as np
import devfx.exceptions as exps
import devfx.core as core
from ..agent import Agent

class EpisodicRunner(object):
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
            self.episode_count = None
            self.episode_number = None
            self.randomness = None

        @property
        def episode_count(self):
            return self.__episode_count

        @episode_count.setter
        def episode_count(self, value):
            self.__episode_count = value


        @property
        def episode_number(self):
            return self.__episode_number

        @episode_number.setter
        def episode_number(self, value):
            self.__episode_number = value


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


    def run(self, episode_count=1, randomness=1.0):
        running_parameters = EpisodicRunner.RunningParameters()
        running_parameters.episode_count = episode_count if(episode_count is not None) else 1024**4
        running_parameters.episode_number = { id(agent) : 0 for agent in self.get_agents() }
        running_parameters.randomness = randomness
        running_parameters.cancellation_token = EpisodicRunner.RunningCancellationToken()

        while(True):
            for agent in self.get_agents():
                if(agent.get_state().is_non_terminal()):
                    rv = np.random.uniform(size=1)
                    if(rv <= running_parameters.randomness):
                        agent.do_random_action()
                    else:
                        agent.do_action()
                else:
                    running_parameters.episode_number[id(agent)] += 1

        while(running_parameters.episode_number < running_parameters.episode_count):
            while(not running_parameters.cancellation_token.is_cancellation_requested()):
                
                    if(agent.get_state().is_non_terminal()):
                        rv = np.random.uniform(size=1)
                        if(rv <= running_parameters.randomness):
                            agent.do_random_action()
                        else:
                            agent.do_action()


            running_parameters.episode_number += 1
            self.running_status(source=self, signal_args=core.SignalArgs(running_parameters=running_parameters))
