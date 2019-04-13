import multiprocessing as mproc
import devfx.reflection as refl

class Process(mproc.Process):
    def __init__(self, target, *args, **kwargs):
        super().__init__()
        self.__target = target
        self.__args = args
        self.__kwargs = kwargs

        self.__queue = mproc.Queue()
        self.__target_result = None

    def run(self):
        try:
            target_result = self.__target(*self.__args, **self.__kwargs)
        except Exception as exception:
            target_result = exception
        finally:
            pass
        self.__target_result = target_result
        self.__queue.put(self.__target_result)

    @property
    def result(self):
        if(not self.__queue.empty()):
            self.__target_result = self.__queue.get() 
        return self.__target_result

    def result_is_exception(self):
        return refl.is_typeof(self.result, Exception)
