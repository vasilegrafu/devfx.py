import matplotlib as mpl
import matplotlib.gridspec

class FigureGrid(mpl.gridspec.GridSpec):
    def __init__(self, nrows, ncols,
                 left=None, bottom=None, right=None, top=None,
                 wspace=None, hspace=None,
                 width_ratios=None, height_ratios=None):
        super().__init__(nrows=nrows, ncols=ncols,
                         left=left, bottom=bottom, right=right, top=top,
                         wspace=wspace, hspace=hspace,
                         width_ratios=width_ratios, height_ratios=height_ratios)