import numpy as np
import random as rnd
import devfx.machine_learning as ml

from .grid_agent_kind import GridAgentKind
from .grid_agent import GridAgent
from .grid_agent_action_ranges import GridAgentActionRanges

class GridEnvironment(ml.rl.Environment):
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
        agent1 = GridAgent(id=1, 
                           name='Wolf', 
                           kind=GridAgentKind.CHASER, 
                           policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=1e-1))
        if(self.__training == True):
            agent1.set_action_randomness(1.0)

        agent2 = GridAgent(id=2, 
                           name='Rabbit', 
                           kind=GridAgentKind.CHASED, 
                           policy=ml.rl.QLearningPolicy(discount_factor=0.95, learning_rate=1e-1))
        if(self.__training == True):
            agent2.set_action_randomness(1.0)
        
        self.add_agents((agent1, agent2))

    def _on_added_agents(self, agents):
        self.reset()

    """------------------------------------------------------------------------------------------------
    """
    def _reset(self):
        scene = self.get_scene()
        
        for agent in self.get_agents():
            scene[agent.get_id(),:,:] = 0
            choosable_ci = np.argwhere(  (scene[0,:,:] == 0) 
                                       & (scene[1,:,:] == 0) 
                                       & (scene[2,:,:] == 0))
            agent_ci = rnd.choice(choosable_ci)
            scene[agent.get_id(),agent_ci[0],agent_ci[1]] = agent.get_id()

        for agent in self.get_agents():
            state = ml.rl.State(kind=ml.rl.StateKind.NON_TERMINAL, value=scene)
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

        agent_ci = np.argwhere(scene[agent.get_id(),:,:] == agent.get_id())[0]
        match agent.get_kind():
            case GridAgentKind.CHASER:   
                agent_next_ci = agent_ci + action.get_value()
            case GridAgentKind.CHASED: 
                agent_next_ci = agent_ci + action.get_value()
        
        if(scene[0,agent_next_ci[0],agent_next_ci[1]] == 1):
            agent_reward = ml.rl.Reward(value=-1)
            agent_next_state = ml.rl.State(kind=ml.rl.StateKind.NON_TERMINAL, value=scene)
        else:
            scene[agent.get_id(),agent_ci[0],agent_ci[1]] = 0
            scene[agent.get_id(),agent_next_ci[0],agent_next_ci[1]] = agent.get_id()

            other_agent = self.get_agents_others_than(id=agent.get_id())[0]
            other_agent_ci = np.argwhere(scene[other_agent.get_id(),:,:] == other_agent.get_id())[0]
            if(np.equal(agent_next_ci, other_agent_ci).all()):
                match agent.get_kind():
                    case GridAgentKind.CHASER:   
                        agent_reward = ml.rl.Reward(value=+1.0)
                        agent_next_state = ml.rl.State(kind=ml.rl.StateKind.TERMINAL, value=scene)
                    case GridAgentKind.CHASED: 
                        agent_reward = ml.rl.Reward(value=-1.0)
                        agent_next_state = ml.rl.State(kind=ml.rl.StateKind.TERMINAL, value=scene)
            else:
                match agent.get_kind():
                    case GridAgentKind.CHASER:   
                        agent_reward = ml.rl.Reward(value=-1.0)
                        agent_next_state = ml.rl.State(kind=ml.rl.StateKind.NON_TERMINAL, value=scene)
                    case GridAgentKind.CHASED: 
                        agent_reward = ml.rl.Reward(value=+1.0)
                        agent_next_state = ml.rl.State(kind=ml.rl.StateKind.NON_TERMINAL, value=scene)
              
        return (agent_reward, agent_next_state)



