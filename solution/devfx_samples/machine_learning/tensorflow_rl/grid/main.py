import time as t
import devfx.statistics as stats
import devfx.machine_learning.tensorflow as ml
import devfx.data_vizualization.seaborn as dv
from devfx_samples.machine_learning.tensorflow_rl.grid.environment import GridEnvironment
from devfx_samples.machine_learning.tensorflow_rl.grid.agent import GridAgent

"""------------------------------------------------------------------------------------------------
"""
def main():
    environment = GridEnvironment()
    agent = GridAgent(environment=environment)

    while(True):
        agent.set_state(state=environment.get_random_non_terminal_state())
        print('start state:', agent.get_state())
        i = 0
        while(environment.is_non_terminal_state(agent.get_state())):
            i += 1
            agent.do_random_action()
            print(i, agent.get_state())
            if(i >= 100):
                break
        t.sleep(0.5)

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()