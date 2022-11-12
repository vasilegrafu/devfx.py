import numpy as np
import random as rnd
import itertools as it
import devfx.core as core
import devfx.exceptions as excps
import devfx.data_structures as ds
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
        cells = ds.dict()
        for (ri, ci) in it.product(range(1, self.shape[0]+1), range(1, self.shape[1]+1)):
            if((ri == 1) or (ri == self.shape[0]) or (ci == 1) or (ci == self.shape[1])):
                (cell_index, cell_content) = (np.array([ri, ci]), np.array([ml.rl.StateKind.UNDEFINED, -1.0]))
            elif((ri, ci) in [(3, 3), (4, 4), (6, 6)]):
                (cell_index, cell_content) = (np.array([ri, ci]), np.array([ml.rl.StateKind.UNDEFINED, -1.0]))
            elif((ri, ci) in [(2, 7)]):
                (cell_index, cell_content) = (np.array([ri, ci]), np.array([ml.rl.StateKind.TERMINAL, +1.0]))
            elif((ri, ci) in [(3, 7)]):
                (cell_index, cell_content) = (np.array([ri, ci]), np.array([ml.rl.StateKind.TERMINAL, -1.0]))
            else:
                (cell_index, cell_content) = (np.array([ri, ci]), np.array([ml.rl.StateKind.NON_TERMINAL, 0.0]))
            cells[cell_index] = cell_content
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

    def __get_initial_state(self):
        choosable_cell_indexes = [cell_index for cell_index in self.cells 
                                             if(self.cells[cell_index][0] == ml.rl.StateKind.NON_TERMINAL)]
        cell_index = rnd.choice(choosable_cell_indexes)
        state = ml.rl.State(value=cell_index, kind=self.cells[cell_index][0])
        return state

    """------------------------------------------------------------------------------------------------
    """
    def _get_next_state_and_reward(self, agent, action):
        agent_state = agent.get_state()
        agent_next_cell_index = agent_state.value + action.value

        if(self.cells[agent_next_cell_index][0] == ml.rl.StateKind.UNDEFINED):
            agent_next_state = agent_state
            agent_next_reward = ml.rl.Reward(value=self.cells[agent_next_cell_index][1])
            return (agent_next_state, agent_next_reward)

        agent_next_state = ml.rl.State(value=agent_next_cell_index, kind=self.cells[agent_next_cell_index][0])
        agent_next_reward = ml.rl.Reward(value=self.cells[agent_next_cell_index][1])
        return (agent_next_state, agent_next_reward)

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_action(self, agent):
        action = GridAgentActionGenerator().get_random()
        return action





