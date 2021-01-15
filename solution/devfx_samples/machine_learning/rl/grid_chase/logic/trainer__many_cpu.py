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

    def train(self):
        while(True):
            self.iteration += 1
            self.grid_environment.do_iteration()

    def get_iteration(self):
        return self.iteration

    def get_policy(self, agent_kind):
        agent_kind_policy = self.grid_environment.get_agent_kind_policy(agent_kind=agent_kind)
        agent_kind_policy = agent_kind_policy.copy()
        return agent_kind_policy

class TrainingManager(object):
    def __init__(self):
        N = 4
        self.remote_trainers = [ppd.remote(Trainer).options(max_concurrency=2).instance() for _ in range(0, N)]
        for remote_trainer in self.remote_trainers:
            remote_trainer.train()

    def learn(self, agent_kind_policies):
        for agent_kind in agent_kind_policies:
            policies = ppd.get_results([remote_trainer.get_policy(agent_kind) for remote_trainer in self.remote_trainers])
            agent_kind_policies[agent_kind].set_policies(policies)
        iterations = ppd.get_results([remote_trainer.get_iteration() for remote_trainer in self.remote_trainers])
        return sum(iterations)