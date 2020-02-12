
class SignalHandlers(object):
    def __init__(self):
        self.__event_handler_list = []

    """------------------------------------------------------------------------------------------------
    """
    def __iadd__(self, event_handler):
        self.__event_handler_list.append(event_handler)
        return self

    def __isub__(self, event_handler):
        while event_handler in self.__event_handler_list:
            self.__event_handler_list.remove(event_handler)
        return self

    """------------------------------------------------------------------------------------------------
    """
    def __len__(self):
        return len(self.__event_handler_list)

    def __iter__(self):
        for event_handler in self.__event_handler_list:
            yield event_handler

    """------------------------------------------------------------------------------------------------
    """
    def __call__(self, source, signal_args):
        for event_handler in self.__event_handler_list:
            event_handler(source=source, signal_args=signal_args)


