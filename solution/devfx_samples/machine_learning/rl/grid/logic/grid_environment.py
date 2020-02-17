import numpy as np
import devfx.exceptions as exps
import devfx.machine_learning as ml
from .grid_actions import GridActions

"""========================================================================================================
"""
class GridEnvironment(ml.rl.Environment):
    def __init__(self):
        super().__init__()

        self.__grid = np.empty(shape=(5, 5), dtype=object)
        cells_with_terminal_states = [((0, 4), +1.0), ((1, 4), -1.0)]
        cells_blocked = [(1, 1), (2, 2), (4, 4)]
        for ri in range(self.__grid.shape[0]):
            for ci in range(self.__grid.shape[1]):
                if((ri, ci) in [state_value for (state_value, reward) in cells_with_terminal_states]):
                    state = ml.rl.State(value=(ri, ci), state_kind=ml.rl.StateKind.TERMINAL)
                    reward = ml.rl.Reward(value=[reward for (state_value, reward) in cells_with_terminal_states if(state_value == (ri, ci))][0])
                    self.__grid[(ri, ci)] = (state, reward)
                elif((ri, ci) in cells_blocked):
                    self.__grid[(ri, ci)] = None
                else:
                    state = ml.rl.State((ri, ci), ml.rl.StateKind.NON_TERMINAL)
                    reward = ml.rl.Reward(value=0.0)
                    self.__grid[(ri, ci)] = (state, reward)

    """------------------------------------------------------------------------------------------------
    """
    def __get_cells_generator(self):
        return ((ci, cc) for ci, cc in np.ndenumerate(self.__grid))

    def get_cells(self):
        return [(ci, cc) for (ci, cc) in self.__get_cells_generator()]

    def get_size(self):
        return self.__grid.shape

    def __get_cells_with_content_generator(self):
        return ((ci, cc) for (ci, cc) in self.__get_cells_generator() if(cc is not None))

    def __get_cells_without_content_generator(self):
        return ((ci, cc) for (ci, cc) in self.__get_cells_generator() if(cc is None))

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_state(self, agent_kind):
        ccs = [cc for (ci, cc) in self.__get_cells_with_content_generator()]
        (state, reward) = ccs[np.random.choice(len(ccs))]
        return state

    def _get_random_non_terminal_state(self, agent_kind):
        ccs = [cc for (ci, cc) in self.__get_cells_with_content_generator() if(cc[0].kind == ml.rl.StateKind.NON_TERMINAL)]
        (state, reward) = ccs[np.random.choice(len(ccs))]
        return state

    def _get_random_terminal_state(self, agent_kind):
        ccs = [cc for (ci, cc) in self.__get_cells_with_content_generator() if(cc[0].kind == ml.rl.StateKind.TERMINAL)]
        (state, reward) = ccs[np.random.choice(len(ccs))]
        return state

    """------------------------------------------------------------------------------------------------
    """
    def _get_next_state_and_reward(self, agent, action):
        state = agent.get_state()
        if(action == GridActions.Left):
            next_state = self.__grid[state.value[0], state.value[1]-1]
        if(action == GridActions.Right):
            next_state = self.__grid[state.value[0], state.value[1]+1]
        if(action == GridActions.Up):
            next_state = self.__grid[state.value[0]-1, state.value[1]]
        if(action == GridActions.Down):
            next_state = self.__grid[state.value[0]+1, state.value[1]]
        return next_state

    """------------------------------------------------------------------------------------------------
    """
    def __get_actions_generator(self, agent):
        state = agent.get_state()
        if(state.kind == ml.rl.StateKind.TERMINAL):
            return
        if((state.value[0] > 0) and (self.__grid[state.value[0]-1, state.value[1]] is not None)):
            yield GridActions.Up
        if((state.value[0] < (self.__grid.shape[0]-1)) and (self.__grid[state.value[0]+1, state.value[1]] is not None)):
            yield GridActions.Down
        if((state.value[1] > 0) and (self.__grid[state.value[0], state.value[1]-1] is not None)):
            yield GridActions.Left
        if((state.value[1] < (self.__grid.shape[1]-1)) and (self.__grid[state.value[0], state.value[1]+1] is not None)):
            yield GridActions.Right     

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_action(self, agent):
        actions = [action for action in self.__get_actions_generator(agent=agent)]
        action = np.random.choice(actions)
        return action

 



