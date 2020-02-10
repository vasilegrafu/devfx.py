import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import devfx.exceptions as exps
from .figure import Figure as Figure
from .chart import Chart

class Chart3d(Chart):
    def __init__(self, 
                 figure=None, fig_size=None,
                 position=None,
                 title=None, 
                 grid=None,
                 xlim=None, xmin=None, xmax=None, ylim=None, ymin=None, ymax=None, zlim=None, zmin=None, zmax=None,
                 xlabel=None, ylabel=None, zlabel=None):
        if(figure is None):
            if(fig_size is None):
                figure = Figure()
            else:
                figure = Figure(size=fig_size)
                      
        if(position is None):
            axes = figure.new_chart3d()
        else:
            axes = figure.new_chart3d(position)

        super().__init__(figure, axes, title, grid)

        if ((xmin is not None) or (xmax is not None)):
            xlim = [xmin, xmax]
        self.set_xlim(xlim)

        if ((ymin is not None) or (ymax is not None)):
            ylim = [ymin, ymax]
        self.set_ylim(ylim)

        if ((zmin is not None) or (zmax is not None)):
            zlim = [zmin, zmax]
        self.set_zlim(zlim)

        if(xlabel is not None):
            self.set_xlabel(xlabel)
            
        if(ylabel is not None):
            self.set_ylabel(ylabel)
            
        if(zlabel is not None):
            self.set_zlabel(zlabel)

    """------------------------------------------------------------------------------------------------
    """
    def get_xlim(self):
        return self.__xlim

    def xlim(self):
        return self.get_xlim()

    def set_xlim(self, xlim):
        self.__xlim = xlim

    """------------------------------------------------------------------------------------------------
    """
    def get_ylim(self):
        return self.__ylim

    def ylim(self):
        return self.get_ylim()

    def set_ylim(self, ylim):
        self.__ylim = ylim
              
    """------------------------------------------------------------------------------------------------
    """ 
    def get_zlim(self):
        return self.__zlim

    def zlim(self):
        return self.get_zlim()

    def set_zlim(self, zlim):
        self.__zlim = zlim
        
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
    def get_zlabel(self):
        return self.axes.get_zlabel()
             
    def zlabel(self):
        return self.get_zlabel()
        
    def set_zlabel(self, *args, **kwargs):
        self.axes.set_zlabel(*args, **kwargs)


    """------------------------------------------------------------------------------------------------
    """
    def __do_prior_draw(self):
        pass

    def __do_post_draw(self):
        if(self.xlim() is not None):
            self.axes.set_xlim(self.get_xlim())
        if(self.ylim() is not None):
            self.axes.set_ylim(self.get_ylim())
        if (self.zlim() is not None):
            self.axes.set_zlim(self.get_zlim())

        for _ in self.axes.get_xticklabels():
            _.set_rotation(0)
            _.set_fontsize('medium')
        for _ in self.axes.get_yticklabels():
            _.set_rotation(0)
            _.set_fontsize('medium')
        for _ in self.axes.get_zticklabels():
            _.set_rotation(0)
            _.set_fontsize('medium')

    def plot(self, *args, **kwargs):
        self.__do_prior_draw()
        result = self.axes.plot(*args, **kwargs)
        self.__do_post_draw()
        return result
        
    def scatter(self, *args, **kwargs):
        self.__do_prior_draw()
        result = self.axes.scatter(*args, marker = kwargs.pop('marker', '.'), **kwargs)
        self.__do_post_draw()
        return result

    def wireframe(self, *args, **kwargs):
        self.__do_prior_draw()
        result = self.axes.plot_wireframe(*args, **kwargs)
        self.__do_post_draw()
        return result

    def surface(self, *args, **kwargs):
        self.__do_prior_draw()
        result = self.axes.plot_surface(*args, **kwargs)
        self.__do_post_draw()
        return result

