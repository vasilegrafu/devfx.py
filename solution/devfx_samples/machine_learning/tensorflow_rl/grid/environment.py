import numpy as np
import devfx.exceptions as exps
import devfx.machine_learning.tensorflow as ml
from .state import GridCellKind, GridCell
from .action import GridAction, GridPossibleActions

"""========================================================================================================
"""
class GridEnvironment(ml.rl.Environment):
    def __init__(self):
        super().__init__()

        self.__grid = np.asarray([
            [GridCell((1,1)), GridCell((1,2)),                       GridCell((1,3)), GridCell((1,4), GridCellKind.TERMINAL, +1.0)],
            [GridCell((2,1)), GridCell((2,2), GridCellKind.BLOCKED), GridCell((2,3)), GridCell((2,4), GridCellKind.TERMINAL, -1.0)],
            [GridCell((3,1)), GridCell((3,2)),                       GridCell((3,3)), GridCell((3,4))]
        ])

    """------------------------------------------------------------------------------------------------
    """
    def __enumerate_states(self):
        return [state for state in self.__grid.flat if(state.kind != GridCellKind.BLOCKED)]

    def _get_random_state(self):
        states = self.__enumerate_states()
        state = states[np.random.choice(len(states), size=1)[0]]
        return state

    def _get_random_non_terminal_state(self):
        states = [state for state in self.__enumerate_states() if(state.kind == GridCellKind.NON_TERMINAL)]
        state = states[np.random.choice(len(states), size=1)[0]]
        return state

    def _get_random_terminal_state(self):
        states = [state for state in self.__enumerate_states() if(state.kind == GridCellKind.TERMINAL)]
        state = states[np.random.choice(len(states), size=1)[0]]
        return state

    def _get_next_state(self, state, action):
        ix = (state.value[0]-1, state.value[1]-1)
        if(action == GridPossibleActions.Left):
            next_state = self.__grid[ix[0], ix[1]-1]
        if(action == GridPossibleActions.Right):
            next_state = self.__grid[ix[0], ix[1]+1]
        if(action == GridPossibleActions.Up):
            next_state = self.__grid[ix[0]-1, ix[1]]
        if(action == GridPossibleActions.Down):
            next_state = self.__grid[ix[0]+1, ix[1]]
        return next_state

    """------------------------------------------------------------------------------------------------
    """
    def __enumerate_possible_actions(self, state):
        if(state.kind == GridCellKind.TERMINAL):
            return []
        actions = []
        ix = (state.value[0]-1, state.value[1]-1)
        if((ix[0] > 0) and (self.__grid[ix[0]-1, ix[1]].kind != GridCellKind.BLOCKED)):
            actions.append(GridPossibleActions.Up)
        if((ix[0] < (self.__grid.shape[0]-1)) and (self.__grid[ix[0]+1, ix[1]].kind != GridCellKind.BLOCKED)):
            actions.append(GridPossibleActions.Down)  
        if((ix[1] > 1) and (self.__grid[ix[0], ix[1]-1].kind != GridCellKind.BLOCKED)):
            actions.append(GridPossibleActions.Left)
        if((ix[1] < (self.__grid.shape[1]-1)) and (self.__grid[ix[0], ix[1]+1].kind != GridCellKind.BLOCKED)):
            actions.append(GridPossibleActions.Right)     
        return actions

    def _get_random_action(self, state):
        actions = self.__enumerate_possible_actions(state)
        action = actions[np.random.choice(len(actions), size=1)[0]]
        return action
