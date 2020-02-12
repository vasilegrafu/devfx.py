import numpy as np
import devfx.exceptions as exps
import devfx.machine_learning as ml
from .grid_actions import GridActions

"""========================================================================================================
"""
class GridEnvironment(ml.rl.Environment):
    def __init__(self):
        super().__init__()

        rn = 8
        cn = 10
        cells_with_terminal_states = [((1, cn), +1.0), ((2, cn), -1.0)]
        cells_blocked = [(2, 2), (3, 3), (6, 5), (7, 9)]
        rclist = []
        for ri in range(1, rn+1):
            clist = []
            rclist.append(clist)
            for ci in range(1, cn+1):
                if((ri, ci) in [state_value for (state_value, reward) in cells_with_terminal_states]):
                    clist.append(ml.rl.State((ri, ci), ml.rl.StateKind.TERMINAL, [reward for (state_value, reward) in cells_with_terminal_states if(state_value == (ri, ci))][0]))
                elif((ri, ci) in cells_blocked):
                    clist.append(None)
                else:
                    clist.append(ml.rl.State((ri, ci), ml.rl.StateKind.NON_TERMINAL, 0.0))

        self.__grid = np.asarray(rclist)

    """------------------------------------------------------------------------------------------------
    """
    def __get_cells_generator(self):
        return ((cell_index, cell_content) for cell_index, cell_content in np.ndenumerate(self.__grid))

    def get_cells(self):
        return [(cell_index, cell_content) for (cell_index, cell_content) in self.__get_cells_generator()]

    def get_cell_index(self, state):
        return [cell_index for (cell_index, cell_content) in self.__get_cells_generator() if(cell_content == state)][0]

    def get_state(self, cell_index):
        cell_content = self.__grid[cell_index]
        if(cell_content is None):
            raise exps.ApplicationError()
        state = cell_content
        return state

    """------------------------------------------------------------------------------------------------
    """
    def __get_states_generator(self):
        return (cell_content for (cell_index, cell_content) in self.__get_cells_generator() if(cell_content is not None))

    def get_states(self):
        return [state for state in self.__get_states_generator()]

    def get_size(self):
        return self.__grid.shape

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_state(self):
        states = [state for state in self.__get_states_generator()]
        state = np.random.choice(states)
        return state

    def _get_random_non_terminal_state(self):
        states = [state for state in self.__get_states_generator() if(state.kind == ml.rl.StateKind.NON_TERMINAL)]
        state = np.random.choice(states)
        return state

    def _get_random_terminal_state(self):
        states = [state for state in self.__get_states_generator() if(state.kind == ml.rl.StateKind.TERMINAL)]
        state = np.random.choice(states)
        return state

    def _get_next_state(self, state, action):
        ix = (state.value[0]-1, state.value[1]-1)
        if(action == GridActions.Left):
            next_state = self.__grid[ix[0], ix[1]-1]
        if(action == GridActions.Right):
            next_state = self.__grid[ix[0], ix[1]+1]
        if(action == GridActions.Up):
            next_state = self.__grid[ix[0]-1, ix[1]]
        if(action == GridActions.Down):
            next_state = self.__grid[ix[0]+1, ix[1]]
        return next_state

    """------------------------------------------------------------------------------------------------
    """
    def __get_actions_generator(self, state):
        if(state.kind == ml.rl.StateKind.TERMINAL):
            return
        ix = (state.value[0]-1, state.value[1]-1)
        if((ix[0] > 0) and (self.__grid[ix[0]-1, ix[1]] is not None)):
            yield GridActions.Up
        if((ix[0] < (self.__grid.shape[0]-1)) and (self.__grid[ix[0]+1, ix[1]] is not None)):
            yield GridActions.Down
        if((ix[1] > 0) and (self.__grid[ix[0], ix[1]-1] is not None)):
            yield GridActions.Left
        if((ix[1] < (self.__grid.shape[1]-1)) and (self.__grid[ix[0], ix[1]+1] is not None)):
            yield GridActions.Right     

    def get_actions(self, state):
        actions = [action for action in self.__get_actions_generator(state)]
        return actions

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_action(self, state):
        actions = [action for action in self.__get_actions_generator(state)]
        action = np.random.choice(actions)
        return action

 



