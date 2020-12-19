import numpy as np
import random as rnd
import itertools as it
import devfx.core as core
import devfx.exceptions as excs
import devfx.machine_learning as ml

from .grid_agent import GridAgent
from .grid_agent_kind import GridAgentKind
from .grid_actions import GridChaserAgentActions
from .grid_actions import GridChasedAgentActions

"""========================================================================================================
"""
class GridEnvironment(ml.rl.Environment):
    def __init__(self):
        super().__init__()

    """------------------------------------------------------------------------------------------------
    """
    @property
    def shape(self):  
        return (10, 10)

    @property
    def target_cell(self):
        return ((2, 9), '+')

    def __create_cells(self):
        cells = {}
        for (ri, ci) in it.product(range(1, self.shape[0]+1), range(1, self.shape[1]+1)):
            if((ri == 1) or (ri == self.shape[0]) or (ci == 1) or (ci == self.shape[1])):
                (cell_index, cell_content) = ((ri, ci), None)
            elif((ri, ci) in [(3, 3), (4, 4), (6, 6), (8, 8)]):
                (cell_index, cell_content) = ((ri, ci), None)
            elif((ri, ci) == self.target_cell[0]):
                (cell_index, cell_content) = (self.target_cell[0], self.target_cell[1])
            else:
                (cell_index, cell_content) = ((ri, ci), ' ')
            cells[cell_index] = cell_content
        self.__cells = cells

    @property
    def cells(self):
        return self.__cells

    """------------------------------------------------------------------------------------------------
    """
    def _create(self):
        self.__create_cells()

    """------------------------------------------------------------------------------------------------
    """       
    def _setup(self):
        if(not self.exists_agent(id=1)):
            self.add_agent(GridAgent(id=1, name='Wolf', kind=GridAgentKind.CHASER, 
                                     environment=self,
                                     policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=1e-3), 
                                     randomness=0.05))
        else:
            self.__setup_positional_state(self.get_agent(id=1))

        if(not self.exists_agent(id=2)):             
            self.add_agent(GridAgent(id=2, name='Rabbit', kind=GridAgentKind.CHASED, 
                                     environment=self,
                                     policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=1e-3), 
                                     randomness=0.05))
        else:
            self.__setup_positional_state(self.get_agent(id=2))

    def _on_added_agent(self, agent):
        self.__setup_positional_state(agent)
        for agent in self.get_agents():
           self.__setup_contextual_state(agent)

    def _on_removed_agent(self, agent):
        for agent in self.get_agents():
           self.__setup_contextual_state(agent)

    def __setup_positional_state(self, agent):
        agent_kind = agent.get_kind()
        if(agent_kind == GridAgentKind.CHASER):
            target_cell_index = self.target_cell[0]
            position_cell_index = (target_cell_index[0]+1, target_cell_index[1]-1)
            state = ml.rl.State(value=(position_cell_index, ), kind=ml.rl.StateKind.NON_TERMINAL)
            agent.set_state(state)
        elif(agent_kind == GridAgentKind.CHASED):
            other_agents_cell_indexes = [other_agent.get_state().value[0] for other_agent in self.get_other_agents(id=agent.get_id())]
            choosable_cell_indexes = [cell_index for cell_index in self.cells 
                                                 if((self.cells[cell_index] is not None) and (cell_index not in other_agents_cell_indexes) and (cell_index[0] >= cell_index[1]))]
            position_cell_index = rnd.choice(choosable_cell_indexes)
            state = ml.rl.State(value=(position_cell_index, ), kind=ml.rl.StateKind.NON_TERMINAL)
            agent.set_state(state)
        else:
            raise excs.ApplicationError()

    def __setup_contextual_state(self, agent):
        other_kind_agents_cell_indexes = [other_kind_agent.get_state().value[0] for other_kind_agent in self.get_other_kind_agents(kind=agent.get_kind())]
        state = ml.rl.State(value=(agent.get_state().value[0], *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.NON_TERMINAL)
        agent.set_state(state)

    """------------------------------------------------------------------------------------------------
    """
    def _destroy(self):
        for agent in self.get_agents():                
            self.destroy_agent(agent.get_id())

    """------------------------------------------------------------------------------------------------
    """
    def _get_next_state_and_reward(self, agent, state, action):
        agent_kind = agent.get_kind()
        agent_cell_index = state.value[0]
        if(agent_kind == GridAgentKind.CHASER):
            if(action == GridChaserAgentActions.Left):
                agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1]-1)
            elif(action == GridChaserAgentActions.Right):
                agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1]+1)
            elif(action == GridChaserAgentActions.Up):
                agent_next_cell_index = (agent_cell_index[0]-1, agent_cell_index[1])
            elif(action == GridChaserAgentActions.Down):
                agent_next_cell_index = (agent_cell_index[0]+1, agent_cell_index[1])
            elif(action == GridChaserAgentActions.Stay):
                agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1])
            else:
                raise excs.ApplicationError() 
        elif(agent_kind == GridAgentKind.CHASED):
            if(action == GridChasedAgentActions.Left):
                agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1]-1)
            elif(action == GridChasedAgentActions.Right):
                agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1]+1)
            elif(action == GridChasedAgentActions.Up):
                agent_next_cell_index = (agent_cell_index[0]-1, agent_cell_index[1])
            elif(action == GridChasedAgentActions.Down):
                agent_next_cell_index = (agent_cell_index[0]+1, agent_cell_index[1])
            else:
                raise excs.ApplicationError() 
        else:
            raise excs.ApplicationError()

        if(self.cells[agent_next_cell_index] is None):
            next_state = state
            next_reward = ml.rl.Reward(value=-1.0)
            return (next_state, next_reward)

        other_kind_agents = self.get_other_kind_agents(kind=agent_kind)
        other_kind_agents_cell_indexes = [other_kind_agent.get_state().value[0] for other_kind_agent in other_kind_agents]
        if(agent_kind == GridAgentKind.CHASER):
            if(agent_next_cell_index in other_kind_agents_cell_indexes):
                next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.TERMINAL)
                next_reward = ml.rl.Reward(value=+1000.0)
            else:
                next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.NON_TERMINAL)
                next_reward = ml.rl.Reward(value=-1.0)
        elif(agent_kind == GridAgentKind.CHASED):
            if(agent_next_cell_index == self.target_cell[0]):
                next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.TERMINAL)
                next_reward = ml.rl.Reward(value=+1000.0)
            elif(agent_next_cell_index in other_kind_agents_cell_indexes):
                next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.TERMINAL)
                next_reward = ml.rl.Reward(value=-1000.0)
            else:
                next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.NON_TERMINAL)
                next_reward = ml.rl.Reward(value=+1.0)
        else:
            raise excs.ApplicationError()
        return (next_state, next_reward)
        
    """------------------------------------------------------------------------------------------------
    """
    def _get_random_action(self, agent, state):  
        agent_kind = agent.get_kind()
        if(agent_kind == GridAgentKind.CHASER):
            actions = [GridChaserAgentActions.Left, GridChaserAgentActions.Right, GridChaserAgentActions.Up, GridChaserAgentActions.Down, GridChaserAgentActions.Stay]
            action = rnd.choice(actions)
            return action
        elif(agent_kind == GridAgentKind.CHASED):
            actions = [GridChasedAgentActions.Left, GridChasedAgentActions.Right, GridChasedAgentActions.Up, GridChasedAgentActions.Down]
            action = rnd.choice(actions)
            return action
        else:
            raise excs.ApplicationError()

    """------------------------------------------------------------------------------------------------
    """ 
    def _on_action_done(self, agent, state, action, next_state_and_reward):
        pass


