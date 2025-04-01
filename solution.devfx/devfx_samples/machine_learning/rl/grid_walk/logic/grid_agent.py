import numpy as np
import devfx.machine_learning as ml
from .grid_agent_action_ranges import GridAgentActionRanges

class GridAgent(ml.rl.Agent):
    def __init__(self, id, name, kind, policy):
        super().__init__(id=id, name=name, kind=kind, policy=policy)

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
        is_terminal_state = agent.is_in_terminal_state()
        if(is_terminal_state):
            return None
    
        scene = self.get_environment().get_scene()

        agent_ci = np.argwhere(scene[2,:,:] == 1)[0]
        agent_nci = agent_ci + action.get_value()

        if(scene[0,agent_nci[0],agent_nci[1]] == ml.rl.StateKind.UNDEFINED):
            agent_reward = ml.rl.Reward(value=scene[1,agent_nci[0],agent_nci[1]])
            agent_next_state = ml.rl.State(kind=ml.rl.StateKind.NON_TERMINAL, value=scene)
        else:
            scene[2,agent_ci[0],agent_ci[1]] = 0
            scene[2,agent_nci[0],agent_nci[1]] = 1
            agent_reward = ml.rl.Reward(value=scene[1,agent_nci[0],agent_nci[1]])
            agent_next_state = ml.rl.State(kind=scene[0,agent_nci[0],agent_nci[1]], value=scene)
        
        return (agent_reward, agent_next_state)

