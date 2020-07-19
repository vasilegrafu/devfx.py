import numpy as np
import devfx.exceptions as exps
import devfx.core as core
from ..state_kind import StateKind
from .runner import Runner

class TrainingRunner(Runner):
    def __init__(self, agents):
        super().__init__(agents=agents)

    """------------------------------------------------------------------------------------------------
    """
    class RunningParameters(Runner.RunningParameters):
        def __init__(self, agents):
            super().__init__(agents=agents)
            self.randomness = 1.0

        @property
        def randomness(self):
            return self.__randomness

        @randomness.setter
        def randomness(self, value):
            self.__randomness = value

    """------------------------------------------------------------------------------------------------
    """
    def _run(self, randomness=1.0):
        running_parameters = TrainingRunner.RunningParameters(agents=super().get_agents())
        running_parameters.randomness = randomness

        for agent in self.get_agents():                
            agent.set_random_state()

        while(True):
            for agent in super().get_agents():   
                if(agent.get_state().kind == StateKind.NON_TERMINAL):
                    rv = np.random.uniform(size=1)
                    if(rv <= running_parameters.randomness):
                        agent.do_random_action()
                    else:
                        agent.do_optimal_action()
                elif(agent.get_state().kind == StateKind.TERMINAL):
                    agent.set_random_state() 
                else:
                    raise exps.NotSupportedError()

            super().running_status(source=self, event_args=core.EventArgs(running_parameters=running_parameters))

            if(running_parameters.cancellation_token.is_cancellation_requested()):
                break


