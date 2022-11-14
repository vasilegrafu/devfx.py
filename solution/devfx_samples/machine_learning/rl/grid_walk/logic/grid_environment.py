import numpy as np
import random as rnd
import itertools as it
import devfx.core as core
import devfx.exceptions as excps
import devfx.machine_learning as ml


from .grid_agent_action_generator import GridAgentActionGenerator
from .grid_agent_kind import GridAgentKind
from .grid_agent import GridAgent

"""========================================================================================================
"""
class GridEnvironment(ml.rl.Environment):
    def __init__(self):
        super().__init__()

        self.__shape = (8, 8)
        self.__cells = None

        self.__actionGenerator = GridAgentActionGenerator()

    """------------------------------------------------------------------------------------------------
    """
    @property
    def shape(self):  
        return self.__shape

    @property
    def cells(self):
        return self.__cells

    """------------------------------------------------------------------------------------------------
    """
    def _create(self):
        cells = {}
        for (r, c) in it.product(range(1, self.shape[0]+1), range(1, self.shape[1]+1)):
            if((r == 1) or (r == self.shape[0]) or (c == 1) or (c == self.shape[1])):
                (ci, cc) = (ml.rl.Data([r, c]), ml.rl.Data([ml.rl.StateKind.UNDEFINED, -1.0]))
            elif((r, c) in [(3, 3), (4, 4), (6, 6)]):
                (ci, cc) = (ml.rl.Data([r, c]), ml.rl.Data([ml.rl.StateKind.UNDEFINED, -1.0]))
            elif((r, c) in [(2, 7)]):
                (ci, cc) = (ml.rl.Data([r, c]), ml.rl.Data([ml.rl.StateKind.TERMINAL, +1.0]))
            elif((r, c) in [(3, 7)]):
                (ci, cc) = (ml.rl.Data([r, c]), ml.rl.Data([ml.rl.StateKind.TERMINAL, -1.0]))
            else:
                (ci, cc) = (ml.rl.Data([r, c]), ml.rl.Data([ml.rl.StateKind.NON_TERMINAL, 0.0]))
            cells[ci] = cc
        self.__cells = cells

    """------------------------------------------------------------------------------------------------
    """
    def _setup(self, iteration_randomness=None):
        if(not self.exists_agent(id=1)):
            self.add_agent(GridAgent(id=1, 
                                     name='Johnny Walker 1', 
                                     kind=GridAgentKind.WALKER, 
                                     environment=self, 
                                     state=self.__get_initial_state(),
                                     policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=1e-1),
                                     iteration_randomness= 0.1 if iteration_randomness is None else iteration_randomness))
        else:
            self.get_agent(id=1).set_state(self.__get_initial_state())

    def _on_added_agent(self, agent):
        pass

    def _on_removed_agent(self, agent):
        pass

    """------------------------------------------------------------------------------------------------
    """
    def __get_initial_state(self):
        ci = rnd.choice([ci for ci in self.cells if(self.cells[ci][0] == ml.rl.StateKind.NON_TERMINAL)])
        state = ml.rl.State(self.cells[ci][0], ci)
        return state

    def _get_next_state_and_reward(self, agent, action):
        state = agent.get_state()
        next_ci = ml.rl.Data(state.value + action.value)
        if(self.cells[next_ci][0] == ml.rl.StateKind.UNDEFINED):
            next_state = state
        else:
            next_state = ml.rl.State(self.cells[next_ci][0], next_ci)
        next_reward = ml.rl.Reward(self.cells[next_ci][1])
        return (next_state, next_reward)

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_action(self, agent):
        action = self.__actionGenerator.get_random()
        return action





