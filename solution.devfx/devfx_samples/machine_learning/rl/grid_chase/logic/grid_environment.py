import numpy as np
import random as rnd
import devfx.exceptions as exp
import devfx.machine_learning as ml

from .grid_agent_kind import GridAgentKind
from .grid_chased_agent import GridChasedAgent
from .grid_chaser_agent import GridChaserAgent
from .grid_agent_action_ranges import GridAgentActionRanges

class GridEnvironment(ml.rl.Environment):
    def __init__(self, training=False):
        super().__init__()

        self.training = training
        self.action_ranges = GridAgentActionRanges()

    """------------------------------------------------------------------------------------------------
    """
    def setup(self):
        # scene
        self.scene = np.zeros(shape=(3, 7, 7), dtype=np.int8)

        self.scene[0,:,:] = 1
        self.scene[0,1:-1,1:-1] = 0
        self.scene[0,2,2] = 1
        self.scene[0,3,3] = 0
        self.scene[0,5,5] = 1
        # self.scene[0,7,7] = 1
        # self.scene[0,3,7] = 1

        self.scene[1,:,:] = 0
        self.scene[2,:,:] = 0
        
        # agents
        agent1 = GridChasedAgent(id=1, 
                                 name='Rabbit', 
                                 policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=1e-1))
        if(self.training == True):
            agent1.set_action_randomness(1.0)

        agent2 = GridChaserAgent(id=2, 
                                 name='Wolf', 
                                 policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=1e-1))
        if(self.training == True):
            agent2.set_action_randomness(1.0)
        
        self.install_agents((agent1, agent2))

        self.reset()

    """------------------------------------------------------------------------------------------------
    """
    def reset(self):       
        for agent in self.get_agents():
            self.scene[agent.get_id(),:,:] = 0
            choosable_ci = np.argwhere(  (self.scene[0,:,:] == 0) 
                                       & (self.scene[1,:,:] == 0) 
                                       & (self.scene[2,:,:] == 0))
            agent_ci = rnd.choice(choosable_ci)
            self.scene[agent.get_id(),agent_ci[0],agent_ci[1]] = 1

        for agent in self.get_agents():
            state = ml.rl.State(kind=ml.rl.StateKind.NON_TERMINAL, value=self.scene)
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
        #----------------------------------------------------------------
        if(agent.get_kind() == GridAgentKind.CHASED):
            agent_ci = np.argwhere(self.scene[1,:,:] == 1)[0]
            agent_next_ci = agent_ci + action.get_value()
            
            if(self.scene[0,agent_next_ci[0],agent_next_ci[1]] == 1):
                agent_reward = ml.rl.Reward(value=-1)
                agent_next_state = ml.rl.TerminalState(value=self.scene)
                return (agent_reward, agent_next_state)

            self.scene[1,agent_ci[0],agent_ci[1]] = 0
            self.scene[1,agent_next_ci[0],agent_next_ci[1]] = 1

            other_agent_ci = np.argwhere(self.scene[2,:,:] == 1)[0]
            if(np.equal(agent_next_ci, other_agent_ci).all()):
                agent_reward = ml.rl.Reward(value=-1.0)
                agent_next_state = ml.rl.TerminalState(value=self.scene)
            else:
                agent_reward = ml.rl.Reward(value=+1.0)
                agent_next_state = ml.rl.NonTerminalState(value=self.scene)
            return (agent_reward, agent_next_state)

        #----------------------------------------------------------------
        if(agent.get_kind() == GridAgentKind.CHASER):
            agent_ci = np.argwhere(self.scene[2,:,:] == 1)[0]
            agent_next_ci = agent_ci + action.get_value()
            
            if(self.scene[0,agent_next_ci[0],agent_next_ci[1]] == 1):
                agent_reward = ml.rl.Reward(value=-1)
                agent_next_state = ml.rl.TerminalState(value=self.scene)
                return (agent_reward, agent_next_state)

            self.scene[2,agent_ci[0],agent_ci[1]] = 0
            self.scene[2,agent_next_ci[0],agent_next_ci[1]] = 1

            other_agent_ci = np.argwhere(self.scene[1,:,:] == 1)[0]
            if(np.equal(agent_next_ci, other_agent_ci).all()):
                agent_reward = ml.rl.Reward(value=+1.0)
                agent_next_state = ml.rl.TerminalState(value=self.scene)
            else:
                agent_reward = ml.rl.Reward(value=-1.0)
                agent_next_state = ml.rl.NonTerminalState(value=self.scene)
            return (agent_reward, agent_next_state)
        
        #----------------------------------------------------------------
        raise exp.ApplicationError()