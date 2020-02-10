import time as t
import devfx.core as core
import devfx.machine_learning as ml
from devfx_samples.machine_learning.rl.grid.logic.environment import Environment

"""------------------------------------------------------------------------------------------------
"""
def main():
    environment = Environment()

    def on_training_info_update(source, event_args):
            print(event_args.message)

    def on_training_progress(source, event_args):
        pass
    
    agent = environment.create_agent(name='agent1',
                                     state=environment.get_random_non_terminal_state(),
                                     policy=ml.rl.QPolicy(discount_factor=0.9, learning_rate=0.25))
    agent.training_info_update += core.SignalHandler(on_training_info_update)
    agent.training_progress += core.SignalHandler(on_training_progress)

    while(True):       
        agents = environment.get_agents()
        for agent in agents:
            agent.train(episodes=1, epsilon=0.25)
            t.sleep(0.5)

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()