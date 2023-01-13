from .callback_list import CallbackList

class EventHandler(object):
    def __init__(self, obj):
        self.__obj = obj
        self.__callback_handlers = {}

    """------------------------------------------------------------------------------------------------
    """
    def OnEvent(self, event):
        if(event not in self.__callback_handlers):
            self.__callback_handlers[event] = CallbackList()
            def _(event_args): 
                try:
                    callback_handler = self.__callback_handlers[event]
                    callback_handler(self.__obj, event_args)
                finally:
                    event_args.Skip()
            self.__obj.Bind(event, _)
        return self.__callback_handlers[event]

    """------------------------------------------------------------------------------------------------
    """
    def OnCallback(self, name):
        if(name not in self.__callback_handlers):
            self.__callback_handlers[name] = CallbackList()
        return self.__callback_handlers[name]

    """------------------------------------------------------------------------------------------------
    """
    def BindCallbackHandlers(self, callback_handlers, cbk_name, cbk_call_condition_fn=None):
        def _(sender, event_args):
            if (cbk_call_condition_fn is None) or cbk_call_condition_fn(event_args):
                self.OnCallback(cbk_name)(sender, event_args)
        for callback_handler in callback_handlers:
            callback_handler += _
        return self.OnCallback(cbk_name)



            
        

