from .. import constants as consts
from .event_handler import EventHandler

class KeyboardEventHandler(object):
    def __init__(self):
        self.__event_handler = EventHandler(self)

    # ----------------------------------------------------------------
    @property
    def OnKeyDown(self):
        return self.__event_handler.OnEvent(consts.EVT_KEY_DOWN)

    @OnKeyDown.setter
    def OnKeyDown(self, value):
        pass


    @property
    def OnKeyUp(self):
        return self.__event_handler.OnEvent(consts.EVT_KEY_UP)

    @OnKeyUp.setter
    def OnKeyUp(self, value):
        pass


    @property
    def OnKeyPress(self):
        return self.OnKeyDown

    @OnKeyPress.setter
    def OnKeyPress(self, value):
        pass

    # ----------------------------------------------------------------
    @property
    def OnHotKey(self):
        return self.__event_handler.OnEvent(consts.EVT_HOTKEY)

    @OnHotKey.setter
    def OnHotKey(self, value):
        pass

    # ----------------------------------------------------------------
    @property
    def OnGotFocus(self):
        return self.__event_handler.OnEvent(consts.EVT_GOT_FOCUS)

    @OnGotFocus.setter
    def OnGotFocus(self, value):
        pass


    @property
    def OnLostFocus(self):
        return self.__event_handler.OnEvent(consts.EVT_LOST_FOCUS)

    @OnLostFocus.setter
    def OnLostFocus(self, value):
        pass

    # ----------------------------------------------------------------
    @property
    def OnEnterKeyDown(self):
        return self.__event_handler.BindCallbackHandlers([self.OnKeyDown], 'CBK_KEY_ENTER_DOWN', lambda event_args: event_args.GetKeyCode() == consts.KEY_ENTER)

    @OnEnterKeyDown.setter
    def OnEnterKeyDown(self, value):
        pass


    @property
    def OnEnterKeyUp(self):
        return self.__event_handler.BindCallbackHandlers([self.OnKeyUp], 'CBK_KEY_ENTER_UP', lambda event_args: event_args.GetKeyCode() == consts.KEY_ENTER)

    @OnEnterKeyUp.setter
    def OnEnterKeyUp(self, value):
        pass


    @property
    def OnEnterKeyPress(self):
        return self.OnEnterKeyDown

    @OnEnterKeyPress.setter
    def OnEnterKeyPress(self, value):
        pass

    # ----------------------------------------------------------------
    @property
    def OnSpaceKeyDown(self):
        return self.__event_handler.BindCallbackHandlers([self.OnKeyDown], 'CBK_KEY_SPACE_DOWN', lambda event_args: event_args.GetKeyCode() == consts.KEY_SPACE)

    @OnSpaceKeyDown.setter
    def OnSpaceKeyDown(self, value):
        pass


    @property
    def OnSpaceKeyUp(self):
        return self.__event_handler.BindCallbackHandlers([self.OnKeyUp], 'CBK_KEY_SPACE_UP', lambda event_args: event_args.GetKeyCode() == consts.KEY_SPACE)

    @OnSpaceKeyUp.setter
    def OnSpaceKeyUp(self, value):
        pass


    @property
    def OnSpaceKeyPress(self):
        return self.OnSpaceKeyDown

    @OnSpaceKeyPress.setter
    def OnSpaceKeyPress(self, value):
        pass