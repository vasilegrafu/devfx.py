import devfx.machine_learning as ml

from .grid_agent_action_generator import GridAgentActionGenerator

class GridAgentRandomPolicy(ml.rl.RandomPolicy):
    def __init__(self):
        super().__init__()

        self.__setup_action_cenerator()

    """------------------------------------------------------------------------------------------------
    """
    def __setup_action_cenerator(self):
        self.__action_generator = GridAgentActionGenerator()

    def __get_action_cenerator(self):
        return self.__action_generator

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_action(self, state):
        action = self.__get_action_cenerator().get_random()
        return action

        