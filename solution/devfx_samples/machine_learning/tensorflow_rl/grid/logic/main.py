import numpy as np
import time as t
import devfx.core as core
import devfx.machine_learning.tensorflow as ml
from devfx_samples.machine_learning.tensorflow_rl.grid.logic.grid_environment import GridEnvironment
from devfx_samples.machine_learning.tensorflow_rl.grid.logic.grid_agent import GridAgent

"""------------------------------------------------------------------------------------------------
"""
def main():
    environment = GridEnvironment()
    def process_training_message(source, event_args):
            print(event_args.message)

    def process_training_progress(source, event_args):
        print(event_args.message)
        
    agent = environment.create_agent(agent_type=GridAgent, name='Predator')
    agent.training_message_events += core.EventHandler(process_training_message)
    agent.training_progress_events += core.EventHandler(process_training_progress)

    while(True):
        agents = environment.get_agents()
        for agent in agents:
            agent.train(episodes=1, discount_factor=0.9, learning_rate=0.25, event_fn=agent_training_event)
            t.sleep(0.5)

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()