import time as t
from devfx_samples.machine_learning.tensorflow_rl.grid.environment import GridEnvironment
from devfx_samples.machine_learning.tensorflow_rl.grid.agent import GridAgent

"""------------------------------------------------------------------------------------------------
"""
def main():
    environment = GridEnvironment()
    agent = GridAgent()
    agent.set_action_policy(action_policy=Ran(end))
    agent.set_state(state=environment.get_random_non_terminal_state())
    environment.add_agent(agent)

    while(True):
        agent.set_state(state=environment.get_random_non_terminal_state())
        print('start state:', agent.get_state())
        i = 0
        while(agent.get_state().is_non_terminal()):
            i += 1
            agent.do_action()
            print(i, agent.get_state())
            if(i >= 100):
                break
        t.sleep(0.5)

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()