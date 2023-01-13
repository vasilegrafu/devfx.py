from .. import constants as consts
from .event_handler import EventHandler

class GenericEventHandler(object):
    def __init__(self):
        self.__event_handler = EventHandler(self)

    # ----------------------------------------------------------------
    def OnEvent(self, event):
        return self.__event_handler.OnEvent(event)

    def OnCallback(self, name):
        return self.__event_handler.OnCallback(name)

    # ----------------------------------------------------------------
    def BindCallbackHandlers(self, callback_handlers, cbk_name, cbk_call_condition_fn=None):
        return self.__event_handler.BindCallbackHandlers(callback_handlers, cbk_name, cbk_call_condition_fn)




