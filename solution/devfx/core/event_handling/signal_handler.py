
class SignalHandler(object):
    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, source, event_args):
        self.__fn(source=source, event_args=event_args)



