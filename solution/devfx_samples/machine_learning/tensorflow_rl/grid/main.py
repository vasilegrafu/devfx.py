import devfx.statistics as stats
import devfx.machine_learning.tensorflow as ml
import devfx.data_vizualization.seaborn as dv
from devfx_samples.machine_learning.tensorflow_rl.grid.environment import GridEnvironment
from devfx_samples.machine_learning.tensorflow_rl.grid.agent import GridAgent

"""------------------------------------------------------------------------------------------------
"""
def main():
    environment = GridEnvironment()
    agent = GridAgent(environment=environment, state=(1, 1))

    is_non_terminal_state = environment.is_non_terminal_state(state=(2,4))

    i = 0
    while((i <= 1000) and environment.is_non_terminal_state(agent.get_state())):
        agent.do_random_action()
        print(i, agent.get_state())
        i += 1


"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()