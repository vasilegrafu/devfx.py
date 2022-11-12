import numpy as np
import devfx.exceptions as excps
import devfx.machine_learning as ml


"""========================================================================================================
"""
    
class GridAgentActionGenerator(ml.rl.ActionGenerator):
    def __init__(self):
        super().__init__(ranges=[ml.rl.DiscreteRange('Move', value=[np.array([ 0,-1]),      #Left     (row: 0, col:-1)
                                                                    np.array([ 0,+1]),      #Right    (row: 0, col:+1)
                                                                    np.array([-1, 0]),      #Up       (row:-1, col: 0)   
                                                                    np.array([+1, 0])])     #Down     (row:+1, col: 0) 
                                ])

