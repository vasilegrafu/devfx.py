import wx
import devfx.core as core
from .layout_handler import LayoutHandler
from .. import groups

class FlexGridSizer(wx.FlexGridSizer, 
                    LayoutHandler, 
                    groups.GroupHandler):
    def __init__(self, *args, **kwargs):
        wx.FlexGridSizer.__init__(self, *args, **kwargs)
        LayoutHandler.__init__(self)
        groups.GroupHandler.__init__(self)
    
    # ----------------------------------------------------------------
    def AddToWindow(self, window, *args, **kwargs):
        window.SetSizer(self, *args, **kwargs)
        return self