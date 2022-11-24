import numpy as np
import random as rnd
import itertools as it
import devfx.core as core
import devfx.exceptions as ex
import devfx.machine_learning as ml

from .grid_agent_action_generator import GridAgentActionGenerator
from .grid_agent_kind import GridAgentKind
from .grid_agent import GridAgent

"""========================================================================================================
"""
class GridEnvironment(ml.rl.Environment):
    def __init__(self):
        super().__init__()

        self.__shape = (10, 10)
        self.__cells = {}

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
    def _create(self):
        cells = {}
        for (ri, ci) in it.product(range(1, self.shape[0]+1), range(1, self.shape[1]+1)):
            if((ri == 1) or (ri == self.shape[0]) or (ci == 1) or (ci == self.shape[1])):
                (cell_index, cell_content) = ((ri, ci), None)
            elif((ri, ci) in [(3, 3), (4, 4), (6, 6), (8, 8), (4, 8)]):
                (cell_index, cell_content) = ((ri, ci), None)
            else:
                (cell_index, cell_content) = ((ri, ci), ' ')
            cells[cell_index] = cell_content
        self.__cells = cells

    """------------------------------------------------------------------------------------------------
    """
    def _setup(self, iteration_randomness=None):
        if(not self.exists_agent(id=1)):
            self.add_agent(GridAgent(id=1, name='Wolf', kind=GridAgentKind.CHASER, 
                                     environment=self,
                                     state=self.__get_initial_state(),
                                     policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=0.1), 
                                     iteration_randomness= 0.1 if iteration_randomness is None else iteration_randomness))
        else:
            self.get_agent(id=1).set_state(self.__get_initial_state())

        if(not self.exists_agent(id=2)):       
            self.add_agent(GridAgent(id=2, name='Rabbit', kind=GridAgentKind.CHASED, 
                                     environment=self,
                                     state=self.__get_initial_state(),
                                     policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=0.1), 
                                     iteration_randomness= 0.0 if iteration_randomness is None else iteration_randomness))
        else:
            self.get_agent(id=2).set_state(self.__get_initial_state())

    def _on_added_agent(self, agent):
        for agent in self.get_agents():
           agent.set_state(self.__get_contextual_state(agent=agent))

    def _on_removed_agent(self, agent):
        for agent in self.get_agents():
           agent.set_state(self.__get_contextual_state(agent=agent))

    def __get_initial_state(self):
        agents_cell_indexes = [agent.get_state().value[0] for agent in self.get_agents()]
        choosable_cell_indexes = [cell_index for cell_index in self.cells 
                                             if((self.cells[cell_index] is not None) and (cell_index not in agents_cell_indexes))]
        random_cell_index = rnd.choice(choosable_cell_indexes)
        state = ml.rl.State(value=(random_cell_index,), kind=ml.rl.StateKind.NON_TERMINAL)
        return state

    def __get_contextual_state(self, agent):
        other_agents = self.get_other_agents(id=agent.id)
        other_agents_cell_indexes = [other_agent.get_state().value[0] for other_agent in other_agents]
        state = ml.rl.State(value=(agent.get_state().value[0], *other_agents_cell_indexes), kind=agent.get_state().kind)
        return state

    """------------------------------------------------------------------------------------------------
    """
    def _get_reward_and_next_state(self, agent, action):  
        agent_state = agent.get_state()     
        agent_cell_index = agent_state.value[0]
        if(action == GridActions.Left):
            agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1]-1)
        elif(action == GridActions.Right):
            agent_next_cell_index = (agent_cell_index[0], agent_cell_index[1]+1)
        elif(action == GridActions.Up):
            agent_next_cell_index = (agent_cell_index[0]-1, agent_cell_index[1])
        elif(action == GridActions.Down):
            agent_next_cell_index = (agent_cell_index[0]+1, agent_cell_index[1])
        else:
            raise ex.ApplicationError()

        if(self.cells[agent_next_cell_index] is None):
            agent_next_state = agent_state
            agent_reward = ml.rl.Reward(value=-1.0)
            return (agent_next_state, agent_reward)

        agent_kind = agent.get_kind()
        other_agents = self.get_other_kind_.....agents(id=agent.id)
        other_agents_cell_indexes = [other_agent.get_state().value[0] for other_agent in other_agents]
        if(agent_kind == GridAgentKind.CHASER):
            if(agent_next_cell_index in other_agents_cell_indexes):
                agent_next_state = ml.rl.State(value=(agent_next_cell_index, *other_agents_cell_indexes), kind=ml.rl.StateKind.TERMINAL)
                agent_reward = ml.rl.Reward(value=+1.0)
            else:
                agent_next_state = ml.rl.State(value=(agent_next_cell_index, *other_agents_cell_indexes), kind=ml.rl.StateKind.NON_TERMINAL)
                agent_reward = ml.rl.Reward(value=-1.0)
        elif(agent_kind == GridAgentKind.CHASED):
            if(agent_next_cell_index in other_agents_cell_indexes):
                agent_next_state = ml.rl.State(value=(agent_next_cell_index, *other_agents_cell_indexes), kind=ml.rl.StateKind.TERMINAL)
                agent_reward = ml.rl.Reward(value=-1.0)
            else:
                agent_next_state = ml.rl.State(value=(agent_next_cell_index, *other_agents_cell_indexes), kind=ml.rl.StateKind.NON_TERMINAL)
                agent_reward = ml.rl.Reward(value=+1.0)
        else:
            raise ex.ApplicationError()
        return (agent_next_state, agent_reward)

    """------------------------------------------------------------------------------------------------
    """
    def _get_available_actions(self, agent):
        actions = [GridActions.Left, GridActions.Right, GridActions.Up, GridActions.Down]
        return actions



