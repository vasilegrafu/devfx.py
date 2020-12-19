import numpy as np
import devfx.exceptions as excs
import devfx.machine_learning as ml

"""========================================================================================================
"""
class GridAgent(ml.rl.Agent):
    def __init__(self, id, name, kind, environment, policy, iteration_randomness):
        super().__init__(id=id, name=name, kind=kind, environment=environment, iteration_randomness=iteration_randomness)
        super().set_state(None)
        super().set_policy(policy)




        