import numpy as np
import devfx.exceptions as exps
import devfx.core as core
from .runner import Runner

class StepRunner(Runner):
    def __init__(self, agents):
        super().__init__(agents=agents)

    """------------------------------------------------------------------------------------------------
    """
    class RunningParameters(Runner.RunningParameters):
        def __init__(self, agents):
            super().__init__(agents=agents)
            self.step_count = 0
            self.step_number = {}
            self.randomness = 1.0

        @property
        def step_count(self):
            return self.__step_count

        @step_count.setter
        def step_count(self, value):
            self.__step_count = value


        @property
        def step_number(self):
            return self.__step_number

        @step_number.setter
        def step_number(self, value):
            self.__step_number = value


        @property
        def randomness(self):
            return self.__randomness

        @randomness.setter
        def randomness(self, value):
            self.__randomness = value


    def _run(self, step_count=1, randomness=1.0):
        running_parameters = StepRunner.RunningParameters(agents=self.get_agents())
        running_parameters.step_count = step_count
        running_parameters.step_number = { agent : 0 for agent in self.get_agents() }
        running_parameters.randomness = randomness

        for agent in self.get_agents():                
            agent.set_random_non_terminal_state()

        while(True):
            for agent in self.get_agents():                
                if(agent.is_in_non_terminal_state()):
                    if(running_parameters.step_number[agent] <= (running_parameters.step_count-1)):
                        rv = np.random.uniform(size=1)
                        if(rv <= running_parameters.randomness):
                            agent.do_random_action()
                        else:
                            agent.do_action()
                        running_parameters.step_number[agent] += 1
                else:
                    agent.set_random_non_terminal_state()

            self.running_status(source=self, signal_args=core.SignalArgs(running_parameters=running_parameters))

            if(all((running_parameters.step_number[agent] >= running_parameters.step_count) for agent in self.get_agents())):
                break
            if(running_parameters.cancellation_token.is_cancellation_requested()):
                break


