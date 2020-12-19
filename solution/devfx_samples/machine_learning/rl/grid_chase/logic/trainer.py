import os
import itertools
import time
import ray
import devfx.exceptions as excs
import devfx.core as core
import devfx.diagnostics as dgn
import devfx.machine_learning as ml
import devfx.processing as processing

from .grid_agent_kind import GridAgentKind
from .grid_environment import GridEnvironment

if(not ray.is_initialized()):
    ray.init()

class Trainer(object):
    def __init__(self):
        self.grid_environment = GridEnvironment()
        self.grid_environment.create()
        self.grid_environment.setup(iteration_randomness=1.0)

    def train(self, agent_kind, d):
        i = 0
        while(i <= d):
            i += 1
            self.grid_environment.do_iteration()
        agent_kind_policy = self.grid_environment.get_agent_kind_policy(agent_kind=agent_kind)
        return (d, agent_kind_policy)
RemoteTrainer = ray.remote(Trainer)

class TrainingManager(object):
    def __init__(self):
        N = 1
        self.remote_trainers = []
        for i in range(0, N):
            remote_trainer = RemoteTrainer.remote()
            self.remote_trainers.append(remote_trainer)

    def learn(self, agent_kind_policies):
        d = 10000
        D = 0
        for agent_kind in agent_kind_policies:
            remote_trainer = self.remote_trainers[0]
            x = remote_trainer.train.remote(agent_kind, d)

            train_result_refs =  [remote_trainer.train.remote(agent_kind, d) for remote_trainer in self.remote_trainers]
            train_results = ray.get(train_result_refs)
            D += sum([d for (d, agent_kind_policy) in train_results])
            agent_kind_policies[agent_kind].assign_from(policies=[agent_kind_policy for (i, agent_kind_policy) in train_results])
        return D

    def close(self):
        self.processes.terminate()
        for channel in self.channels:
            channel.close()




