from .. import constants as consts
from .event_handler import EventHandler

class ApplicationEventHandler(object):
    def __init__(self):
        self.__event_handler = EventHandler(self)

    # ----------------------------------------------------------------
    @property
    def OnPaint(self):
        return self.__event_handler.OnEvent(consts.EVT_PAINT)

    @OnPaint.setter
    def OnPaint(self, value):
        pass

    # ----------------------------------------------------------------
    @property
    def OnEraseBackground(self):
        return self.__event_handler.OnEvent(consts.EVT_ERASE_BACKGROUND)

    @OnEraseBackground.setter
    def OnEraseBackground(self, value):
        pass

    # ----------------------------------------------------------------
    @property
    def OnSizeChanged(self):
        return self.__event_handler.OnEvent(consts.EVT_SIZE_CHANGED)

    @OnSizeChanged.setter
    def OnSizeChanged(self, value):
        pass

