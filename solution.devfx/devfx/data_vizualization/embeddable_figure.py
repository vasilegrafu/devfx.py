import matplotlib
import matplotlib.figure
import matplotlib.gridspec

class EmbeddableFigure(object):
    """------------------------------------------------------------------------------------------------
    """
    def __init__(self, size=(8, 4), dpi=None,
                       grid=(1, 1),
                       facecolor=None,
                       linewidth=0.0, edgecolor=None, frameon=True,
                       layout=None):
        self.__figure = matplotlib.figure.Figure(figsize=size, dpi=dpi,
                                                 facecolor=facecolor,
                                                 linewidth=linewidth, edgecolor=edgecolor, frameon=frameon,
                                                 layout=layout)
        if(grid is None):
            self.__grid = None
        else:
            self.__grid = matplotlib.gridspec.GridSpec(*grid)

    """----------------------------------------------------------------
    """
    @property
    def self(self):
        return self.__figure

    """----------------------------------------------------------------
    """
    @property
    def grid(self):
        return self.__grid

    """----------------------------------------------------------------
    """
    def add_subplot(self, *args, **kwargs):
        return self.__figure.add_subplot(*args, **kwargs)

    """------------------------------------------------------------------------------------------------
    """
    def clear(self, chart=None):
        self.__figure.clear()


