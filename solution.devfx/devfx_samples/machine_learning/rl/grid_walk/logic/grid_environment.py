import numpy as np
import random as rnd
import devfx.machine_learning as ml

from .grid_agent_kind import GridAgentKind
from .grid_agent import GridAgent

class GridEnvironment(ml.rl.Environment):
    def __init__(self, training=False):
        super().__init__()

        self.__training = training

    """------------------------------------------------------------------------------------------------
    """
    def setup(self):
        # scene
        self.__scene = np.zeros(shape=(3, 8, 8), dtype=np.int8)

        self.__scene[0,:,:] = ml.rl.StateKind.UNDEFINED
        self.__scene[0,1:-1,1:-1] = ml.rl.StateKind.NON_TERMINAL
        self.__scene[0,2,2] = ml.rl.StateKind.UNDEFINED
        self.__scene[0,3,3] = ml.rl.StateKind.UNDEFINED
        self.__scene[0,4,4] = ml.rl.StateKind.UNDEFINED
        self.__scene[0,5,5] = ml.rl.StateKind.UNDEFINED
        self.__scene[0,1,6] = ml.rl.StateKind.TERMINAL
        self.__scene[0,2,6] = ml.rl.StateKind.TERMINAL

        self.__scene[1,:,:] = -1
        self.__scene[1,1:-1,1:-1] = 0
        self.__scene[1,2,2] = -1
        self.__scene[1,3,3] = -1
        self.__scene[1,4,4] = -1
        self.__scene[1,5,5] = -1
        self.__scene[1,1,6] = 100
        self.__scene[1,2,6] = -100

        self.__scene[2,:,:] = 0
        
        # agents
        agent = GridAgent(id=1, 
                          name='Johnny Walker 1', 
                          kind=GridAgentKind.WALKER, 
                          policy=ml.rl.QLearningPolicy(discount_factor=0.90, learning_rate=1e-1))

        if(self.__training == True):
            agent.set_action_randomness(1.0)
        
        self.install_agents((agent, ))

        self.reset()

    """------------------------------------------------------------------------------------------------
    """
    def reset(self):
        scene = self.__scene
        scene[2,:,:] = 0

        agent = self.get_agents()[0]
        choosable_ci = np.argwhere((scene[0,:,:] == ml.rl.StateKind.NON_TERMINAL) & (scene[2,:,:] == 0))
        agent_ci = rnd.choice(choosable_ci)
        scene[2,agent_ci[0],agent_ci[1]] = 1

        agent = self.get_agents()[0]
        agent_ci = np.argwhere(scene[2,:,:] == 1)[0]
        state = ml.rl.State(kind=scene[0,agent_ci[0],agent_ci[1]], value=scene)
        agent.set_state(state=state)

    """------------------------------------------------------------------------------------------------
    """
    def get_scene(self):
        return self.__scene

    """------------------------------------------------------------------------------------------------
    """ 
    def do_iteration(self, log_transition=False):
        for agent in self.get_agents():
            if(self.has_agents_in_terminal_state()):
                self.reset()
            else:
                agent.do_action(log_transition=log_transition)

    def do_iterations(self, n, log_transition=False):
        for i in range(0, n):
            self.do_iteration(log_transition=log_transition)






