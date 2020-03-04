import devfx.machine_learning as ml

"""========================================================================================================
"""
class GridActions(object):
    Left = ml.rl.Action('Left')
    Right = ml.rl.Action('Right')
    Up = ml.rl.Action('Up')
    Down = ml.rl.Action('Down')
    Stay = ml.rl.Action('Stay')
