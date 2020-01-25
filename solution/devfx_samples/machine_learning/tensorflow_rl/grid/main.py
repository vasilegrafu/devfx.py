import time as t
from devfx_samples.machine_learning.tensorflow_rl.grid.environment import GridEnvironment
from devfx_samples.machine_learning.tensorflow_rl.grid.qlearning_action_policy import GridQLearningActionPolicy

"""------------------------------------------------------------------------------------------------
"""
def main():
    environment = GridEnvironment()
    environment.create_agent(name='Predator', state=environment.get_random_non_terminal_state(), action_policy=GridQLearningActionPolicy())

    while(True):
        agents = environment.get_agents()
        for agent in agents:
            agent.set_state(state=environment.get_random_non_terminal_state())
            print(f'agent: \'{agent.get_name()}\', start state: {agent.get_state()}')
            i = 0
            while(agent.get_state().is_non_terminal()):
                i += 1
                (state, action, next_state) = agent.do_random_action()
                agent.get_action_policy().update(state=state, action=action, next_state=next_state, next_state_reward=next_state.reward)
                print(i, agent.get_state())
            t.sleep(0.5)

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()