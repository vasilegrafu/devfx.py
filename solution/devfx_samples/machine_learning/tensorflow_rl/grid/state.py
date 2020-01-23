import devfx.machine_learning.tensorflow as ml

"""========================================================================================================
"""
class GridCellKind(ml.rl.StateKind):
    BLOCKED = 'BLOCKED'

"""========================================================================================================
"""
class GridCell(ml.rl.State):
    def __init__(self, value, state_kind=GridCellKind.NON_TERMINAL, reward=0.0):
        super().__init__(value=value, state_kind=state_kind, reward=reward)

    def __str__(self):
        return str(super().value)