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
            [GridCell(), GridCell(),                          GridCell(), GridCell(reward=+1.0)],
            [GridCell(), GridCell(kind=GridCellKind.Blocked), GridCell(), GridCell(kind=GridCellKind.Free.Terminal, reward=-1.0)],
            [GridCell(), GridCell(),                          GridCell(), GridCell()]
        ])

    def __getitem__(self, key):
        return self.__grid[key]

    @property
    def shape(self):
        return (self.__grid.shape[0], self.__grid.shape[1])

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
        if(not (0 <= (state[0]-1) <= (self.__grid.shape[0]-1))):
            return False
        if(not (0 <= (state[1]-1) <= (self.__grid.shape[1]-1))):
            return False
        grid_cell = self.__grid[(state[0]-1), (state[1]-1)]
        if(grid_cell.kind == GridCellKind.Blocked):
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
        states = []
        for (i, grid_cells) in enumerate(self.__grid):
            for (j, grid_cell) in enumerate(grid_cells): 
                if(grid_cell.kind != GridCellKind.Blocked):
                    state = (i+1, j+1)
                    states.append(state)
        return states

    """------------------------------------------------------------------------------------------------
    """
    def _get_reward(self, state):
        grid_cell = self.__grid[(state[0]-1), (state[1]-1)]
        reward = grid_cell.reward
        return reward
    
    """------------------------------------------------------------------------------------------------
    """
    def _get_actions(self, state):
        grid_cell = self.__grid[(state[0]-1), (state[1]-1)]
        if(grid_cell.kind == GridCellKind.Free.Terminal):
            return []

        actions = []

        if(state[1] > 1):
            grid_cell = self.__grid[(state[0]-1), (state[1]-1)-1]
            if(grid_cell.kind != GridCellKind.Blocked):
                actions.append(GridAction.Left)

        if(state[1] < self.__grid.shape[1]):
            grid_cell = self.__grid[(state[0]-1), (state[1]-1)+1]
            if(grid_cell.kind != GridCellKind.Blocked):
                actions.append(GridAction.Right)

        if(state[0] > 1):
            grid_cell = self.__grid[(state[0]-1)-1, (state[1]-1)]
            if(grid_cell.kind != GridCellKind.Blocked):
                actions.append(GridAction.Up)

        if(state[0] < self.__grid.shape[0]):
            grid_cell = self.__grid[(state[0]-1)+1, (state[1]-1)]
            if(grid_cell.kind != GridCellKind.Blocked):
                actions.append(GridAction.Down)         

        return actions

    """------------------------------------------------------------------------------------------------
    """
    def _get_next_state(self, state, action):
        if(action == GridAction.Left):
            next_state = (state[0], state[1]-1)

        if(action == GridAction.Right):
            next_state = (state[0], state[1]+1)

        if(action == GridAction.Up):
            next_state = (state[0]-1, state[1])

        if(action == GridAction.Down):
            next_state = (state[0]+1, state[1]) 

        if(not super().is_valid_state(state=next_state)):
            raise exceps.ApplicationError()

        return next_state




