import numpy as np
import devfx.exceptions as exps
import devfx.machine_learning.tensorflow as ml

class GridVLearningActionPolicy(ml.rl.VLearningActionPolicy):
    def __init__(self):
        super().__init__()

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_action(self, state):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def _update(self, state, reward):
        raise exps.NotImplementedError()
