import numpy as np
import random as rnd
import devfx.machine_learning as ml

from .grid_agent_action_ranges import GridAgentActionRanges
from .grid_agent import GridAgent


class GridEnvironment(ml.rl.Environment):
    def __init__(self, training=False):
        super().__init__()

        self.training = training
        self.action_ranges = GridAgentActionRanges()

    """------------------------------------------------------------------------------------------------
    """
    def setup(self):
        # scene
        self.scene = np.zeros(shape=(3, 8, 8), dtype=np.int8)

        self.scene[0,:,:] = ml.rl.StateKind.UNDEFINED
        self.scene[0,1:-1,1:-1] = ml.rl.StateKind.NON_TERMINAL
        self.scene[0,2,2] = ml.rl.StateKind.UNDEFINED
        self.scene[0,3,3] = ml.rl.StateKind.UNDEFINED
        self.scene[0,4,4] = ml.rl.StateKind.UNDEFINED
        self.scene[0,5,5] = ml.rl.StateKind.UNDEFINED
        self.scene[0,1,6] = ml.rl.StateKind.TERMINAL
        self.scene[0,2,6] = ml.rl.StateKind.TERMINAL

        self.scene[1,:,:] = -1
        self.scene[1,1:-1,1:-1] = 0
        self.scene[1,2,2] = -1
        self.scene[1,3,3] = -1
        self.scene[1,4,4] = -1
        self.scene[1,5,5] = -1
        self.scene[1,1,6] = 100
        self.scene[1,2,6] = -100

        self.scene[2,:,:] = 0
        
        # agents
        agent = GridAgent(id=1, 
                          name='Johnny Walker 1', 
                          policy=ml.rl.QLearningPolicy(discount_factor=0.90, learning_rate=1e-1))

        if(self.training == True):
            agent.set_action_randomness(1.0)
        
        self.install_agents((agent, ))
        
        self.reset()

    """------------------------------------------------------------------------------------------------
    """
    def reset(self):
        self.scene[2,:,:] = 0

        agent = self.get_agents()[0]
        choosable_ci = np.argwhere(  (self.scene[0,:,:] == ml.rl.StateKind.NON_TERMINAL) 
                                    & (self.scene[2,:,:] == 0))
        agent_ci = rnd.choice(choosable_ci)
        self.scene[2,agent_ci[0],agent_ci[1]] = 1

        state = ml.rl.State(kind=self.scene[0,agent_ci[0],agent_ci[1]], value=self.scene)
        agent.set_state(state=state)


    """------------------------------------------------------------------------------------------------
    """  
    def generate_random_action(self, agent):
        range = self.action_ranges.get_range(name='MOVE')
        action = ml.rl.Action(*range.get_random())
        return action
    
    """------------------------------------------------------------------------------------------------
    """
    def do_next_transition(self, agent, action):   
        agent_ci = np.argwhere(self.scene[2,:,:] == 1)[0]
        agent_nci = agent_ci + action.get_value()

        if(self.scene[0,agent_nci[0],agent_nci[1]] == ml.rl.StateKind.UNDEFINED):
            agent_reward = ml.rl.Reward(value=self.scene[1,agent_nci[0],agent_nci[1]])
            agent_next_state = ml.rl.TerminalState(kind=ml.rl.StateKind.TERMINAL, value=self.scene)
            return (agent_reward, agent_next_state)

        self.scene[2,agent_ci[0],agent_ci[1]] = 0
        self.scene[2,agent_nci[0],agent_nci[1]] = 1

        agent_reward = ml.rl.Reward(value=self.scene[1,agent_nci[0],agent_nci[1]])
        agent_next_state = ml.rl.State(kind=self.scene[0,agent_nci[0],agent_nci[1]], value=self.scene)
        return (agent_reward, agent_next_state)






