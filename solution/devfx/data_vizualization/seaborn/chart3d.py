from ..matplotlib.chart3d import Chart3d as matplotlib_Chart3d

class Chart3d(matplotlib_Chart3d):
    def __init__(self,
                 figure=None, fig_size=None,
                 position=None,
                 title=None,
                 grid=None,
                 xlim=None, xmin=None, xmax=None, ylim=None, ymin=None, ymax=None, zlim=None, zmin=None, zmax=None,
                 xlabel=None, ylabel=None, zlabel=None):
        super().__init__(figure=figure, fig_size=fig_size,
                         position=position,
                         title=title,
                         grid=grid,
                         xlim=xlim, xmin=xmin, xmax=xmax, ylim=ylim, ymin=ymin, ymax=ymax, zlim=zlim, zmin=zmin, zmax=zmax,
                         xlabel=xlabel, ylabel=ylabel, zlabel=zlabel)




