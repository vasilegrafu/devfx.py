import numpy as np
import devfx.machine_learning as ml
from .grid_agent_kind import GridAgentKind

class GridChaserAgent(ml.rl.Agent):
    def __init__(self, id, name, policy):
        super().__init__(id=id, name=name, kind=GridAgentKind.CHASER, policy=policy)



        