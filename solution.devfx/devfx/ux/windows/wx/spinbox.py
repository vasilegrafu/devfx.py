import wx
import devfx.core as core
from . import constants as consts
from . import layout
from . import events

"""------------------------------------------------------------------------------------------------
"""
class IntSpinBox(wx.SpinCtrl, 
                 layout.LayoutHandler,
                 events.GenericEventHandler, 
                 events.MouseEventHandler, 
                 events.KeyboardEventHandler, 
                 events.ApplicationEventHandler):
    def __init__(self, parent, id=wx.ID_ANY, min=0, max=100, initial=0, inc=1, **kwargs):
        wx.SpinCtrl.__init__(self, parent, id=id, min=min, max=max, initial=initial, inc=inc, **kwargs)
        layout.LayoutHandler.__init__(self)
        events.GenericEventHandler.__init__(self)
        events.MouseEventHandler.__init__(self)
        events.KeyboardEventHandler.__init__(self)
        events.ApplicationEventHandler.__init__(self)

    # ----------------------------------------------------------------
    @property
    def OnValueChanged(self):
        return self.OnEvent(consts.EVT_INTSPINBOX_VALUE_CHANGED)

    @OnValueChanged.setter
    def OnValueChanged(self, value):
        pass


"""------------------------------------------------------------------------------------------------
"""
class FloatSpinBox(wx.SpinCtrlDouble, 
                   layout.LayoutHandler,
                   events.GenericEventHandler, 
                   events.MouseEventHandler, 
                   events.KeyboardEventHandler, 
                   events.ApplicationEventHandler):
    def __init__(self, parent, id=wx.ID_ANY, min=0, max=100, initial=0, inc=1, **kwargs):
        wx.SpinCtrlDouble.__init__(self, parent, id=id, min=min, max=max, initial=initial, inc=inc, **kwargs)
        layout.LayoutHandler.__init__(self)
        events.GenericEventHandler.__init__(self)
        events.MouseEventHandler.__init__(self)
        events.KeyboardEventHandler.__init__(self)
        events.ApplicationEventHandler.__init__(self)

    # ----------------------------------------------------------------
    @property
    def OnValueChanged(self):
        return self.OnEvent(consts.EVT_FLOATSPINBOX_VALUE_CHANGED)

    @OnValueChanged.setter
    def OnValueChanged(self, value):
        pass



