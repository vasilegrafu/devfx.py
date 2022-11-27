import numpy as np
import random as rnd
import devfx.machine_learning as ml

from .grid_agent_kind import GridAgentKind
from .grid_agent import GridAgent
from .grid_agent_random_policy import GridAgentRandomPolicy

class GridEnvironment(ml.rl.Environment):
    def __init__(self, training=False):
        super().__init__()
        
        self.__policy = GridAgentRandomPolicy() if training == True else ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=5e-1)

    """------------------------------------------------------------------------------------------------
    """
    def __set_scene(self, scene):
        self.__scene = scene

    def __get_scene(self):
        return self.__scene
   
    @property
    def scene_layer_shape(self):
        return self.__get_scene().shape[1:3]
    
    @property
    def state_kind_scene_layer(self):
        return self.__get_scene()[0,:,:]
    
    @property
    def reward_scene_layer(self):
        return self.__get_scene()[1,:,:]
    
    @property
    def agent_scene_layer(self):
        return self.__get_scene()[2,:,:]

    """------------------------------------------------------------------------------------------------
    """
    def _setup(self):
        # scene
        self.__set_scene(scene=np.zeros(shape=(3, 8, 8), dtype=np.int8))

        # state kind
        self.__get_scene()[0,:,:] = ml.rl.StateKind.UNDEFINED
        self.__get_scene()[0,1:-1,1:-1] = ml.rl.StateKind.NON_TERMINAL
        self.__get_scene()[0,2,2] = ml.rl.StateKind.UNDEFINED
        self.__get_scene()[0,3,3] = ml.rl.StateKind.UNDEFINED
        self.__get_scene()[0,4,4] = ml.rl.StateKind.UNDEFINED
        self.__get_scene()[0,5,5] = ml.rl.StateKind.UNDEFINED
        self.__get_scene()[0,1,6] = ml.rl.StateKind.TERMINAL
        self.__get_scene()[0,2,6] = ml.rl.StateKind.TERMINAL
        # print(self.__get_scene()[0,:,:])

        # reward
        self.__get_scene()[1,:,:] = -1
        self.__get_scene()[1,1:-1,1:-1] = 0
        self.__get_scene()[1,2,2] = -1
        self.__get_scene()[1,3,3] = -1
        self.__get_scene()[1,4,4] = -1
        self.__get_scene()[1,5,5] = -1
        self.__get_scene()[1,1,6] = +1
        self.__get_scene()[1,2,6] = -1
        # print(self.__get_scene()[1,:,:])

        # agent
        self.__get_scene()[2,:,:] = 0
        # print(self.__get_scene()[2,:,:])
        
        # agents
        agent1 = GridAgent(id=1, 
                           name='Johnny Walker 1', 
                           kind=GridAgentKind.WALKER, 
                           policy=self.__policy)
        
        self.add_agents((agent1,))

    def _on_added_agents(self, agents):
        pass

    """------------------------------------------------------------------------------------------------
    """
    def _reset(self):
        pass

    """------------------------------------------------------------------------------------------------
    """
    def _cleanup(self):
        self.remove_agents()
        self.scene = None

    def _on_removed_agents(self, agents):
        pass

    """------------------------------------------------------------------------------------------------
    """
    def _get_initial_state(self, agent):
        scene = self.__get_scene().copy()
        ci = rnd.choice(np.argwhere(scene[0,:,:] == ml.rl.StateKind.NON_TERMINAL))
        scene[2, ci[0], ci[1]] = +1
        state = ml.rl.State(scene[0, ci[0], ci[1]], scene)
        return state

    def _get_reward_and_next_state(self, agent, action):
        ci = np.argwhere(agent.get_state()[2,:,:] == 1)[0]
        next_ci = ci + action.get_value()
        if(self.__get_scene()[0, next_ci[0], next_ci[1]] == ml.rl.StateKind.UNDEFINED):
            next_state = agent.get_state()
        else:
            scene = self.__get_scene().copy()
            scene[2, next_ci[0], next_ci[1]] = +1
            next_state = ml.rl.State(scene[0, next_ci[0], next_ci[1]], scene)
        reward = ml.rl.Reward(self.__get_scene()[1, next_ci[0], next_ci[1]])
        return (reward, next_state)





