import wx
import devfx.core as core
from . import constants as consts
from . import layout
from . import events

class ComboBox(wx.ComboBox, 
                layout.LayoutHandler,
                events.GenericEventHandler, 
                events.MouseEventHandler, 
                events.KeyboardEventHandler, 
                events.ApplicationEventHandler):
    def __init__(self, parent, id=wx.ID_ANY, value='', choices=[], **kwargs):
        # indexed_choices = [(i, choice) for (i, choice) in enumerate(choices)]


        wx.ComboBox.__init__(self, parent, id=id, value=value, choices=choices, **kwargs)
        layout.LayoutHandler.__init__(self)
        events.GenericEventHandler.__init__(self)
        events.MouseEventHandler.__init__(self)
        events.KeyboardEventHandler.__init__(self)
        events.ApplicationEventHandler.__init__(self)

    # ----------------------------------------------------------------
    @property
    def OnItemSelected(self):
        return self.OnEvent(consts.EVT_COMBOBOX_ITEM_SELECTED)

    @OnItemSelected.setter
    def OnItemSelected(self, value):
        pass
