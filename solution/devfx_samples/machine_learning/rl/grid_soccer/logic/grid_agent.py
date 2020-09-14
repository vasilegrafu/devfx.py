import numpy as np
import devfx.exceptions as exps
import devfx.machine_learning as ml

from .grid_agent_kind import GridAgentKind

"""========================================================================================================
"""
class GridAgent(ml.rl.Agent):
    def __init__(self, id, name, kind, environment, policy, randomness):
        super().__init__(id=id, name=name, kind=kind, environment=environment)
        super().set_state(None)
        super().set_policy(policy)
        self.set_randomness(randomness)

    """------------------------------------------------------------------------------------------------
    """
    def set_randomness(self, randomness):
        self.__randomness = randomness

    def get_randomness(self):
        return self.__randomness

    """------------------------------------------------------------------------------------------------
    """
    def _do_iteration(self, randomness=None):
        if(self.is_in_non_terminal_state()):
            rv = np.random.uniform(size=1)
            if(rv <= (self.get_randomness() if(randomness is None) else randomness)):
                self.do_random_action()
            else:
                self.do_optimal_action()
        elif(self.is_in_terminal_state()):
            pass  
        else:
            raise exps.NotSupportedError()