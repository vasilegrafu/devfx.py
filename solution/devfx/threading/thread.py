import threading

class Thread(threading.Thread):
    def __init__(self, target, *args, **kwargs):
        super().__init__()
        self.__target = target
        self.__args = args
        self.__kwargs = kwargs

        self.__result = None

    def run(self):
        try:
            result = self.__target(*self.__args, **self.__kwargs)
        except Exception as exception:
            result = exception
        finally:
            pass
        self.__result = result

    @property
    def result(self):
        return self.__result

    def result_is_exception(self):
        return isinstance(self.result, Exception)
