import numpy as np
import devfx.exceptions as exps
import devfx.core as core
from .runner import Runner

class EpisodicRunner(Runner):
    def __init__(self, agents):
        super().__init__(agents=agents)

    """------------------------------------------------------------------------------------------------
    """
    class RunningParameters(Runner.RunningParameters):
        def __init__(self, agents):
            super().__init__(agents=agents)
            self.episode_count = 0
            self.episode_number = 0
            self.randomness = 1.0

        @property
        def episode_count(self):
            return self.__episode_count

        @episode_count.setter
        def episode_count(self, value):
            self.__episode_count = value


        @property
        def episode_numbers(self):
            return self.__episode_numbers

        @episode_numbers.setter
        def episode_numbers(self, value):
            self.__episode_numbers = value


        @property
        def randomness(self):
            return self.__randomness

        @randomness.setter
        def randomness(self, value):
            self.__randomness = value


    def _run(self, episode_count=1, randomness=1.0):
        running_parameters = EpisodicRunner.RunningParameters(agents=self.get_agents())
        running_parameters.episode_count = episode_count
        running_parameters.episode_numbers = { agent : 0 for agent in self.get_agents() }
        running_parameters.randomness = randomness

        while(not running_parameters.cancellation_token.is_cancellation_requested()):
            for agent in self.get_agents():
                if(running_parameters.episode_numbers[agent] <= running_parameters.episode_count):
                    if(agent.get_state().is_non_terminal()):
                        rv = np.random.uniform(size=1)
                        if(rv <= running_parameters.randomness):
                            agent.do_random_action()
                        else:
                            agent.do_action()
                    else:
                        running_parameters.episode_numbers[agent] += 1

                    self.running_status(source=self, signal_args=core.SignalArgs(running_parameters=running_parameters, agent=agent))

