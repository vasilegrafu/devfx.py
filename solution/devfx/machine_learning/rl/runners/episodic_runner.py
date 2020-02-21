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
            self.episode_number = {}
            self.randomness = 1.0

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


    def _run(self, episode_count=1, randomness=1.0):
        running_parameters = EpisodicRunner.RunningParameters(agents=self.get_agents())
        running_parameters.episode_count = episode_count
        running_parameters.episode_number = { agent : 0 for agent in self.get_agents() }
        running_parameters.randomness = randomness

        for agent in self.get_agents():                
            agent.set_random_non_terminal_state()
            running_parameters.episode_number[agent] = 1

        while(True):
            for agent in self.get_agents():                
                if(agent.get_state().is_non_terminal()):
                    rv = np.random.uniform(size=1)
                    if(rv <= running_parameters.randomness):
                        agent.do_random_action()
                    else:
                        agent.do_action()
                else:
                    if(running_parameters.episode_number[agent] <= (running_parameters.episode_count-1)):
                        agent.set_random_non_terminal_state()
                    if(running_parameters.episode_number[agent] <= running_parameters.episode_count):
                        running_parameters.episode_number[agent] += 1

            self.running_status(source=self, signal_args=core.SignalArgs(running_parameters=running_parameters))

            if(all((running_parameters.episode_number[agent] > running_parameters.episode_count) for agent in self.get_agents())):
                break
            if(running_parameters.cancellation_token.is_cancellation_requested()):
                break


