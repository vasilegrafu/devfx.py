import numpy as np
import devfx.exceptions as excps
import devfx.machine_learning as ml


"""========================================================================================================
"""
    
class GridAgentActionValuesGenerator(ml.rl.DiscreteActionValuesGenerator):
    def __init__(self):
        super().__init__(name='Move', values=((-1, 0),      #Left     (x-axis:-1, y-axis: 0)
                                              ( 0,+1),      #Right    (x-axis:+1, y-axis: 0)
                                              (+1, 0),      #Up       (x-axis: 0, y-axis:+1)   
                                              ( 0,+1)))     #Down     (x-axis: 0, y-axis:-1) 