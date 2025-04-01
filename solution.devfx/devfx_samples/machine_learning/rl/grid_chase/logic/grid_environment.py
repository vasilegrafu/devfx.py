import numpy as np
import random as rnd
import devfx.machine_learning as ml

from .grid_chased_agent import GridChasedAgent
from .grid_chaser_agent import GridChaserAgent

class GridEnvironment(ml.rl.Environment):
    def __init__(self, training=False):
        super().__init__()

        self.__training = training

    """------------------------------------------------------------------------------------------------
    """
    def setup(self):
        # scene
        self.__scene = np.zeros(shape=(3, 8, 8), dtype=np.int8)

        self.get_scene()[0,:,:] = 1
        self.get_scene()[0,1:-1,1:-1] = 0
        self.get_scene()[0,2,2] = 1
        self.get_scene()[0,3,3] = 1
        self.get_scene()[0,5,5] = 1
        self.get_scene()[0,7,7] = 1
        self.get_scene()[0,3,7] = 1

        self.get_scene()[1,:,:] = 0
        self.get_scene()[2,:,:] = 0
        
        # agents
        agent1 = GridChasedAgent(id=1, 
                                 name='Rabbit', 
                                 policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=1e-1))
        if(self.__training == True):
            agent1.set_action_randomness(1.0)

        agent2 = GridChaserAgent(id=2, 
                                 name='Wolf', 
                                 policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=1e-1))
        if(self.__training == True):
            agent2.set_action_randomness(1.0)
        
        self.install_agents((agent1, agent2))

        self.reset()

    """------------------------------------------------------------------------------------------------
    """
    def reset(self):
        scene = self.get_scene()
        
        for agent in self.get_agents():
            scene[agent.get_id(),:,:] = 0
            choosable_ci = np.argwhere(  (scene[0,:,:] == 0) 
                                       & (scene[1,:,:] == 0) 
                                       & (scene[2,:,:] == 0))
            agent_ci = rnd.choice(choosable_ci)
            scene[agent.get_id(),agent_ci[0],agent_ci[1]] = 1

        for agent in self.get_agents():
            state = ml.rl.State(kind=ml.rl.StateKind.NON_TERMINAL, value=scene)
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



