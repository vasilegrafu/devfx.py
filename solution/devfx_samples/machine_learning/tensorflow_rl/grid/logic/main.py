import time as t
from devfx_samples.machine_learning.tensorflow_rl.grid.logic.grid_environment import GridEnvironment
from devfx_samples.machine_learning.tensorflow_rl.grid.logic.grid_agent import GridAgent

"""------------------------------------------------------------------------------------------------
"""
def main():
    environment = GridEnvironment()
    def on_training_info_update(source, event_args):
            print(event_args.message)

    def on_training_progress(source, event_args):
        pass
        
    agent = environment.create_agent(agent_type=GridAgent, name='Predator')
    agent.training_info_update += core.SignalHandler(on_training_info_update)
    agent.training_progress += core.SignalHandler(on_training_progress)

    while(True):
        agents = environment.get_agents()
        for agent in agents:
            agent.train(episodes=1, discount_factor=0.9, learning_rate=0.25)
            t.sleep(0.5)

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()