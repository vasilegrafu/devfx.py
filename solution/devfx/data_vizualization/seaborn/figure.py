from ..matplotlib.figure import Figure as matplotlib_Figure

class Figure(matplotlib_Figure):
    def __init__(self, size=(8, 4), dpi=None,
                       grid=(1, 1),
                       facecolor=None,
                       linewidth=0.0, edgecolor=None, frameon=True):
        super().__init__(size=size, dpi=dpi,
                         grid=grid,
                         facecolor=facecolor,
                         linewidth=linewidth, edgecolor=edgecolor, frameon=frameon)

