import devfx.machine_learning as ml

"""========================================================================================================
"""
class GridAgentMovementActions(object):
    Left = ml.rl.Action('Left')
    Right = ml.rl.Action('Right')
    Up = ml.rl.Action('Up')
    Down = ml.rl.Action('Down')

class GridAgentHittingBallActions(object):
    Left = ml.rl.Action('Left')
    Right = ml.rl.Action('Right')
    Up = ml.rl.Action('Up')
    Down = ml.rl.Action('Down')
    