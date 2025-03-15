import numpy as np
import random as rnd
import devfx.machine_learning as ml

from .grid_agent_kind import GridAgentKind
from .grid_agent import GridAgent
from .grid_agent_action_ranges import GridAgentActionRanges

class GridEnvironment(ml.rl.SingleAgentEnvironment):
    def __init__(self, training=False):
        super().__init__()

        self.__training = training

        self.__action_ranges = GridAgentActionRanges()

    """------------------------------------------------------------------------------------------------
    """
    def __setup_scene(self):
        self.__scene = np.zeros(shape=(3, 8, 8), dtype=np.int8)
        
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
        self.get_scene()[1,1,6] = 100
        self.get_scene()[1,2,6] = -100

        self.get_scene()[2,:,:] = 0
        
        # agents
        agent = GridAgent(id=1, 
                          name='Johnny Walker 1', 
                          kind=GridAgentKind.WALKER, 
                          policy=ml.rl.QLearningPolicy(discount_factor=0.90, learning_rate=1e-1))

        if(self.__training == True):
            agent.set_action_randomness(1.0)
        
        self.set_agent(agent)

    def _on_set_agent(self, agent):
        self.reset()

    """------------------------------------------------------------------------------------------------
    """
    def _reset(self):
        scene = self.get_scene()
        scene[2,:,:] = 0

        agent = self.get_agent()
        choosable_ci = np.argwhere((scene[0,:,:] == ml.rl.StateKind.NON_TERMINAL) & (scene[2,:,:] == 0))
        agent_ci = rnd.choice(choosable_ci)
        scene[2,agent_ci[0],agent_ci[1]] = agent.get_id()

        agent = self.get_agent()
        agent_ci = np.argwhere(scene[2,:,:] == agent.get_id())[0]
        state = ml.rl.State(kind=scene[0,agent_ci[0],agent_ci[1]], value=scene)
        agent.set_state(state=state)

    """------------------------------------------------------------------------------------------------
    """  
    def _generate_random_action(self, agent):
        range = self.__action_ranges.get_range(name='MOVE')
        action = ml.rl.Action(*range.get_random())
        return action

    """------------------------------------------------------------------------------------------------
    """
    def _do_next_transition(self, agent, action):
        scene = self.get_scene()

        agent_ci = np.argwhere(scene[2,:,:] == agent.get_id())[0]
        agent_nci = agent_ci + action.get_value()

        if(scene[0,agent_nci[0],agent_nci[1]] == ml.rl.StateKind.UNDEFINED):
            agent_reward = ml.rl.Reward(value=scene[1,agent_nci[0],agent_nci[1]])
            agent_next_state = ml.rl.State(kind=ml.rl.StateKind.NON_TERMINAL, value=scene)
        else:
            scene[2,agent_ci[0],agent_ci[1]] = 0
            scene[2,agent_nci[0],agent_nci[1]] = agent.get_id()
            agent_reward = ml.rl.Reward(value=scene[1,agent_nci[0],agent_nci[1]])
            agent_next_state = ml.rl.State(kind=scene[0,agent_nci[0],agent_nci[1]], value=scene)
        
        return (agent_reward, agent_next_state)





