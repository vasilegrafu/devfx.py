from ..matplotlib.chart2d import Chart2d as matplotlib_Chart2d

class Chart2d(matplotlib_Chart2d):
    def __init__(self,
                 figure=None, fig_size=None,
                 position=None,
                 title=None,
                 grid=None,
                 xlim=None, xmin=None, xmax=None, ylim=None, ymin=None, ymax=None,
                 xlabel=None, ylabel=None):
        super().__init__(figure=figure, fig_size=fig_size,
                         position=position,
                         title=title,
                         grid=grid,
                         xlim=xlim, xmin=xmin, xmax=xmax, ylim=ylim, ymin=ymin, ymax=ymax,
                         xlabel=xlabel, ylabel=ylabel)


