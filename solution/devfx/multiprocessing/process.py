import multiprocessing

class Process(multiprocessing.Process):
    def __init__(self, target, *args, **kwargs):
        super().__init__()
        self.__target = target
        self.__args = args
        self.__kwargs = kwargs

        self.__parent_connection, self.__child_connection = multiprocessing.Pipe()
        self.__result = None

    def run(self):
        try:
            result = self.__target(*self.__args, **self.__kwargs)
        except Exception as exception:
            result = exception
        finally:
            pass
        self.__child_connection.send(result)

    @property
    def result(self):
        if self.__parent_connection.poll():
            self.__result = self.__parent_connection.recv()
        return self.__result

    def result_is_exception(self):
        return isinstance(self.result, Exception)
