import numpy as np
import devfx.core as core
import devfx.machine_learning as ml

"""========================================================================================================
"""
class GridAgent(ml.rl.Agent):
    def __init__(self, name, environment):
        state = environment.get_random_non_terminal_state()
        policy=ml.rl.QPolicy(discount_factor=0.9, learning_rate=0.25)
        super().__init__(name=name, environment=environment, state=state, policy=policy)

