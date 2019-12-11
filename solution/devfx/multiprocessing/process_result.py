import devfx.core as core

class ProcessResult(object):
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def is_exception(self):
        return core.is_typeof(self.__value, Exception)
