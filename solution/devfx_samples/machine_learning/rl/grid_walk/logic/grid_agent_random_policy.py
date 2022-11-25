import devfx.machine_learning as ml

from .grid_agent_action_generator import GridAgentActionGenerator

class GridAgentRandomPolicy(ml.rl.RandomPolicy):
    def __init__(self):
        super().__init__()

        self.__actionGenerator = GridAgentActionGenerator()

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_action(self, state):
        action = self.__actionGenerator.get_random()
        return action

        