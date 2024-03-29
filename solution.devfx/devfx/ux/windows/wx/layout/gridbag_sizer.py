import wx
import devfx.core as core
from .layout_handler import LayoutHandler
from .. import groups

class GridBagSizer(wx.GridBagSizer, 
                   LayoutHandler, 
                   groups.GroupHandler):
    def __init__(self, *args, **kwargs):
        wx.GridBagSizer.__init__(self, *args, **kwargs)
        LayoutHandler.__init__(self)
        groups.GroupHandler.__init__(self)
    
    # ----------------------------------------------------------------
    def AddToWindow(self, window, *args, **kwargs):
        window.SetSizer(self, *args, **kwargs)
        return self

    def AddToWindowAndFit(self, window, *args, **kwargs):
        window.SetSizerAndFit(self, *args, **kwargs)
        return self

