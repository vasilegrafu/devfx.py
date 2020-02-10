import devfx.machine_learning as ml
from .grid_cell_state_kind import GridCellStateKind

"""========================================================================================================
"""
class GridCellState(ml.rl.State):
    def __init__(self, value, state_kind=GridCellStateKind.NON_TERMINAL, reward=0.0):
        super().__init__(value=value, state_kind=state_kind, reward=reward)
