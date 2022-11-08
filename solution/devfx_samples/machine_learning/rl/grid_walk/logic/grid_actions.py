import numpy as np
import devfx.exceptions as excps
import devfx.machine_learning as ml


"""========================================================================================================
"""
class GridAgentMoveActions(ml.rl.DiscreteActions):
    def __init__(self):
        super().__init__(name='Move', values=['Left', 'Right', 'Up', 'Down'])


    
