import random as rnd
import devfx.diagnostics as dgn
import devfx.processing.concurrent as pc
import devfx.processing.parallel.distributed as ppd

from .grid_agent_kind import GridAgentKind
from .grid_environment import GridEnvironment

class Trainer(object):
    def __init__(self):
        self.grid_environment = GridEnvironment()
        self.grid_environment.create()
        self.grid_environment.setup(iteration_randomness=1.0)
        self.iteration = 0

    def learn(self, agent_kind_policies):
        for agent_kind in agent_kind_policies:
            agent_kind_policies[agent_kind].set_policies(policies=[self.grid_environment.get_agent_kind_policy(agent_kind=agent_kind)])
        n = 1000
        self.grid_environment.do_iterations(n)
        self.iteration += n
        return self.iteration
    