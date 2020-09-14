import multiprocessing
import devfx.exceptions as exps
import devfx.core as core

class Process(multiprocessing.Process):
    def __init__(self, name=None, daemon=False):
        super().__init__(name=name, daemon=daemon)

    """------------------------------------------------------------------------------------------------
    """
    def target(self, fn, *args, **kwargs):
        self.__fn = fn
        self.__args = args
        self.__kwargs = kwargs

        self.__queue = multiprocessing.Queue()

        self.__result = None

        return self

    """------------------------------------------------------------------------------------------------
    """
    def run(self):
        try:
            result = self.__fn(*self.__args, **self.__kwargs)
        except Exception as exception:
            result = exception
        finally:
            pass
        self.__queue.put(result)

    def has_result(self):
        return self.__queue.empty()
    
    """------------------------------------------------------------------------------------------------
    """
    @property
    def result(self):
        if(self.__result is None):
            if(self.__queue.empty()):
                raise exps.OperationError()
            else:
                self.__result = TargetResult(process_name=self.name, value=self.__queue.get())
                return self.__result
        else:
            return self.__result


class TargetResult(object):
    def __init__(self, process_name, value):
        self.__process_name = process_name
        self.__value = value

    """------------------------------------------------------------------------------------------------
    """
    @property
    def process_name(self):
        return self.__process_name

    @property
    def value(self):
        return self.__value

    """------------------------------------------------------------------------------------------------
    """
    def is_exception(self):
        return core.is_typeof(self.__value, Exception)

