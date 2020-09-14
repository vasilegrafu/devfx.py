import numpy as np
import random as rnd
import itertools as it
import devfx.core as core
import devfx.exceptions as exps
import devfx.machine_learning as ml
from .grid_agent import GridAgent
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

    def __create_cells(self):
        cells = {}
        for (ri, ci) in it.product(range(1, self.shape[0]+1), range(1, self.shape[1]+1)):
            if((ri == 1) or (ri == self.shape[0]) or (ci == 1) or (ci == self.shape[1])):
                (cell_index, cell_content) = ((ri, ci), None)
            elif((ri, ci) in [(3, 3), (4, 4), (6, 6)]):
                (cell_index, cell_content) = ((ri, ci), None)
            # elif((ri, ci) in [(2, 2), (2, 7)]):
            #     (cell_index, cell_content) = ((ri, ci), (ml.rl.StateKind.TERMINAL, +1.0))
            elif((ri, ci) == (3, 7)):
                (cell_index, cell_content) = ((ri, ci), (ml.rl.StateKind.TERMINAL, +100.0))
            else:
                (cell_index, cell_content) = ((ri, ci), (ml.rl.StateKind.NON_TERMINAL, 0.0))
            cells[cell_index] = cell_content
        self.__cells = cells

    def get_cells(self):
        return self.__cells

    def get_walkable_cells(self):
        walkable_cells = {cell_index: self.get_cells()[cell_index] for cell_index in self.get_cells() if(self.get_cells()[cell_index] is not None)}
        return walkable_cells

    """------------------------------------------------------------------------------------------------
    """
    def _create(self):
        self.__create_cells()

        self.setup()
        
    """------------------------------------------------------------------------------------------------
    """
    def _setup(self):
        if(not self.exists_agent(id=1)):
            self.add_agent(GridAgent(id=1, name='Johnny Walker 1', kind='WALKER', 
                                    environment=self, 
                                    policy=ml.rl.QLearningPolicy(discount_factor=0.9, learning_rate=0.05), 
                                    randomness=0.1))
        else:
            self.__setup_positional_state(self.get_agent(id=1))

    def _on_added_agent(self, agent):
        self.__setup_positional_state(agent)

    def _on_removed_agent(self, agent):
        pass

    def __setup_positional_state(self, agent):
        choosable_cell_indexes = [cell_index for cell_index in self.get_walkable_cells() if(self.get_cells()[cell_index][0] == ml.rl.StateKind.NON_TERMINAL)]
        agent_cell_index = rnd.choice(choosable_cell_indexes)
        state = ml.rl.State(value=agent_cell_index, kind=self.get_cells()[agent_cell_index][0])
        agent.set_state(state)

    """------------------------------------------------------------------------------------------------
    """
    def _do_iteration(self, agents=None, randomness=None):
        if(any([agent.is_in_terminal_state() for agent in self.get_agents()])):
            self.setup()
        else:
            if(agents is None):
                agents = self.get_agents()
            for agent in agents:
                agent.do_iteration(randomness=randomness)

    """------------------------------------------------------------------------------------------------
    """
    def _destroy(self):
        for agent in self.get_agents():                
            self.remove_agent(agent)

    """------------------------------------------------------------------------------------------------
    """
    def _get_next_state_and_reward(self, agent, state, action):
        agent_cell_index = state.value
        if(action == GridActions.Left):
            agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1]-1)
        if(action == GridActions.Right):
            agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1]+1)
        if(action == GridActions.Up):
            agent_next_cell_index = (agent_cell_index[0]-1, agent_cell_index[1])
        if(action == GridActions.Down):
            agent_next_cell_index = (agent_cell_index[0]+1, agent_cell_index[1])
        if(action == GridActions.Stay):
            agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1])
        if(agent_next_cell_index not in self.get_walkable_cells()):
            raise exps.ApplicationError()
        next_state = ml.rl.State(value=agent_next_cell_index, kind=self.get_cells()[agent_next_cell_index][0])
        next_reward = ml.rl.Reward(value=self.get_cells()[agent_next_cell_index][1])
        return (next_state, next_reward)

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_action(self, agent, state):
        def get_possibile_actions(cells, agent, state):          
            agent_cell_index = state.value
            if(cells[(agent_cell_index[0], agent_cell_index[1]-1)] is not None):
                yield GridActions.Left
            if(cells[(agent_cell_index[0], agent_cell_index[1]+1)] is not None):
                yield GridActions.Right   
            if(cells[(agent_cell_index[0]-1, agent_cell_index[1])] is not None):
                yield GridActions.Up
            if(cells[(agent_cell_index[0]+1, agent_cell_index[1])] is not None):
                yield GridActions.Down 
            yield GridActions.Stay  

        actions = [action for action in get_possibile_actions(cells=self.get_cells(), agent=agent, state=state)]
        action = rnd.choice(actions)
        return action

 


