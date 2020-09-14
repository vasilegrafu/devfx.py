import wx
import devfx.core as core
from . import constants as consts
from . import layout
from . import events
from . import groups

class Window(wx.Frame, 
             events.GenericEventHandler, 
             events.MouseEventHandler, 
             events.KeyboardEventHandler, 
             events.ApplicationEventHandler,
             groups.GroupHandler):
    def __init__(self, parent=None, id=wx.ID_ANY, title='', size=(256, 256), align=(consts.CENTER, consts.CENTER), **kwargs):
        wx.Frame.__init__(self, parent, id=id, title=title, size=size, **kwargs)
        layout.LayoutHandler.__init__(self)
        events.GenericEventHandler.__init__(self)
        events.MouseEventHandler.__init__(self)
        events.KeyboardEventHandler.__init__(self)
        events.ApplicationEventHandler.__init__(self)

        self.align = align

    # ----------------------------------------------------------------
    @property
    def OnShow(self):
        return self.OnEvent(consts.EVT_WINDOW_SHOW)

    @OnShow.setter
    def OnShow(self, value):
        pass


    @property
    def OnClose(self):
        return self.OnEvent(consts.EVT_WINDOW_CLOSE)

    @OnClose.setter
    def OnClose(self, value):
        pass


    @property
    def OnMove(self):
        return self.OnEvent(consts.EVT_WINDOW_MOVE)

    @OnMove.setter
    def OnMove(self, value):
        pass


    @property
    def OnMaximize(self):
        return self.OnEvent(consts.EVT_WINDOW_MAXIMIZE)

    @OnMaximize.setter
    def OnMaximize(self, value):
        pass


    @property
    def OnIconize(self):
        return self.OnEvent(consts.EVT_WINDOW_ICONIZE)

    @OnIconize.setter
    def OnIconize(self, value):
        pass


    @property
    def OnCreate(self):
        return self.OnEvent(consts.EVT_WINDOW_CREATE)

    @OnCreate.setter
    def OnCreate(self, value):
        pass


    @property
    def OnDestroy(self):
        return self.OnEvent(consts.EVT_WINDOW_DESTROY)

    @OnDestroy.setter
    def OnDestroy(self, value):
        pass


    # ----------------------------------------------------------------
    @core.setter   
    def align(self, value):
        horizontal_align, vertical_align = value
        _, _, screenwidth, screenheight = wx.ClientDisplayRect()
        windowwidth, windowheight = self.GetSize()

        if(horizontal_align == consts.LEFT):
            xposition = 0
        if(horizontal_align in (consts.CENTER, consts.CENTRE)):
            xposition = int(screenwidth/2 - windowwidth/2)
        if(horizontal_align == consts.RIGHT):
            xposition = int(screenwidth - windowwidth)

        if(vertical_align == consts.TOP):
            yposition = 0
        if(vertical_align in (consts.CENTER, consts.CENTRE)):
            yposition = int(screenheight/2 - windowheight/2)
        if(vertical_align == consts.BOTTOM):
            yposition = int(screenheight - windowheight)

        self.SetPosition((xposition, yposition))


