import numpy as np
import random as rnd
import itertools as it
import devfx.core as core
import devfx.exceptions as excs
import devfx.machine_learning as ml

from .grid_agent import GridAgent
from .grid_agent_kind import GridAgentKind
from .grid_actions import GridAgentMovementActions
from .grid_actions import GridAgentHittingBallActions

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
    def target_cell(self):
        return ((2, 7), '+')

    def __create_cells(self):
        cells = {}
        for (ri, ci) in it.product(range(1, self.shape[0]+1), range(1, self.shape[1]+1)):
            if((ri == 1) or (ri == self.shape[0]) or (ci == 1) or (ci == self.shape[1])):
                (cell_index, cell_content) = ((ri, ci), None)
            elif((ri, ci) in [(3, 3), (4, 4), (6, 6)]):
                (cell_index, cell_content) = ((ri, ci), None)
            else:
                (cell_index, cell_content) = ((ri, ci), ' ')
            cells[cell_index] = cell_content
        self.__cells = cells

    def get_cells(self):
        return self.__cells

    def get_walkable_cells(self):
        walkable_cells = core.ObjectStorage.intercept(self, 'walkable_cells', 
                                                      lambda: {cell_index: cell_content for (cell_index, cell_content) in self.get_cells().items() if(cell_content != None)})
        return walkable_cells

    def get_ball_cell_index(self):
        return [cell_index for (cell_index, cell_content) in self.get_walkable_cells().items() if(cell_content == 'o')]

    def setup_ball_to_cell_index(self, cell_index):
        self.get_cells()[cell_index] = 'o'

    def move_ball_to_cell_index(self, cell_index):
        ball_cell_index = self.get_ball_cell_index()
        self.get_cells()[ball_cell_index] = ' '
        self.get_cells()[cell_index] = 'o'

    """------------------------------------------------------------------------------------------------
    """
    def _create(self):
        self.__create_cells()

        self.setup()

    """------------------------------------------------------------------------------------------------
    """       
    def _setup(self):
        self.__setup_ball_to_random_cell_index()

        if(not self.exists_agent(id=1)):
            self.add_agent(GridAgent(id=1, name='Player1', kind=GridAgentKind.PLAYER, 
                                    environment=self,
                                    policy=ml.rl.ESarsaPolicy(discount_factor=0.99, learning_rate=1e-2), 
                                    randomness=0.05))
        else:
            self.__setup_positional_state(self.get_agent(id=1))

    def _on_added_agent(self, agent):
        self.__setup_agent_to_random_cell_index(agent)

    def _on_removed_agent(self, agent):
        pass

    def __setup_ball_to_random_cell_index(self):
        agents = self.get_agents()
        agents_cell_indexes = [agent.get_state().value[0] for agent in agents]
        ball_choosable_cell_indexes = [cell_index for cell_index in self.get_walkable_cells() if(cell_index != self.target_cell[0])]
        ball_cell_index = rnd.choice(ball_choosable_cell_indexes)
        self.setup_ball_to_cell_index(ball_cell_index)

    def __setup_agent_to_random_cell_index(self, agent):
        ball_cell_index = self.get_ball_cell_index()
        other_agents = self.get_other_agents(id=agent.get_id())
        other_agents_cell_indexes = [other_agent.get_state().value[0] for other_agent in other_agents]
        agent_choosable_cell_indexes = [cell_index for cell_index in self.get_walkable_cells() if(cell_index != self.target_cell[0] and cell_index != ball_cell_index)]
        agent_cell_index = rnd.choice(agent_choosable_cell_indexes)
        state = ml.rl.State(value=(agent_cell_index, ball_cell_index), kind=ml.rl.StateKind.NON_TERMINAL)
        agent.set_state(state)

    """------------------------------------------------------------------------------------------------
    """
    def _destroy(self):
        for agent in self.get_agents():                
            self.destroy_agent(agent.get_id())

    """------------------------------------------------------------------------------------------------
    """
    def _get_next_state_and_reward(self, agent, state, action):
        agent_cell_index = state.value[0]
        if(action == GridAgentMovementActions.Left):
            agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1]-1)
        elif(action == GridAgentMovementActions.Right):
            agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1]+1)
        elif(action == GridAgentMovementActions.Up):
            agent_next_cell_index = (agent_cell_index[0]-1, agent_cell_index[1])
        elif(action == GridAgentMovementActions.Down):
            agent_next_cell_index = (agent_cell_index[0]+1, agent_cell_index[1])
        elif(action == GridAgentMovementActions.Stay):
            agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1])
        else:
            raise excs.ApplicationError() 

        if(agent_next_cell_index not in self.get_walkable_cells()):
            raise excs.ApplicationError()

        other_kind_agents = self.get_other_kind_agents(kind=agent_kind)
        other_kind_agents_cell_indexes = [other_kind_agent.get_state().value[0] for other_kind_agent in other_kind_agents]

        if(agent_next_cell_index in [cell_index for cell_index in self.get_walkable_cells() if(cell_index == self.target_cell[0])]):
            if(agent_kind == GridAgentKind.CHASER):
                next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.NON_TERMINAL)
                next_reward = ml.rl.Reward(value=-1.0)
            elif(agent_kind == GridAgentKind.CHASED):
                next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.TERMINAL)
                next_reward = ml.rl.Reward(value=+5000.0)
            else:
                raise excs.ApplicationError()
            return (next_state, next_reward)

        if(agent_next_cell_index in other_kind_agents_cell_indexes):
            if(agent_kind == GridAgentKind.CHASER):
                next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.TERMINAL)
                next_reward = ml.rl.Reward(value=+1000.0)
            elif(agent_kind == GridAgentKind.CHASED):
                next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.TERMINAL)
                next_reward = ml.rl.Reward(value=-1000.0)
            else:
                raise excs.ApplicationError()
            return (next_state, next_reward)

        if(agent_next_cell_index not in other_kind_agents_cell_indexes):
            if(agent_kind == GridAgentKind.CHASER):
                next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.NON_TERMINAL)
                next_reward = ml.rl.Reward(value=-1.0)
            elif(agent_kind == GridAgentKind.CHASED):
                next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.NON_TERMINAL)
                next_reward = ml.rl.Reward(value=0.0)
            else:
                raise excs.ApplicationError()
            return (next_state, next_reward)

        raise excs.ApplicationError()

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_action(self, agent, state):  
        agent_movement_possibile_actions = core.ObjectStorage.intercept(self, 'agent_movement_possibile_actions', lambda: {})
        if(state not in agent_movement_possibile_actions):       
            agent_movement_possibile_actions[state] = []
            agent_cell_index = state.value[0]
            if(self.get_cells()[(agent_cell_index[0], agent_cell_index[1]-1)] is not None):
                agent_movement_possibile_actions[state].append(GridAgentMovementActions.Left)
            if(self.get_cells()[(agent_cell_index[0], agent_cell_index[1]+1)] is not None):
                agent_movement_possibile_actions[state].append(GridAgentMovementActions.Right) 
            if(self.get_cells()[(agent_cell_index[0]-1, agent_cell_index[1])] is not None):
                agent_movement_possibile_actions[state].append(GridAgentMovementActions.Up)
            if(self.get_cells()[(agent_cell_index[0]+1, agent_cell_index[1])] is not None):
                agent_movement_possibile_actions[state].append(GridAgentMovementActions.Down)
        agent_movement_action = rnd.choice(agent_movement_possibile_actions[state])

        agent_hitting_ball_possibile_actions = core.ObjectStorage.intercept(self, 'agent_hitting_ball_possibile_actions', lambda: {})
        if(state not in agent_hitting_ball_possibile_actions):       
            agent_hitting_ball_possibile_actions[state] = []
            ball_cell_index = self.get_ball_cell_index()
            if(self.get_cells()[(ball_cell_index[0], ball_cell_index[1]-1)] is not None):
                agent_hitting_ball_possibile_actions[state].append(GridAgentHittingBallActions.Left)
            if(self.get_cells()[(ball_cell_index[0], ball_cell_index[1]+1)] is not None):
                agent_hitting_ball_possibile_actions[state].append(GridAgentMovementActions.Right) 
            if(self.get_cells()[(ball_cell_index[0]-1, ball_cell_index[1])] is not None):
                agent_hitting_ball_possibile_actions[state].append(GridAgentMovementActions.Up)
            if(self.get_cells()[(ball_cell_index[0]+1, ball_cell_index[1])] is not None):
                agent_hitting_ball_possibile_actions[state].append(GridAgentMovementActions.Down)
        agent_hitting_ball_action = rnd.choice(agent_hitting_ball_possibile_actions[state])

        return (agent_movement_action, agent_hitting_ball_action)

    """------------------------------------------------------------------------------------------------
    """ 
    def _on_action_done(self, agent, state, action, next_state_and_reward):
        pass