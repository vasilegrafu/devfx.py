import numpy as np
import devfx.machine_learning as ml
from .grid_agent_kind import GridAgentKind
from .grid_agent_action_ranges import GridAgentActionRanges

class GridChasedAgent(ml.rl.Agent):
    def __init__(self, id, name, policy):
        super().__init__(id=id, name=name, kind=GridAgentKind.CHASED, policy=policy)

        self.__action_ranges = GridAgentActionRanges()

    """------------------------------------------------------------------------------------------------
    """  
    def generate_random_action(self):
        range = self.__action_ranges.get_range(name='MOVE')
        action = ml.rl.Action(*range.get_random())
        return action

    """------------------------------------------------------------------------------------------------
    """  
    def do_next_transition(self, action):
        scene = self.get_environment().get_scene()

        agent_ci = np.argwhere(scene[1,:,:] == 1)[0]
        agent_next_ci = agent_ci + action.get_value()
        
        if(scene[0,agent_next_ci[0],agent_next_ci[1]] == 1):
            agent_reward = ml.rl.Reward(value=-1)
            agent_next_state = ml.rl.State(kind=ml.rl.StateKind.TERMINAL, value=scene)
            return (agent_reward, agent_next_state)

        scene[1,agent_ci[0],agent_ci[1]] = 0
        scene[1,agent_next_ci[0],agent_next_ci[1]] = 1

        other_agent_ci = np.argwhere(scene[2,:,:] == 1)[0]
        if(np.equal(agent_next_ci, other_agent_ci).all()):
            agent_reward = ml.rl.Reward(value=-1.0)
            agent_next_state = ml.rl.State(kind=ml.rl.StateKind.TERMINAL, value=scene)
        else:
            agent_reward = ml.rl.Reward(value=+1.0)
            agent_next_state = ml.rl.State(kind=ml.rl.StateKind.NON_TERMINAL, value=scene)
              
        return (agent_reward, agent_next_state)
        