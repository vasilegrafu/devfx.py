import matplotlib
import matplotlib.figure
import matplotlib.gridspec
import matplotlib.pyplot

class Figure(object):


    """------------------------------------------------------------------------------------------------
    """
    def __init__(self, size=(8, 4), dpi=None,
                       grid=(1, 1),
                       facecolor=None,
                       linewidth=0.0, edgecolor=None, frameon=True):
        self.__figure = matplotlib.pyplot.figure(figsize=size, dpi=dpi,
                                                 facecolor=facecolor,
                                                 linewidth=linewidth, edgecolor=edgecolor, frameon=frameon)
        if(grid is None):
            self.__grid = None
        else:
            self.__grid = matplotlib.gridspec.GridSpec(*grid)

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
    def show(self, block=True):
        matplotlib.pyplot.figure(self.__figure.number)
        matplotlib.pyplot.tight_layout(pad=0.25)
        matplotlib.pyplot.show(block=block)
        matplotlib.pyplot.pause(0.001)

    def clear(self, chart=None):
        matplotlib.pyplot.figure(self.__figure.number)
        matplotlib.pyplot.clf()

    def close(self):
        matplotlib.pyplot.figure(self.__figure.number)
        matplotlib.pyplot.close()
