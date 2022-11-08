import numpy as np
import devfx.exceptions as excps
import devfx.machine_learning as ml

"""========================================================================================================
"""
class GridAgent(ml.rl.Agent):
    def __init__(self, id, name, kind, environment, state, policy, iteration_randomness):
        super().__init__(id=id, name=name, kind=kind, environment=environment, state=state, policy=policy, iteration_randomness=iteration_randomness)




        