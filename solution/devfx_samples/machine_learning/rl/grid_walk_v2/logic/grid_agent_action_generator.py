import numpy as np
import devfx.exceptions as excps
import devfx.machine_learning as ml


"""========================================================================================================
"""
    
class GridAgentActionGenerator(ml.rl.ActionGenerator):
    def __init__(self):
        super().__init__(ranges=[ml.rl.DiscreteRange('MOVE', value=[('LEFT',    [ 0,-1]),      #Left     (row: 0, col:-1)
                                                                    ('RIGHT',   [ 0,+1]),      #Right    (row: 0, col:+1)
                                                                    ('UP',      [-1, 0]),      #Up       (row:-1, col: 0)   
                                                                    ('DOWN',    [+1, 0])])     #Down     (row:+1, col: 0) 
                                ])

    def _get_random(self):
        return ml.rl.Action(*self.ranges[0].get_random())