from enum import Enum
import numpy as np
import devfx.exceptions as exceps
import devfx.statistics as stats
import devfx.machine_learning.tensorflow as ml

"""========================================================================================================
"""
class GridCellKind(object):
    class Free(object):
        NonTerminal = 'Free-NonTerminal'
        Terminal = 'Free-Terminal'
    Blocked = 'Blocked'

"""========================================================================================================
"""
class GridCell(object):
    def __init__(self, kind=GridCellKind.Free.NonTerminal, reward=0.0):
        self.__kind = kind
        self.__reward = reward

    @property
    def kind(self):
        return self.__kind
    
    @property
    def reward(self):
        return self.__reward

"""========================================================================================================
"""
class Grid(object):
    def __init__(self):
        self.__grid = np.asarray([
            [GridCell(), GridCell(),                          GridCell(), GridCell(kind=GridCellKind.Free.Terminal, reward=+1.0)],
            [GridCell(), GridCell(kind=GridCellKind.Blocked), GridCell(), GridCell(kind=GridCellKind.Free.Terminal, reward=-1.0)],
            [GridCell(), GridCell(),                          GridCell(), GridCell()]
        ])

    @property
    def shape(self):
        shape = (self.__grid.shape[0], self.__grid.shape[1])
        return shape

    def __iter__(self):
        for (key, grid_cell) in np.ndenumerate(self.__grid):
            yield ((key[0]+1, key[1]+1), grid_cell)

    def __getitem__(self, key):
        grid_cell = self.__grid[(key[0]-1, key[1]-1)]
        return grid_cell

"""========================================================================================================
"""
class GridAction(object):
    Left = 'Left'
    Right = 'Right'
    Up = 'Up'
    Down = 'Down'

"""========================================================================================================
"""
class GridEnvironment(ml.rl.Environment):
    def __init__(self):
        super().__init__()

        self.__grid = Grid()


    """------------------------------------------------------------------------------------------------
    """
    def _is_valid_state(self, state):
        if(not 1 <= state[0] <= self.__grid.shape[0]):
            return False
        if(not 0 <= state[1] <= self.__grid.shape[1]):
            return False
        if(self.__grid[state].kind == GridCellKind.Blocked):
            return False
        return True

    def _is_valid_action(self, action):
        if(action == GridAction.Left):
            return True
        if(action == GridAction.Right):
            return True
        if(action == GridAction.Up):
            return True
        if(action == GridAction.Down):
            return True
        return False

    """------------------------------------------------------------------------------------------------
    """
    def _get_states(self):
        states = [state for (state, grid_cell) in self.__grid if(grid_cell.kind != GridCellKind.Blocked)]
        return states

    """------------------------------------------------------------------------------------------------
    """
    def _get_reward(self, state):
        reward = self.__grid[state].reward
        return reward
    
    """------------------------------------------------------------------------------------------------
    """
    def _get_actions(self, state):
        if(self.__grid[state].kind == GridCellKind.Free.Terminal):
            return []

        actions = []

        if((state[0] > 1) and (self.__grid[state[0]-1, state[1]].kind != GridCellKind.Blocked)):
            actions.append(GridAction.Up)

        if((state[0] < self.__grid.shape[0]) and (self.__grid[state[0]+1, state[1]].kind != GridCellKind.Blocked)):
            actions.append(GridAction.Down)  

        if((state[1] > 1) and (self.__grid[state[0], state[1]-1].kind != GridCellKind.Blocked)):
            actions.append(GridAction.Left)

        if((state[1] < self.__grid.shape[1]) and (self.__grid[state[0], state[1]+1].kind != GridCellKind.Blocked)):
            actions.append(GridAction.Right)     

        return actions

    """------------------------------------------------------------------------------------------------
    """
    def _get_next_state(self, state, action):
        next_state = None

        if(action == GridAction.Left):
            next_state = (state[0], state[1]-1)

        if(action == GridAction.Right):
            next_state = (state[0], state[1]+1)

        if(action == GridAction.Up):
            next_state = (state[0]-1, state[1])

        if(action == GridAction.Down):
            next_state = (state[0]+1, state[1]) 

        return next_state




