import numpy as np
import random as rnd
import itertools as it
import devfx.core as core
import devfx.exceptions as excs
import devfx.machine_learning as ml

from .grid_actions import GridActions
from .grid_agent_kind import GridAgentKind
from .grid_agent import GridAgent

"""========================================================================================================
"""
class GridEnvironment(ml.rl.Environment):
    def __init__(self):
        super().__init__()

        self.__shape = (10, 10)
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
            self.set_agent_kind_policy(agent_kind=GridAgentKind.CHASER, policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=0.1))
            self.add_agent(GridAgent(id=1, name='Wolf', kind=GridAgentKind.CHASER, 
                                     environment=self,
                                     policy=self.get_agent_kind_policy(GridAgentKind.CHASER), 
                                     iteration_randomness= 0.1 if iteration_randomness is None else iteration_randomness))
        else:
            self.__setup_positional_state(self.get_agent(id=1))

        if(not self.exists_agent(id=2)):      
            self.set_agent_kind_policy(agent_kind=GridAgentKind.CHASED, policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=0.1))       
            self.add_agent(GridAgent(id=2, name='Rabbit', kind=GridAgentKind.CHASED, 
                                     environment=self,
                                     policy=self.get_agent_kind_policy(GridAgentKind.CHASED), 
                                     iteration_randomness= 0.0 if iteration_randomness is None else iteration_randomness))
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
        other_agents_cell_indexes = [other_agent.get_state().value[0] for other_agent in self.get_other_agents(id=agent.get_id())]
        choosable_cell_indexes = [cell_index for cell_index in self.cells 
                                             if((self.cells[cell_index] is not None) and (cell_index not in other_agents_cell_indexes))]
        random_cell_index = rnd.choice(choosable_cell_indexes)
        state = ml.rl.State(value=(random_cell_index,), kind=ml.rl.StateKind.NON_TERMINAL)
        agent.set_state(state)

    def __setup_contextual_state(self, agent):
        other_kind_agents_cell_indexes = [other_kind_agent.get_state().value[0] for other_kind_agent in self.get_agents_not_like(kind=agent.get_kind())]
        state = ml.rl.State(value=(agent.get_state().value[0], *other_kind_agents_cell_indexes), kind=agent.get_state().kind)
        agent.set_state(state)

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
            raise excs.ApplicationError()

        if(self.cells[agent_next_cell_index] is None):
            next_state = state
            next_reward = ml.rl.Reward(value=-1.0)
            return (next_state, next_reward)

        agent_kind = agent.get_kind()
        other_kind_agents = self.get_agents_not_like(kind=agent_kind)
        other_kind_agents_cell_indexes = [other_kind_agent.get_state().value[0] for other_kind_agent in other_kind_agents]
        if(agent_kind == GridAgentKind.CHASER):
            if(agent_next_cell_index in other_kind_agents_cell_indexes):
                next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.TERMINAL)
                next_reward = ml.rl.Reward(value=+1.0)
            else:
                next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.NON_TERMINAL)
                next_reward = ml.rl.Reward(value=-1.0)
        elif(agent_kind == GridAgentKind.CHASED):
            if(agent_next_cell_index in other_kind_agents_cell_indexes):
                next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.TERMINAL)
                next_reward = ml.rl.Reward(value=-1.0)
            else:
                next_state = ml.rl.State(value=(agent_next_cell_index, *other_kind_agents_cell_indexes), kind=ml.rl.StateKind.NON_TERMINAL)
                next_reward = ml.rl.Reward(value=+1.0)
        else:
            raise excs.ApplicationError()
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
 


