import numpy as np
import devfx.exceptions as ex
import devfx.machine_learning as ml

"""========================================================================================================
"""
class GridAgent(ml.rl.Agent):
    def __init__(self, id, name, kind, policy, environment, state, iteration_randomness):
        super().__init__(id=id, name=name, kind=kind, policy=policy, environment=environment, state=state, iteration_randomness=iteration_randomness)




        