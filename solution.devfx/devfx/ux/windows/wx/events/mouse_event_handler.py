from .. import constants as consts
from .event_handler import EventHandler

class MouseEventHandler(object):
    def __init__(self):
        self.__event_handler = EventHandler(self)

    # ----------------------------------------------------------------
    @property
    def OnMouseLeftDown(self):
        return self.__event_handler.OnEvent(consts.EVT_MOUSE_LEFT_DOWN)

    @OnMouseLeftDown.setter
    def OnMouseLeftDown(self, value):
        pass


    @property
    def OnMouseLeftUp(self):
        return self.__event_handler.OnEvent(consts.EVT_MOUSE_LEFT_UP)

    @OnMouseLeftUp.setter
    def OnMouseLeftUp(self, value):
        pass


    @property
    def OnMouseLeftClick(self):
        return self.OnMouseLeftUp

    @OnMouseLeftClick.setter
    def OnMouseLeftClick(self, value):
        pass


    @property
    def OnMouseClick(self):
        return self.OnMouseLeftClick

    @OnMouseClick.setter
    def OnMouseClick(self, value):
        pass

    # ----------------------------------------------------------------
    @property
    def OnMouseMiddleDown(self):
        return self.__event_handler.OnEvent(consts.EVT_MOUSE_MIDDLE_DOWN)

    @OnMouseMiddleDown.setter
    def OnMouseMiddleDown(self, value):
        pass


    @property
    def OnMouseMiddleUp(self):
        return self.__event_handler.OnEvent(consts.EVT_MOUSE_MIDDLE_UP)

    @OnMouseMiddleUp.setter
    def OnMouseMiddleUp(self, value):
        pass


    @property
    def OnMouseMiddleClick(self):
        return self.__event_handler.OnEvent(consts.EVT_MOUSE_MIDDLE_CLICK)

    @OnMouseMiddleClick.setter
    def OnMouseMiddleClick(self, value):
        pass

    # ----------------------------------------------------------------
    @property
    def OnMouseRightDown(self):
        return self.__event_handler.OnEvent(consts.EVT_MOUSE_RIGHT_DOWN)

    @OnMouseRightDown.setter
    def OnMouseRightDown(self, value):
        pass


    @property
    def OnMouseRightUp(self):
        return self.__event_handler.OnEvent(consts.EVT_MOUSE_RIGHT_UP)

    @OnMouseRightUp.setter
    def OnMouseRightUp(self, value):
        pass


    @property
    def OnMouseRightClick(self):
        return self.__event_handler.OnEvent(consts.EVT_MOUSE_RIGHT_CLICK)

    @OnMouseRightClick.setter
    def OnMouseRightClick(self, value):
        pass

    # ----------------------------------------------------------------
    @property
    def OnMouseLeftDoubleClick(self):
        return self.__event_handler.OnEvent(consts.EVT_MOUSE_LEFT_DOUBLECLICK)

    @OnMouseLeftDoubleClick.setter
    def OnMouseLeftDoubleClick(self, value):
        pass


    @property
    def OnMouseMiddleDoubleClick(self):
        return self.__event_handler.OnEvent(consts.EVT_MOUSE_MIDDLE_DOUBLECLICK)

    @OnMouseMiddleDoubleClick.setter
    def OnMouseMiddleDoubleClick(self, value):
        pass


    @property
    def OnMouseRightDoubleClick(self):
        return self.__event_handler.OnEvent(consts.EVT_MOUSE_RIGHT_DOUBLECLICK)

    @OnMouseRightDoubleClick.setter
    def OnMouseRightDoubleClick(self, value):
        pass

    # ----------------------------------------------------------------
    @property
    def OnMouseEnter(self):
        return self.__event_handler.OnEvent(consts.EVT_MOUSE_ENTER)

    @OnMouseEnter.setter
    def OnMouseEnter(self, value):
        pass


    @property
    def OnMouseMove(self):
        return self.__event_handler.OnEvent(consts.EVT_MOUSE_MOVE)

    @OnMouseMove.setter
    def OnMouseMove(self, value):
        pass


    @property
    def OnMouseLeave(self):
        return self.__event_handler.OnEvent(consts.EVT_MOUSE_LEAVE)

    @OnMouseLeave.setter
    def OnMouseLeave(self, value):
        pass

