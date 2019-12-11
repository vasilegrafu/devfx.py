import multiprocessing as mproc
import devfx.exceptions as exceps
import devfx.core as core
from .process_result import ProcessResult

class Process(mproc.Process):
    def __init__(self, name=None, target=None, args=(), kwargs={}):
        super().__init__(name=name)

        self.__target = target
        self.__args = args
        self.__kwargs = kwargs

        self.__queue = mproc.Queue()

        self.__result = None

    def run(self):
        try:
            result = self.__target(*self.__args, **self.__kwargs)
        except Exception as exception:
            result = exception
        finally:
            pass
        self.__queue.put(result)

    def has_result(self):
        return self.__queue.empty()
    
    @property
    def result(self):
        if(self.__result is None):
            if(self.__queue.empty()):
                raise exceps.OperationError()
            else:
                self.__result = ProcessResult(self.__queue.get())
                return self.__result
        else:
            return self.__result

