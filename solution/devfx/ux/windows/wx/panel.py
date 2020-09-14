import wx
import devfx.core as core
from . import constants as consts
from . import layout
from . import events
from . import groups

class Panel(wx.Panel, 
            layout.LayoutHandler,
            events.GenericEventHandler, 
            events.MouseEventHandler, 
            events.KeyboardEventHandler, 
            events.ApplicationEventHandler,
            groups.GroupHandler):
    def __init__(self, parent, id=wx.ID_ANY, **kwargs):
        wx.Panel.__init__(self, parent, id=id, **kwargs)
        layout.LayoutHandler.__init__(self)
        events.GenericEventHandler.__init__(self)
        events.MouseEventHandler.__init__(self)
        events.KeyboardEventHandler.__init__(self)
        events.ApplicationEventHandler.__init__(self)


