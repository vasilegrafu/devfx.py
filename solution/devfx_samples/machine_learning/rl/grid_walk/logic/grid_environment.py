import numpy as np
import random as rnd
import itertools as it
import devfx.exceptions as exps
import devfx.machine_learning as ml
from .grid_actions import GridActions

"""========================================================================================================
"""
class GridEnvironment(ml.rl.Environment):
    def __init__(self):
        super().__init__()

    """------------------------------------------------------------------------------------------------
    """
    @property
    def shape(self):  
        return (8, 8)

    @property
    def cells(self):
        cells = {}
        for (ri, ci) in it.product(range(1, self.shape[0]+1), range(1, self.shape[1]+1)):
            if((ri == 1) or (ri == self.shape[0]) or (ci == 1) or (ci == self.shape[1])):
                (cell_index, cell_content) = ((ri, ci), None)
            elif((ri, ci) in [(3, 3), (4, 4), (6, 6)]):
                (cell_index, cell_content) = ((ri, ci), None)
            elif((ri, ci) == (2, 6)):
                (cell_index, cell_content) = ((ri, ci), (ml.rl.StateKind.TERMINAL, +1.0))
            elif((ri, ci) == (3, 6)):
                (cell_index, cell_content) = ((ri, ci), (ml.rl.StateKind.TERMINAL, -1.0))
            else:
                (cell_index, cell_content) = ((ri, ci), (ml.rl.StateKind.NON_TERMINAL, 0.0))
            cells[cell_index] = cell_content
        return cells

    @property
    def walkable_cells(self):
        return {cell_index: self.cells[cell_index] for cell_index in self.cells if(self.cells[cell_index] is not None)}

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_state(self, agent_kind):
        cell_indexes = [cell_index for cell_index in self.walkable_cells if(self.cells[cell_index][0] == ml.rl.StateKind.NON_TERMINAL)]
        cell_index = rnd.choice(cell_indexes)
        state = ml.rl.State(value=cell_index, kind=self.cells[cell_index][0])
        return state

    """------------------------------------------------------------------------------------------------
    """
    def _get_next_state_and_reward(self, agent_kind, state, action):
        cell_index = state.value
        if(action == GridActions.Left):
            next_cell_index = (cell_index[0]-1, cell_index[1])
        if(action == GridActions.Right):
            next_cell_index = (cell_index[0]+1, cell_index[1])
        if(action == GridActions.Up):
            next_cell_index = (cell_index[0], cell_index[1]-1)
        if(action == GridActions.Down):
            next_cell_index = (cell_index[0], cell_index[1]+1)
        if(action == GridActions.Stay):
            next_cell_index = (cell_index[0], cell_index[1])
        if(next_cell_index not in self.walkable_cells):
            raise exps.ApplicationError()
        next_state = ml.rl.State(value=next_cell_index, kind=self.cells[next_cell_index][0])
        next_reward = ml.rl.Reward(value=self.cells[next_cell_index][1])
        return (next_state, next_reward)

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_action(self, agent_kind, state):
        def get_possibile_actions(cells, agent_kind, state):          
            cell_index = state.value
            if(cells[(cell_index[0]-1, cell_index[1])] is not None):
                yield GridActions.Left
            if(cells[(cell_index[0]+1, cell_index[1])] is not None):
                yield GridActions.Right   
            if(cells[(cell_index[0], cell_index[1]-1)] is not None):
                yield GridActions.Up
            if(cells[(cell_index[0], cell_index[1]+1)] is not None):
                yield GridActions.Down 
            yield GridActions.Stay  

        actions = [action for action in get_possibile_actions(cells=self.cells, agent_kind=agent_kind, state=state)]
        action = rnd.choice(actions)
        return action

 



