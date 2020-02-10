import time as t
import devfx.core as core
from devfx_samples.machine_learning.rl.grid.logic.grid_environment import GridEnvironment
from devfx_samples.machine_learning.rl.grid.logic.grid_agent import GridAgent
from devfx_samples.machine_learning.rl.grid.logic.grid_cell_state_kind import GridCellStateKind
from devfx_samples.machine_learning.rl.grid.logic.grid_cell_state import GridCellState

"""------------------------------------------------------------------------------------------------
"""
def main():
    environment = GridEnvironment()
    def on_training_info_update(source, event_args):
            print(event_args.message)

    def on_training_progress(source, event_args):
        pass
       
    agent = environment.create_agent(agent_type=GridAgent, name='agent1')
    agent.training_info_update += core.SignalHandler(on_training_info_update)
    agent.training_progress += core.SignalHandler(on_training_progress)

    while(True):
        actions = environment.get_actions(GridCellState((1,2)))
        
        agents = environment.get_agents()



        for agent in agents:
            agent.train(episodes=1, epsilon=0.25)
            t.sleep(0.5)

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()