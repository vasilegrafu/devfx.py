import numpy as np
import time as t
import devfx.machine_learning.tensorflow as ml
from devfx_samples.machine_learning.tensorflow_rl.grid.environment import GridEnvironment

"""------------------------------------------------------------------------------------------------
"""
def main():
    environment = GridEnvironment()
    environment.create_agent(name='Predator', state=environment.get_random_non_terminal_state(), action_policy=ml.rl.QLearningActionPolicy())

    while(True):
        agents = environment.get_agents()
        for agent in agents:
            agent.set_state(state=environment.get_random_non_terminal_state())
            print(f'Agent: \'{agent.get_name()}\'. Start state: {agent.get_state()}.')
            i = 0
            while(agent.get_state().is_non_terminal()):
                i += 1
                action = agent.get_action_policy().get_action(state=agent.get_state())
                if(action is None):
                    (state, action, next_state) = agent.do_random_action()
                else:
                    rv = np.random.uniform(low=0.0, high=1.0, size=1)
                    if(rv <= 0.1):
                        (state, action, next_state) = agent.do_random_action()
                    else:
                        (state, action, next_state) = agent.do_action()
                agent.get_action_policy().update(state=state, action=action, next_state=next_state, alpha=0.1, gamma=0.9)
                print(i, agent.get_state())
            t.sleep(0.5)

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()