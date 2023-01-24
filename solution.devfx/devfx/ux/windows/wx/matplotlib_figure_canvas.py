import matplotlib
matplotlib.use('WXAgg')
import matplotlib.backends.backend_wxagg

import wx
from . import layout
from . import events
from . import groups

class MatplotlibFigureCanvas(matplotlib.backends.backend_wxagg.FigureCanvasWxAgg, 
            layout.LayoutHandler,
            events.GenericEventHandler, 
            events.MouseEventHandler, 
            events.KeyboardEventHandler, 
            events.ApplicationEventHandler,
            groups.GroupHandler):
    def __init__(self, parent, id=wx.ID_ANY, figure=None):
        matplotlib.backends.backend_wxagg.FigureCanvasWxAgg.__init__(self, parent, id=id, figure=figure)
        layout.LayoutHandler.__init__(self)
        events.GenericEventHandler.__init__(self)
        events.MouseEventHandler.__init__(self)
        events.KeyboardEventHandler.__init__(self)
        events.ApplicationEventHandler.__init__(self)


