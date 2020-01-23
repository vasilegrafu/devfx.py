import numpy as np
import devfx.exceptions as exps
import devfx.machine_learning.tensorflow as ml

class GridLearningActionPolicy(ml.rl.LearningActionPolicy):
    def __init__(self, environment):
        super().__init__(environment=environment)

    """------------------------------------------------------------------------------------------------
    """ 
    def _get_action(self, state):
        raise exps.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """ 
    def _update(self, state, action, reward):
        raise exps.NotImplementedError()
