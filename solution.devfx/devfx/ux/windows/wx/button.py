import wx
import devfx.core as core
from . import constants as consts
from . import layout
from . import events

class Button(wx.Button, 
             layout.LayoutHandler,
             events.GenericEventHandler, 
             events.MouseEventHandler, 
             events.KeyboardEventHandler, 
             events.ApplicationEventHandler):
    def __init__(self, parent, id=wx.ID_ANY, label='', **kwargs):
        wx.Button.__init__(self, parent, id=id, label=label, **kwargs)
        layout.LayoutHandler.__init__(self)
        events.GenericEventHandler.__init__(self)
        events.MouseEventHandler.__init__(self)
        events.KeyboardEventHandler.__init__(self)
        events.ApplicationEventHandler.__init__(self)

    # ----------------------------------------------------------------
    @property
    def OnPress(self):
        return self.BindCallbackHandlers([self.OnMouseClick, self.OnEnterKeyPress], 'CBK_BUTTON_PRESS')

    @OnPress.setter
    def OnPress(self, value):
        pass



    



