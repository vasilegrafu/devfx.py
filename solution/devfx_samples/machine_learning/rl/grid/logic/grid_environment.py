import numpy as np
import devfx.exceptions as exps
import devfx.machine_learning as ml
from .grid_cell_state_kind import GridCellStateKind
from .grid_cell_state import GridCellState
from .grid_action import GridAction
from .grid_possible_actions import GridPossibleActions

"""========================================================================================================
"""
class GridEnvironment(ml.rl.Environment):
    def __init__(self):
        super().__init__()

        self.__grid = np.asarray([
            [GridCellState((1,1)), GridCellState((1,2)),                            GridCellState((1,3)), GridCellState((1,4), GridCellStateKind.TERMINAL, +1.0)],
            [GridCellState((2,1)), GridCellState((2,2), GridCellStateKind.BLOCKED), GridCellState((2,3)), GridCellState((2,4), GridCellStateKind.TERMINAL, -1.0)],
            [GridCellState((3,1)), GridCellState((3,2)),                            GridCellState((3,3)), GridCellState((3,4))]
        ])

    """------------------------------------------------------------------------------------------------
    """
    def __get_states_generator(self):
        return (state for state in self.__grid.flat)
    
    def __get_non_blocked_states_generator(self):
        return (state for state in self.__get_states_generator() if(state.kind != GridCellStateKind.BLOCKED))

    def __get_enumerable_blocked_states(self):
        return (state for state in self.__get_states_generator() if(state.kind == GridCellStateKind.BLOCKED))

    def _get_random_state(self):
        states = [state for state in self.__get_non_blocked_states_generator()]
        state = states[np.random.choice(len(states), size=1)[0]]
        return state

    def _get_random_non_terminal_state(self):
        states = [state for state in self.__get_non_blocked_states_generator() if(state.kind == GridCellStateKind.NON_TERMINAL)]
        state = states[np.random.choice(len(states), size=1)[0]]
        return state

    def _get_random_terminal_state(self):
        states = [state for state in self.__get_non_blocked_states_generator() if(state.kind == GridCellStateKind.TERMINAL)]
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
    def __get_possible_actions_generator(self, state):
        if(state.kind == GridCellStateKind.TERMINAL):
            return
        ix = (state.value[0]-1, state.value[1]-1)
        if((ix[0] > 0) and (self.__grid[ix[0]-1, ix[1]].kind != GridCellStateKind.BLOCKED)):
            yield GridPossibleActions.Up
        if((ix[0] < (self.__grid.shape[0]-1)) and (self.__grid[ix[0]+1, ix[1]].kind != GridCellStateKind.BLOCKED)):
            yield GridPossibleActions.Down
        if((ix[1] > 0) and (self.__grid[ix[0], ix[1]-1].kind != GridCellStateKind.BLOCKED)):
            yield GridPossibleActions.Left
        if((ix[1] < (self.__grid.shape[1]-1)) and (self.__grid[ix[0], ix[1]+1].kind != GridCellStateKind.BLOCKED)):
            yield GridPossibleActions.Right     


    def _get_random_action(self, state):
        actions = [action for action in self.__get_possible_actions_generator(state)]
        action = actions[np.random.choice(len(actions), size=1)[0]]
        return action

    """------------------------------------------------------------------------------------------------
    """
    def get_size(self):
        return self.__grid.shape

    def get_state(self, key):
        return self.__grid[key[0]-1, key[1]-1]

    def get_states(self):
        states = [state for state in self.__get_states_generator()]
        return states

    """------------------------------------------------------------------------------------------------
    """
    def get_actions(self, state):
        actions = [action for action in self.__get_possible_actions_generator(state)]
        return actions

