import os
import itertools
import time
import ray
ray.init(ignore_reinit_error=True)
import devfx.exceptions as excs
import devfx.core as core
import devfx.diagnostics as dgn
import devfx.machine_learning as ml
import devfx.processing as processing

from .grid_agent_kind import GridAgentKind
from .grid_environment import GridEnvironment

class Trainer(object):
    def __init__(self):
        self.grid_environment = GridEnvironment()
        self.grid_environment.create()
        self.grid_environment.setup(iteration_randomness=1.0)

    def train(self, agent_kind, n):
        i = 0
        while(i <= n):
            i += 1
            self.grid_environment.do_iteration()
        agent_kind_policy = self.grid_environment.get_agent_kind_policy(agent_kind=agent_kind)
        return (n, agent_kind_policy)
                
class TrainingManager(object):
    def __init__(self):
        RemoteTrainer = ray.remote(Trainer)
        n = 4
        self.remote_trainers = []
        for i in range(0, n):
            self.remote_trainers.append(RemoteTrainer.remote())

    def learn(self, agent_kind_policies):
        d = 0
        for agent_kind in agent_kind_policies:
            train_result_refs =  [remote_trainer.train.remote(agent_kind, 1000) for remote_trainer in self.remote_trainers]
            train_results = ray.get(train_result_refs)
            d = sum([i for (i, agent_kind_policy) in train_results])
            agent_kind_policies[agent_kind].assign_from(policies=[agent_kind_policy for (i, agent_kind_policy) in train_results])
        return d

    def close(self):
        self.processes.terminate()
        for channel in self.channels:
            channel.close()


# class TrainingManager(object):
#     def __init__(self):
#         self.grid_environment = GridEnvironment()
#         self.grid_environment.create()
#         self.grid_environment.setup(iteration_randomness=1.0)

#     def learn(self, agent_kind_policies):
#         d = 1000
#         i = 0
#         while True:
#             i += 1
#             self.grid_environment.do_iteration()
#             if(i % d == 0):
#                 for agent_kind in agent_kind_policies:
#                     agent_kind_policies[agent_kind].assign_from(policies=[self.grid_environment.get_agent_kind_policy(agent_kind=agent_kind)])
#                 break
#         return d

#     def close(self):
#         pass





