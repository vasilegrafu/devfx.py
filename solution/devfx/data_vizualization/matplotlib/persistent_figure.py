import devfx.exceptions as exceps
from .figure import Figure

class PersistentFigure(object):
    __persister_dict__ = {}

    @staticmethod
    def __new__(cls, id,
                     size=(8, 4), dpi=None,
                     facecolor=None,
                     linewidth=0.0, edgecolor=None, frameon=True,
                     chart_fns=None,
                     show=True,
                     block=False,
                     clear=True,
                     clear_data=False,
                     empty=False):
        def construct():
            figure = Figure(size=size, dpi=dpi,
                            facecolor=facecolor,
                            linewidth=linewidth, edgecolor=edgecolor, frameon=frameon)
            charts = []
            if(chart_fns is not None):
                for chart_fn in chart_fns:
                    charts.append(chart_fn(figure))

            if (show):
                figure.show(block=block)

            if(len(charts) == 0):
                return figure
            else:
                return (figure, *charts)

        if(id not in PersistentFigure.__persister_dict__):
            (figure, *charts) = construct()
            PersistentFigure.__persister_dict__[id] = (figure, *charts)
        else:
            (figure, *charts) = PersistentFigure.__persister_dict__[id]
            if(clear):
                figure.clear()
            if (clear_data):
                figure.clear_data()
            if (empty):
                figure.empty()

        if(len(charts) == 0):
            raise exceps.NotSupportedError()
        elif(len(charts) == 1):
            return (figure, charts[0])
        else:
            return (figure, *tuple(charts))



