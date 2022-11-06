import numpy as np
import random as rnd
import itertools as it
import devfx.core as core
import devfx.exceptions as excps
import devfx.machine_learning as ml

from .grid_actions import GridActions
from .grid_agent_kind import GridAgentKind
from .grid_agent import GridAgent

"""========================================================================================================
"""
class GridEnvironment(ml.rl.Environment):
    def __init__(self):
        super().__init__()

        self.__shape = (8, 8)
        self.__cells = {}
        self.__agent_kind_policies = {}

    """------------------------------------------------------------------------------------------------
    """
    @property
    def shape(self):  
        return self.__shape

    @property
    def cells(self):
        return self.__cells

    """------------------------------------------------------------------------------------------------
    """
    def set_agent_kind_policy(self, agent_kind, policy):
        self.__agent_kind_policies[agent_kind] = policy
        for agent in self.get_agents_like(kind=agent_kind):
            agent.set_policy(policy=policy)

    def get_agent_kind_policy(self, agent_kind):
        return self.__agent_kind_policies[agent_kind]

    def get_agent_kind_policies(self):
        return self.__agent_kind_policies

    """------------------------------------------------------------------------------------------------
    """
    def _create(self):
        cells = {}
        for (ri, ci) in it.product(range(1, self.shape[0]+1), range(1, self.shape[1]+1)):
            if((ri == 1) or (ri == self.shape[0]) or (ci == 1) or (ci == self.shape[1])):
                (cell_index, cell_content) = ((ri, ci), (ml.rl.StateKind.UNDEFINED, -1.0))
            elif((ri, ci) in [(3, 3), (4, 4), (6, 6)]):
                (cell_index, cell_content) = ((ri, ci), (ml.rl.StateKind.UNDEFINED, -1.0))
            elif((ri, ci) in [(2, 7)]):
                (cell_index, cell_content) = ((ri, ci), (ml.rl.StateKind.TERMINAL, +1.0))
            elif((ri, ci) in [(3, 7)]):
                (cell_index, cell_content) = ((ri, ci), (ml.rl.StateKind.TERMINAL, -1.0))
            else:
                (cell_index, cell_content) = ((ri, ci), (ml.rl.StateKind.NON_TERMINAL, 0.0))
            cells[cell_index] = cell_content
        self.__cells = cells

    """------------------------------------------------------------------------------------------------
    """
    def _setup(self, iteration_randomness=None):
        if(not self.exists_agent(id=1)):
            self.set_agent_kind_policy(agent_kind=GridAgentKind.WALKER, policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=1e-1))
            self.add_agent(GridAgent(id=1, name='Johnny Walker 1', kind=GridAgentKind.WALKER, 
                                     environment=self, 
                                     policy=self.get_agent_kind_policy(GridAgentKind.WALKER),
                                     iteration_randomness= 0.1 if iteration_randomness is None else iteration_randomness))
        else:
            self.__setup_positional_state(self.get_agent(id=1))

    def _on_added_agent(self, agent):
        self.__setup_positional_state(agent)

    def _on_removed_agent(self, agent):
        pass

    def __setup_positional_state(self, agent):
        choosable_cell_indexes = [cell_index for cell_index in self.cells 
                                             if(self.cells[cell_index][0] == ml.rl.StateKind.NON_TERMINAL)]
        agent_cell_index = rnd.choice(choosable_cell_indexes)
        state = ml.rl.State(value=agent_cell_index, kind=self.cells[agent_cell_index][0])
        agent.set_state(state)

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
        elif(action == GridActions.Right):
            agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1]+1)
        elif(action == GridActions.Up):
            agent_next_cell_index = (agent_cell_index[0]-1, agent_cell_index[1])
        elif(action == GridActions.Down):
            agent_next_cell_index = (agent_cell_index[0]+1, agent_cell_index[1])
        else:
            raise excps.ApplicationError()

        if(self.cells[agent_next_cell_index][0] is ml.rl.StateKind.UNDEFINED):
            next_state = state
            next_reward = ml.rl.Reward(value=self.cells[agent_next_cell_index][1])
            return (next_state, next_reward)

        next_state = ml.rl.State(value=agent_next_cell_index, kind=self.cells[agent_next_cell_index][0])
        next_reward = ml.rl.Reward(value=self.cells[agent_next_cell_index][1])
        return (next_state, next_reward)

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_action(self, agent, state):
        actions = [GridActions.Left, GridActions.Right, GridActions.Up, GridActions.Down]
        action = rnd.choice(actions)
        return action

    """------------------------------------------------------------------------------------------------
    """ 
    def _on_action_done(self, agent, state, action, next_state_and_reward):
        pass

 


