import numpy as np
import random as rnd
import devfx.machine_learning as ml

from .grid_agent_kind import GridAgentKind

class GridAgent(ml.rl.Agent):
    def __init__(self, id, name, policy):
        super().__init__(id=id, name=name, kind=GridAgentKind.WALKER, policy=policy)



