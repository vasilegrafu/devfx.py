import devfx.machine_learning as ml

"""========================================================================================================
"""
class GridActions(object):
    Left = ml.rl.Action('Left', 1)
    Right = ml.rl.Action('Right', 1)
    Up = ml.rl.Action('Up', 1)
    Down = ml.rl.Action('Down', 1)
