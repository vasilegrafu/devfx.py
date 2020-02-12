
class SignalHandler(object):
    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, source, signal_args):
        self.__fn(source=source, signal_args=signal_args)



