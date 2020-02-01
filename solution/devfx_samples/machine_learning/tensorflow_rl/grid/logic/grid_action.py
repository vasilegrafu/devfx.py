import devfx.machine_learning.tensorflow as ml

"""========================================================================================================
"""
class GridAction(ml.rl.Action):
    def __init__(self, value):
        super().__init__(value=value)
