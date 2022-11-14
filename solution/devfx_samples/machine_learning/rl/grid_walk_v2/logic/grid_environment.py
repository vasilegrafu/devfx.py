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

        self.__set_scene(scene=np.zeros(shape=[8, 8, 3]))

        self.__actionGenerator = GridAgentActionGenerator()

    """------------------------------------------------------------------------------------------------
    """
    def __set_scene(self, scene):
        self.__scene = scene

    @property
    def scene(self):
        return self.__scene

    """------------------------------------------------------------------------------------------------
    """
    def _create(self):
        # state kind
        self.scene[:,:,0] = ml.rl.StateKind.UNDEFINED
        self.scene[1:-1,1:-1,0] = ml.rl.StateKind.NON_TERMINAL
        self.scene[2,2,0] = ml.rl.StateKind.UNDEFINED
        self.scene[3,3,0] = ml.rl.StateKind.UNDEFINED
        self.scene[5,5,0] = ml.rl.StateKind.UNDEFINED
        self.scene[1,6,0] = ml.rl.StateKind.TERMINAL
        self.scene[2,6,0] = ml.rl.StateKind.TERMINAL
        #print(self.scene[:,:,0])

        # reward
        self.scene[:,:,1] = -1
        self.scene[1:-1,1:-1,1] = 0
        self.scene[2,2,1] = -1
        self.scene[3,3,1] = -1
        self.scene[5,5,1] = -1
        self.scene[1,6,1] = +1
        self.scene[2,6,1] = -1
        #print(self.scene[:,:,1])

        # agent
        self.scene[:,:,2] = 0
        #print(self.scene[:,:,2])

    """------------------------------------------------------------------------------------------------
    """
    def _setup(self, iteration_randomness=None):
        if(not self.exists_agent(id=1)):
            self.add_agent(GridAgent(id=1, 
                                     name='Johnny Walker 1', 
                                     kind=GridAgentKind.WALKER, 
                                     environment=self, 
                                     state=self.__get_initial_state(),
                                     policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=5e-1),
                                     iteration_randomness= 0.1 if iteration_randomness is None else iteration_randomness))
        else:
            self.get_agent(id=1).set_state(self.__get_initial_state())

    def _on_added_agent(self, agent):
        pass

    def _on_removed_agent(self, agent):
        pass

    """------------------------------------------------------------------------------------------------
    """
    def __get_initial_state(self):
        scene = self.scene.copy()
        ci = rnd.choice(np.argwhere(scene[:,:,0] == ml.rl.StateKind.NON_TERMINAL))
        scene[ci[0], ci[1], 2] = +1
        state = ml.rl.State(scene[ci[0], ci[1], 0], scene)
        return state

    def _get_next_state_and_reward(self, agent, action):
        ci = np.argwhere(agent.get_state()[:,:,2] == 1)[0]
        next_ci = ci + action.value
        if(self.scene[next_ci[0], next_ci[1], 0] == ml.rl.StateKind.UNDEFINED):
            next_state = agent.get_state()
        else:
            scene = self.scene.copy()
            scene[next_ci[0], next_ci[1], 2] = +1
            next_state = ml.rl.State(scene[next_ci[0], next_ci[1], 0], scene)
        next_reward = ml.rl.Reward(self.scene[next_ci[0], next_ci[1], 1])
        return (next_state, next_reward)

    """------------------------------------------------------------------------------------------------
    """
    def _get_random_action(self, agent):
        action = self.__actionGenerator.get_random()
        return action





