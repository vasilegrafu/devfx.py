import matplotlib as mpl
import numpy as np
import devfx.exceptions as ex
from .figure import Figure as Figure
from .chart import Chart
from .chart_factory import ChartFactory

class ChartPolar(Chart):
    def __init__(self, 
                 figure=None, fig_size=None,
                 position=None,
                 title=None, 
                 grid=None,
                 rmin=None, rmax=None,
                 xlabel=None, ylabel=None):
        if(figure is None):
            if(fig_size is None):
                figure = Figure()
            else:
                figure = Figure(size=fig_size)

        if(position is None):
            axes = ChartFactory.new_chartPolar(figure=figure)
        else:
            axes = ChartFactory.new_chartPolar(figure=figure, position=position)

        super().__init__(figure, axes, title, grid)

        self.set_rmin(rmin)
        self.set_rmax(rmax)

        if(xlabel is not None):
            self.set_xlabel(xlabel)

        if(ylabel is not None):
            self.set_ylabel(ylabel)

    """------------------------------------------------------------------------------------------------
    """
    def get_rmin(self):
        return self.__rmin

    def rmin(self):
        return self.get_rmin()

    def set_rmin(self, rmin):
        self.__rmin = rmin

    """------------------------------------------------------------------------------------------------
    """ 
    def get_rmax(self):
        return self.__rmax

    def rmax(self):
        return self.get_rmax()

    def set_rmax(self, rmax):
        self.__rmax = rmax

    """------------------------------------------------------------------------------------------------
    """ 
    def get_xlabel(self):
        return self.axes.get_xlabel()

    def xlabel(self):
        return self.get_xlabel()

    def set_xlabel(self, *args, **kwargs):
        self.axes.set_xlabel(*args, **kwargs)

    """------------------------------------------------------------------------------------------------
    """ 
    def get_ylabel(self):
        return self.axes.get_ylabel()

    def ylabel(self):
        return self.get_ylabel()

    def set_ylabel(self, *args, **kwargs):
        self.axes.set_ylabel(*args, **kwargs)

    """------------------------------------------------------------------------------------------------
    """
    def __do_prior_draw(self):
        pass

    def __do_post_draw(self):
        if(self.rmin() is not None):
            self.axes.set_rmin(self.get_rmin())
        if(self.rmax() is not None):
            self.axes.set_rmax(self.get_rmax())

    def plot(self, *args, **kwargs):
        self.__do_prior_draw()
        result = self.axes.plot(*args, **kwargs)
        self.__do_post_draw()
        return result

