import numpy as np
import itertools as it
import devfx.exceptions as exps
import devfx.machine_learning as ml
from .grid_actions import GridActions

"""========================================================================================================
"""
class GridEnvironment(ml.rl.Environment):
    def __init__(self):
        super().__init__()

        self.grid_shape=(5, 5)
        self.grid_cells_blocked = [(2, 2), (3, 3), (5, 5)]

        self.terminal_states = [(1, 5), (2, 5)]
        self.states_with_reward = {(1, 5):+1.0, (2, 5):-1.0}

    """------------------------------------------------------------------------------------------------
    """
    def __get_cells_generator(self):
        for (ri, ci) in it.product(range(1, self.grid_shape[0]+1), range(1, self.grid_shape[1]+1)):
            if((ri, ci) in self.grid_cells_blocked):
                (cell_index, cell_content) = ((ri, ci), None)
                yield (cell_index, cell_content)
            else:
                (cell_index, cell_content) = ((ri, ci), ())
                yield (cell_index, cell_content)

    def get_cells(self):
        return [(cell_index, cell_content) for (cell_index, cell_content) in self.__get_cells_generator()]

    def get_shape(self):
        return self.grid_shape

    def __get_non_blocked_cells_generator(self):
        return ((cell_index, cell_content) for (cell_index, cell_content) in self.__get_cells_generator() if(cell_content is not None))

    def __get_blocked_cells_generator(self):
        return ((cell_index, cell_content) for (cell_index, cell_content) in self.__get_cells_generator() if(cell_content is None))

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_state(self, agent_kind):
        cell_indexes = [cell_index for (cell_index, cell_content) in self.__get_non_blocked_cells_generator()]
        cell_index = cell_indexes[np.random.choice(len(cell_indexes))]
        state = ml.rl.State(value=cell_index)
        return state

    def _get_random_non_terminal_state(self, agent_kind):
        cell_indexes = [cell_index for (cell_index, cell_content) in self.__get_non_blocked_cells_generator() if(cell_content not in self.terminal_states)]
        cell_index = cell_indexes[np.random.choice(len(cell_indexes))]
        state = ml.rl.State(value=cell_index)
        return state

    def _get_random_terminal_state(self, agent_kind):
        cell_indexes = [cell_index for (cell_index, cell_content) in self.__get_non_blocked_cells_generator() if(cell_content in self.terminal_states)]
        cell_index = cell_indexes[np.random.choice(len(cell_indexes))]
        state = ml.rl.State(value=cell_index)
        return state

    """------------------------------------------------------------------------------------------------
    """
    def _get_state_kind(self, agent_kind, state):
        if(state.value not in self.terminal_states):
            return ml.rl.StateKind.NON_TERMINAL
        else:
            return ml.rl.StateKind.TERMINAL

    """------------------------------------------------------------------------------------------------
    """
    def _get_next_state(self, agent_kind, state, action):
        cell_index = state.value
        if(action == GridActions.Left):
            next_cell_index = (cell_index[0], cell_index[1]-1)
        if(action == GridActions.Right):
            next_cell_index = (cell_index[0], cell_index[1]+1)
        if(action == GridActions.Up):
            next_cell_index = (cell_index[0]-1, cell_index[1])
        if(action == GridActions.Down):
            next_cell_index = (cell_index[0]+1, cell_index[1])
        if(action == GridActions.Stay):
            next_cell_index = (cell_index[0], cell_index[1])
        next_state = ml.rl.State(value=next_cell_index)
        return next_state

    """------------------------------------------------------------------------------------------------
    """
    def _get_reward(self, agent_kind, state):
        cell_index = state.value
        if(cell_index not in self.states_with_reward):
            reward = ml.rl.Reward(value=0.0)
        else:
            reward = ml.rl.Reward(self.states_with_reward[cell_index])
        return reward

    """------------------------------------------------------------------------------------------------
    """
    def __get_actions_generator(self, agent_kind, state):
        state_kind = self.get_state_kind(agent_kind=agent_kind, state=state)
        if(state_kind == ml.rl.StateKind.TERMINAL):
            return
        cell_index = state.value
        indexed_cells = {cell_index:cell_content for (cell_index, cell_content) in self.__get_cells_generator()}
        if((cell_index[0] > 1) and indexed_cells[cell_index[0]-1, cell_index[1]] is not None):
            yield GridActions.Up
        if((cell_index[0] < self.get_shape()[0]) and (indexed_cells[cell_index[0]+1, cell_index[1]] is not None)):
            yield GridActions.Down
        if((cell_index[1] > 1) and (indexed_cells[cell_index[0], cell_index[1]-1] is not None)):
            yield GridActions.Left
        if((cell_index[1] < self.get_shape()[1]) and indexed_cells[cell_index[0], cell_index[1]+1] is not None):
            yield GridActions.Right     
        yield GridActions.Stay   

    def _get_random_action(self, agent_kind, state):
        actions = [action for action in self.__get_actions_generator(agent_kind=agent_kind, state=state)]
        action = np.random.choice(actions)
        return action

 



