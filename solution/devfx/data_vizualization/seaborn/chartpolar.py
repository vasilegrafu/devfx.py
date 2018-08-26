from ..matplotlib.chartpolar import ChartPolar as matplotlib_ChartPolar

class ChartPolar(matplotlib_ChartPolar):
    def __init__(self,
                 figure=None, fig_size=None,
                 position=None,
                 title=None,
                 grid=None,
                 rmin=None, rmax=None,
                 xlabel=None, ylabel=None):
        super().__init__(figure=figure, fig_size=fig_size,
                         position=position,
                         title=title,
                         grid=grid,
                         rmin=rmin, rmax=rmax,
                         xlabel=xlabel, ylabel=ylabel)
