import threading, queue
import devfx.exceptions as exps
import devfx.core as core

class Thread(threading.Thread):
    def __init__(self, name=None):
        super().__init__(name=name)

    """------------------------------------------------------------------------------------------------
    """
    def target(self, fn, *args, **kwargs):
        self.__fn = fn
        self.__args = args
        self.__kwargs = kwargs

        self.__queue = queue.Queue()

        self.__result = None

        return self

    """------------------------------------------------------------------------------------------------
    """
    def run(self):
        try:
            result = self.__fn(*self.__args, **self.__kwargs)
        except Exception as exception:
            result = exception
            print(exception)
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
                self.__result = TargetResult(thread_name=self.name, value=self.__queue.get())
                return self.__result
        else:
            return self.__result


class TargetResult(object):
    def __init__(self, thread_name, value):
        self.__thread_name = thread_name
        self.__value = value

    """------------------------------------------------------------------------------------------------
    """
    @property
    def thread_name(self):
        return self.__thread_name

    @property
    def value(self):
        return self.__value

    """------------------------------------------------------------------------------------------------
    """
    def is_exception(self):
        return core.is_typeof(self.__value, Exception)

