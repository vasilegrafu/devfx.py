from ..matplotlib.persistent_figure import PersistentFigure as matplotlib_PersistentFigure

class PersistentFigure(matplotlib_PersistentFigure):
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
        return super().__new__(cls, id,
                                    size=size, dpi=dpi,
                                    facecolor=facecolor,
                                    linewidth=linewidth, edgecolor=edgecolor, frameon=frameon,
                                    chart_fns=chart_fns,
                                    show=show,
                                    block=block,
                                    clear=clear,
                                    clear_data=clear_data,
                                    empty=empty)
