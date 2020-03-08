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
        raise exps.NotImplementedError()

    def _get_random_non_terminal_state(self, agent_kind):
        if(agent_kind == 'CHASER'):
            agents = super().get_agents(kind='CHASED')
        if(agent_kind == 'CHASED'):
            agents = super().get_agents(kind='CHASER')
            
        if(agents is None):
            cell_indexes = [cell_index for (cell_index, cell_content) in self.__get_non_blocked_cells_generator()]
            cell_index = cell_indexes[np.random.choice(len(cell_indexes))]
            state = ml.rl.State(value=(cell_index, (None, None)))
            return state
        else:
            other_cell_index = agents[0].get_state().value[0]
            cell_indexes = [cell_index for (cell_index, cell_content) in self.__get_non_blocked_cells_generator() if(cell_index != other_cell_index)]
            cell_index = cell_indexes[np.random.choice(len(cell_indexes))]
            state = ml.rl.State(value=(cell_index, other_cell_index))
            return state

    def _get_random_terminal_state(self, agent_kind):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """
    def _get_state_kind(self, agent_kind, state):
        if(state.value[0] != state.value[1]):
            return ml.rl.StateKind.NON_TERMINAL
        else:
            return ml.rl.StateKind.TERMINAL

    """------------------------------------------------------------------------------------------------
    """
    def _get_next_state_and_reward(self, agent_kind, state, action):
        if(agent_kind == 'CHASER'):
            agents = super().get_agents(kind='CHASED')
        if(agent_kind == 'CHASED'):
            agents = super().get_agents(kind='CHASER')
        other_cell_index = agents[0].get_state().value[0]

        cell_index = state.value[0]

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

        next_state = ml.rl.State(value=(next_cell_index, other_cell_index))

        if(next_cell_index != other_cell_index):
            next_reward = ml.rl.Reward(value=0.0)
        else:
            if(agent_kind == 'CHASER'):
                next_reward = ml.rl.Reward(value=+10)
            elif(agent_kind == 'CHASED'):
                next_reward = ml.rl.Reward(value=-10)

        return (next_state, next_reward)

    """------------------------------------------------------------------------------------------------
    """
    def __get_actions_generator(self, agent_kind, state):
        state_kind = self.get_state_kind(agent_kind=agent_kind, state=state)
        if(state_kind == ml.rl.StateKind.TERMINAL):
            return
        cell_index = state.value[0]
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

 



