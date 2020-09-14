import numpy as np
import random as rnd
import itertools as it
import devfx.core as core
import devfx.exceptions as exps
import devfx.machine_learning as ml

from .grid_actions import GridActions
from .grid_agent_kind import GridAgentKind
from .grid_agent import GridAgent

"""========================================================================================================
"""
class GridEnvironment(ml.rl.Environment):
    def __init__(self):
        super().__init__()

    # """------------------------------------------------------------------------------------------------
    # """
    # @property
    # def shape(self):  
    #     return (8, 8)

    # @property
    # def template_layer(self):
    #     cells = np.zeros(shape=self.shape, dtype=np.int8)
    #     cells[(3, 3)] = 1
    #     cells[(4, 4)] = 1
    #     cells[(6, 6)] = 1
    #     return cells

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

    """------------------------------------------------------------------------------------------------
    """
    def _create(self):
        self.__create_cells()

        self.setup()

    """------------------------------------------------------------------------------------------------
    """
    def _setup(self):
        if(not self.exists_agent(id=1)):
            self.add_agent(GridAgent(id=1, name='Wolf', kind=GridAgentKind.CHASER, 
                                     environment=self,
                                     policy=ml.rl.ESarsaPolicy(discount_factor=0.99, learning_rate=0.01), 
                                     randomness=0.05))
        else:
            self.__setup_positional_state(self.get_agent(id=1))

        if(not self.exists_agent(id=2)):             
            self.add_agent(GridAgent(id=2, name='Rabbit', kind=GridAgentKind.CHASED, 
                                     environment=self,
                                     policy=ml.rl.ESarsaPolicy(discount_factor=0.99, learning_rate=0.01), 
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
        other_agents = self.get_other_agents(id=agent.get_id())
        other_agents_cell_indexes = [other_agent.get_state().value[0] for other_agent in other_agents]
        choosable_cell_indexes = [cell_index for cell_index in self.get_walkable_cells() if(cell_index not in other_agents_cell_indexes)]
        random_cell_index = rnd.choice(choosable_cell_indexes)
        state = ml.rl.State(value=(random_cell_index, ), kind=ml.rl.StateKind.NON_TERMINAL)
        agent.set_state(state)

    def __setup_contextual_state(self, agent):
        other_kind_agents = self.get_other_kind_agents(kind=agent.get_kind())
        other_kind_agents_cell_indexes = [other_kind_agent.get_state().value[0] for other_kind_agent in other_kind_agents]
        state = ml.rl.State(value=(agent.get_state().value[0], *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.NON_TERMINAL)
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
        agent_cell_index = state.value[0]
        if(action == GridActions.Left):
            agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1]-1)
        elif(action == GridActions.Right):
            agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1]+1)
        elif(action == GridActions.Up):
            agent_next_cell_index = (agent_cell_index[0]-1, agent_cell_index[1])
        elif(action == GridActions.Down):
            agent_next_cell_index = (agent_cell_index[0]+1, agent_cell_index[1])
        else:
            raise exps.ApplicationError()

        if(agent_next_cell_index not in self.get_walkable_cells()):
            raise exps.ApplicationError()

        agent_kind = agent.get_kind()
        other_kind_agents = self.get_other_kind_agents(kind=agent_kind)
        other_kind_agents_cell_indexes = [other_kind_agent.get_state().value[0] for other_kind_agent in other_kind_agents]
        if(agent_next_cell_index not in other_kind_agents_cell_indexes):
            next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.NON_TERMINAL)
            if(agent_kind == GridAgentKind.CHASER):
                next_reward = ml.rl.Reward(value=-1.0)
            elif(agent_kind == GridAgentKind.CHASED):
                next_reward = ml.rl.Reward(value=+1.0)
            else:
                raise exps.ApplicationError()
        else:
            next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.TERMINAL)
            if(agent_kind == GridAgentKind.CHASER):
                next_reward = ml.rl.Reward(value=+10000.0)
            elif(agent_kind == GridAgentKind.CHASED):
                next_reward = ml.rl.Reward(value=-10000.0)
            else:
                raise exps.ApplicationError()

        return (next_state, next_reward)

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_action(self, agent, state):           
        possibile_actions = core.ObjectStorage.intercept(self, 'possibile_actions', lambda: {})
        if(state not in possibile_actions):       
            possibile_actions[state] = []
            agent_cell_index = state.value[0]
            if(self.get_cells()[(agent_cell_index[0], agent_cell_index[1]-1)] is not None):
                possibile_actions[state].append(GridActions.Left)
            if(self.get_cells()[(agent_cell_index[0], agent_cell_index[1]+1)] is not None):
                possibile_actions[state].append(GridActions.Right) 
            if(self.get_cells()[(agent_cell_index[0]-1, agent_cell_index[1])] is not None):
                possibile_actions[state].append(GridActions.Up)
            if(self.get_cells()[(agent_cell_index[0]+1, agent_cell_index[1])] is not None):
                possibile_actions[state].append(GridActions.Down)
        action = rnd.choice(possibile_actions[state])
        return action
 


