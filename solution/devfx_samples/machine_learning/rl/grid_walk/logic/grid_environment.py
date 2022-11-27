import numpy as np
import random as rnd
import devfx.machine_learning as ml

from .grid_agent_kind import GridAgentKind
from .grid_agent import GridAgent
from .grid_agent_random_policy import GridAgentRandomPolicy

class GridEnvironment(ml.rl.Environment):
    def __init__(self, training=False):
        super().__init__()

        self.__training = training
        
    """------------------------------------------------------------------------------------------------
    """
    def __setup_scene(self):
        self.__scene = np.zeros(shape=(3, 8, 8), dtype=np.int8)
        
    def __cleanup_scene(self):
        self.__scene = None

    def get_scene(self):
        return self.__scene

    """------------------------------------------------------------------------------------------------
    """
    def _setup(self):
        # scene
        self.__setup_scene()

        self.get_scene()[0,:,:] = ml.rl.StateKind.UNDEFINED
        self.get_scene()[0,1:-1,1:-1] = ml.rl.StateKind.NON_TERMINAL
        self.get_scene()[0,2,2] = ml.rl.StateKind.UNDEFINED
        self.get_scene()[0,3,3] = ml.rl.StateKind.UNDEFINED
        self.get_scene()[0,4,4] = ml.rl.StateKind.UNDEFINED
        self.get_scene()[0,5,5] = ml.rl.StateKind.UNDEFINED
        self.get_scene()[0,1,6] = ml.rl.StateKind.TERMINAL
        self.get_scene()[0,2,6] = ml.rl.StateKind.TERMINAL

        self.get_scene()[1,:,:] = -1
        self.get_scene()[1,1:-1,1:-1] = 0
        self.get_scene()[1,2,2] = -1
        self.get_scene()[1,3,3] = -1
        self.get_scene()[1,4,4] = -1
        self.get_scene()[1,5,5] = -1
        self.get_scene()[1,1,6] = +1
        self.get_scene()[1,2,6] = -1

        self.get_scene()[2,:,:] = 0
        
        # agents
        agent1 = GridAgent(id=1, 
                           name='Johnny Walker 1', 
                           kind=GridAgentKind.WALKER, 
                           policy=GridAgentRandomPolicy() if self.__training == True else ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=5e-1))
        
        self.add_agents((agent1,))

    def _on_added_agents(self, agents):
        scene = self.get_scene()

        for agent in agents:
            choosable_ci = np.argwhere((scene[0,:,:] == ml.rl.StateKind.NON_TERMINAL) & (scene[2,:,:] == 0))
            ci = rnd.choice(choosable_ci)
            scene[2, ci[0], ci[1]] = agent.get_id()

        for agent in self.get_agents():
            ci = np.argwhere(scene[2,:,:] == agent.get_id())[0]
            state = ml.rl.State(kind=scene[0, ci[0], ci[1]], value=scene.copy())
            agent.set_state(state=state)

    """------------------------------------------------------------------------------------------------
    """
    def _reset(self):
        scene = self.get_scene()
        scene[2,:,:] = 0

        for agent in self.get_agents():
            choosable_ci = np.argwhere((scene[0,:,:] == ml.rl.StateKind.NON_TERMINAL) & (scene[2,:,:] == 0))
            ci = rnd.choice(choosable_ci)
            scene[2, ci[0], ci[1]] = agent.get_id()

        for agent in self.get_agents():
            ci = np.argwhere(scene[2,:,:] == agent.get_id())[0]
            state = ml.rl.State(kind=scene[0, ci[0], ci[1]], value=scene.copy())
            agent.set_state(state=state)

    """------------------------------------------------------------------------------------------------
    """
    def _cleanup(self):
        self.remove_agents()
        self.__cleanup_scene()

    def _on_removed_agents(self, agents):
        scene = self.get_scene()
        scene[2,:,:] = 0

    """------------------------------------------------------------------------------------------------
    """
    def _do_action(self, agent, action):
        scene = self.get_scene()

        ci = np.argwhere(scene[2,:,:] == agent.get_id())[0]
        nci = ci + action.get_value()

        reward = ml.rl.Reward(value=scene[1, nci[0], nci[1]])

        if(scene[0, nci[0], nci[1]] == ml.rl.StateKind.UNDEFINED):
            next_state = agent.get_state()
        else:
            scene[2, ci[0], ci[1]] = 0
            scene[2, nci[0], nci[1]] = agent.get_id()
            next_state = ml.rl.State(kind=scene[0, nci[0], nci[1]], value=scene.copy())
        
        return (reward, next_state)





