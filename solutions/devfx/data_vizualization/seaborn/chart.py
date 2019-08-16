import seaborn as sb
sb.set_style('darkgrid')

from ..matplotlib.chart import Chart as matplotlib_Chart

class Chart(matplotlib_Chart):
    def __init__(self, figure=None, axes=None, title=None, grid=None):
        super().__init__(figure=figure, axes=axes, title=title, grid=grid)
