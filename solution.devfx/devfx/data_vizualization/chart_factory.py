import matplotlib
import matplotlib.gridspec
import devfx.core as core

class ChartFactory(object):
    """------------------------------------------------------------------------------------------------
    """ 
    @classmethod
    def new_chart2d(cls, figure, position=None):
        if(position is None):
            position=(1, 1, 1)
            return figure.add_subplot(*position)
        elif(core.is_typeof(position, matplotlib.gridspec.SubplotSpec)):
            return figure.add_subplot(position)
        elif(core.is_typeof(position, int)):
            return figure.add_subplot(position)
        else:
            if(len(position) == 3 and all([not core.is_iterable(_) for _ in position])):
                return figure.add_subplot(*position)
            if(len(position) == 3 and all([core.is_iterable(_) for _ in position])):
                return figure.add_subplot(matplotlib.gridspec.GridSpec(position[0][0], position[0][1]).new_subplotspec(position[1], rowspan = position[2][0], colspan = position[2][1]))

    """------------------------------------------------------------------------------------------------
    """    
    @classmethod     
    def new_chart3d(cls, figure, position=None):
        if(position is None):
            position=(1, 1, 1)
            return figure.add_subplot(*position, projection='3d')
        elif(core.is_typeof(position, matplotlib.gridspec.SubplotSpec)):
            return figure.add_subplot(position, projection='3d')
        elif(core.is_typeof(position, int)):
            return figure.add_subplot(position, projection='3d')
        else:
            if(len(position) == 3 and all([not core.is_iterable(_) for _ in position])):
                return figure.add_subplot(*position, projection='3d')
            if(len(position) == 3 and all([core.is_iterable(_) for _ in position])):
                return figure.add_subplot(matplotlib.gridspec.GridSpec(position[0][0], position[0][1]).new_subplotspec(position[1], rowspan = position[2][0], colspan = position[2][1]), projection='3d')

    """------------------------------------------------------------------------------------------------
    """ 
    @classmethod        
    def new_chartPolar(cls, figure, position=None):
        if(position is None):
            position=(1, 1, 1)
            return figure.add_subplot(*position, projection='polar')
        elif(core.is_typeof(position, matplotlib.gridspec.SubplotSpec)):
            return figure.add_subplot(position, projection='polar')
        elif(core.is_typeof(position, int)):
            return figure.add_subplot(position)
        else:
            if(len(position) == 3 and all([not core.is_iterable(_) for _ in position])):
                return figure.add_subplot(*position, projection='polar')
            if(len(position) == 3 and all([core.is_iterable(_) for _ in position])):
                return figure.add_subplot(matplotlib.gridspec.GridSpec(position[0][0], position[0][1]).new_subplotspec(position[1], rowspan = position[2][0], colspan = position[2][1]), projection='polar')

    """------------------------------------------------------------------------------------------------
    """
    def clear_chart(self, chart):
        chart.axes.clear()

    def clear_charts(self, figure):
        for axes in figure.get_axes():
            axes.clear()

    def remove_chart(self, chart):
        chart.axes.remove()

    def remove_charts(self, figure):
        for axes in figure.get_axes():
            axes.remove()

