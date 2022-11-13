import numpy as np
import random as rnd
import itertools as it
import devfx.core as core
import devfx.exceptions as excps
import devfx.machine_learning as ml

from .grid_agent_action_generator import GridAgentActionGenerator
from .grid_agent_kind import GridAgentKind
from .grid_agent import GridAgent

"""========================================================================================================
"""
class GridEnvironment(ml.rl.Environment):
    def __init__(self):
        super().__init__()

        self.__shape = (8, 8)
        self.__env = np.zeros(shape=[*self.__shape, 3])

        self.__actionGenerator = GridAgentActionGenerator()

    """------------------------------------------------------------------------------------------------
    """
    @property
    def shape(self):  
        return self.__shape

    @property
    def model(self):
        return self.__model

    """------------------------------------------------------------------------------------------------
    """
    def _create(self):
        # state kind
        self.env[:,:,0] = ml.rl.StateKind.UNDEFINED
        self.env[1:-1,1:-1,0] = ml.rl.StateKind.NON_TERMINAL
        self.env[2,2,0] = ml.rl.StateKind.UNDEFINED
        self.env[3,3,0] = ml.rl.StateKind.UNDEFINED
        self.env[5,5,0] = ml.rl.StateKind.UNDEFINED
        self.env[1,6,0] = ml.rl.StateKind.TERMINAL
        self.env[2,6,0] = ml.rl.StateKind.TERMINAL
        #print(self.env[:,:,0])

        # reward
        self.env[:,:,1] = -1
        self.env[1:-1,1:-1,1] = 0
        self.env[2,2,1] = -1
        self.env[3,3,1] = -1
        self.env[5,5,1] = -1
        self.env[1,6,1] = +1
        self.env[2,6,1] = -1
        #print(self.env[:,:,1])

        # agent
        self.env[:,:,2] = 0
        #print(self.env[:,:,2])

    """------------------------------------------------------------------------------------------------
    """
    def _setup(self, iteration_randomness=None):
        if(not self.exists_agent(id=1)):
            self.add_agent(GridAgent(id=1, 
                                     name='Johnny Walker 1', 
                                     kind=GridAgentKind.WALKER, 
                                     environment=self, 
                                     state=self.__get_initial_state(),
                                     policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=1e-1),
                                     iteration_randomness= 0.1 if iteration_randomness is None else iteration_randomness))
        else:
            self.get_agent(id=1).set_state(self.__get_initial_state())

    def _on_added_agent(self, agent):
        pass

    def _on_removed_agent(self, agent):
        pass

    def __get_initial_state(self):
        env = self.env.copy()
        ci = rnd.choice(np.argwhere(env[:,:,0] == ml.rl.StateKind.NON_TERMINAL))
        env[ci[0], ci[1], 2] = +1
        state = ml.rl.State(env[ci[0], ci[1], 0], env)
        return state

    """------------------------------------------------------------------------------------------------
    """
    def _get_next_state_and_reward(self, agent, action):
        agent_state = agent.get_state()
        agent_ci = np.argwhere(agent_state[:,:,2] == 1)[0]
        agent_next_ci = agent_ci + action.value
        if(self.env[agent_next_ci[0], agent_next_ci[1], 0] == ml.rl.StateKind.UNDEFINED):
            agent_next_state = agent_state
        else:
            env = self.env.copy()
            env[agent_next_ci[0], agent_next_ci[1], 2] = +1
            agent_next_state = ml.rl.State(env[agent_next_ci[0], agent_next_ci[1], 0], env)
        agent_next_reward = ml.rl.Reward(env[agent_next_ci[0], agent_next_ci[1], 1])
        return (agent_next_state, agent_next_reward)

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_action(self, agent):
        action = self.__actionGenerator.get_random()
        return action





