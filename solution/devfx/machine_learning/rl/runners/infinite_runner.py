import numpy as np
import devfx.exceptions as exps
import devfx.core as core
from .runner import Runner

class InfiniteRunner(Runner):
    def __init__(self, agents):
        super().__init__(agents=agents)

    """------------------------------------------------------------------------------------------------
    """
    class RunningParameters(Runner.RunningParameters):
        def __init__(self, agents):
            super().__init__(agents=agents)
            self.episode_number = 0
            self.randomness = 1.0

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


    def _run(self, randomness=1.0):
        if(not all(agent.get_state().is_non_terminal() for agent in self.get_agents())):
            raise exps.ApplicationError()

        running_parameters = InfiniteRunner.RunningParameters(agents=self.get_agents())
        running_parameters.episode_number = { agent : 1 for agent in self.get_agents() }
        running_parameters.randomness = randomness

        while(True):
            for agent in self.get_agents():                
                if(agent.get_state().is_non_terminal()):
                    rv = np.random.uniform(size=1)
                    if(rv <= running_parameters.randomness):
                        agent.do_random_action()
                    else:
                        agent.do_action()
                else:
                    agent.set_random_non_terminal_state()
                    running_parameters.episode_number[agent] += 1
                    
            self.running_status(source=self, signal_args=core.SignalArgs(running_parameters=running_parameters))

            if(running_parameters.cancellation_token.is_cancellation_requested()):
                break


