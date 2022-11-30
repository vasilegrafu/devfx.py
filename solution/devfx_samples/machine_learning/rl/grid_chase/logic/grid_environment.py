import numpy as np
import random as rnd
import devfx.exceptions as ex
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
        self.__scene = np.zeros(shape=(3, 10, 10), dtype=np.int8)
        
    def __cleanup_scene(self):
        self.__scene = None

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
                           policy=GridAgentRandomPolicy() if self.__training == True else ml.rl.QLearningPolicy(discount_factor=0.99, learning_rate=5e-1))
        agent2 = GridAgent(id=2, 
                           name='Rabbit', 
                           kind=GridAgentKind.CHASED, 
                           policy=GridAgentRandomPolicy() if self.__training == True else ml.rl.QLearningPolicy(discount_factor=0.99, learning_rate=5e-1))
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
            ci = rnd.choice(choosable_ci)
            scene[agent.get_id(),ci[0],ci[1]] = agent.get_id()

        for agent in self.get_agents():
            ci = np.argwhere(scene[agent.get_id(),:,:] == agent.get_id())[0]
            state = ml.rl.State(kind=ml.rl.StateKind.NON_TERMINAL, value=scene)
            agent.set_state(state=state)

    """------------------------------------------------------------------------------------------------
    """
    def _cleanup(self):
        self.remove_agents()
        self.__cleanup_scene()

    def _on_removed_agents(self, agents):
        scene = self.get_scene()
        scene[1,:,:] = 0
        scene[2,:,:] = 0

    """------------------------------------------------------------------------------------------------
    """
    def _do_next_transition(self, agent, action):
        scene = self.get_scene()

        agent_ci = np.argwhere(scene[agent.get_id(),:,:] == agent.get_id())[0]
        agent_next_ci = agent_ci + action.get_value()
        
        scene[agent.get_id(),agent_ci[0],agent_ci[1]] = 0
        scene[agent.get_id(),agent_next_ci[0],agent_next_ci[1]] = agent.get_id()

        other_agent = self.get_agents_others_than(id=agent.get_id())[0]

        if(scene[0,agent_next_ci[0],agent_next_ci[1]] == 1):
            agent_reward = ml.rl.Reward(value=-1e+3)
            agent_next_state = ml.rl.State(kind=ml.rl.StateKind.TERMINAL, value=scene)
            # other_agent_state = ml.rl.State(kind=ml.rl.StateKind.TERMINAL, value=scene)
        else:
            other_agent_ci = np.argwhere(scene[other_agent.get_id(),:,:] == other_agent.get_id())[0]
            if(np.equal(agent_next_ci, other_agent_ci).all()):
                match agent.get_kind():
                    case GridAgentKind.CHASER:   
                        agent_reward = ml.rl.Reward(value=+1e+3)
                        agent_next_state = ml.rl.State(kind=ml.rl.StateKind.TERMINAL, value=scene)
                        # other_agent_state = ml.rl.State(kind=ml.rl.StateKind.TERMINAL, value=scene)
                    case GridAgentKind.CHASED: 
                        agent_reward = ml.rl.Reward(value=-1e+3)
                        agent_next_state = ml.rl.State(kind=ml.rl.StateKind.TERMINAL, value=scene)
                        # other_agent_state = ml.rl.State(kind=ml.rl.StateKind.TERMINAL, value=scene)
            else:
                agent_reward = ml.rl.Reward(value=0)
                agent_next_state = ml.rl.State(kind=ml.rl.StateKind.NON_TERMINAL, value=scene)
                # other_agent_state = ml.rl.State(kind=ml.rl.StateKind.NON_TERMINAL, value=scene)
        
        # other_agent.set_state(state=other_agent_state)
        
        return (agent_reward, agent_next_state)



