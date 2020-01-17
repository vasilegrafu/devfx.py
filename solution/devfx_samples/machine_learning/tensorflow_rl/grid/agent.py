import numpy as np
import devfx.statistics as stats
import devfx.machine_learning.tensorflow as ml

class GridAgent(ml.rl.Agent):
    def __init__(self, environment, state=None):
        super().__init__(environment=environment, state=state)

