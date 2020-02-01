import numpy as np
import time as t
import devfx.machine_learning.tensorflow as ml
from devfx_samples.machine_learning.tensorflow_rl.grid.logic.grid_environment import GridEnvironment

class Trainer(object):
    def __init__(self):
        self.environment = GridEnvironment()
        self.environment.create_agent(name='agent1', state=self.environment.get_random_non_terminal_state())

    def train(self, callback_on_new_state=None):
        agents = self.environment.get_agents()
        for agent in agents:
            agent.set_state(state=self.environment.get_random_non_terminal_state())
            while(agent.get_state().is_non_terminal()):
                action = agent.get_action_policy().get_action(state=agent.get_state())
                if(action is None):
                    (state, action, next_state) = agent.do_random_action()
                else:
                    rv = np.random.uniform(low=0.0, high=1.0, size=1)
                    if(rv <= 0.1):
                        (state, action, next_state) = agent.do_random_action()
                    else:
                        (state, action, next_state) = agent.do_action()
                agent.get_action_policy().update(state=state, action=action, next_state=next_state, alpha=0.25, gamma=0.9)

                if(callback_on_new_state is not None):
                    callback_on_new_state()
            

