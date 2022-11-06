import threading
import queue
import devfx.exceptions as excps
import devfx.core as core

class Thread(threading.Thread):
    def __init__(self, name=None, fn=None, args=(), kwargs={}):
        super().__init__(name=name)

        self.__fn = fn
        self.__args = args
        self.__kwargs = kwargs

        self.__queue = queue.Queue()
        self.__is_started_event = threading.Event()

        self.__result = None

    # ----------------------------------------------------------------  
    def start(self):
        super().start()
        self.__is_started_event.wait()

    def is_alive(self):
        super().is_alive()

    # ----------------------------------------------------------------  
    class _Result(object):
        def __init__(self, value):
            self.__value = value

        @property
        def value(self):
            return self.__value

    def run(self):
        try:
            self.__is_started_event.set()
            fn_result = self.__fn(*self.__args, **self.__kwargs)
            thread_result = Thread._Result(value=fn_result)
        except Exception as exception:
            thread_result = Thread._Result(value=exception)
            excps.ErrorInfo.print()
        finally:
            self.__is_started_event.clear()
            self.__queue.put(thread_result)
   
    def has_result(self):
        if(self.__result is None):
            if(self.__queue.empty()):
                return False
            else:
                return True
        else:
            return True

    @property
    def result(self):
        if(self.__result is None):
            self.__result = self.__queue.get()
        if(core.is_typeof(self.__result.value, Exception)):
            raise excps.ApplicationError(inner=self.__result.value)
        else:
            return self.__result.value

    # ----------------------------------------------------------------  
    def join(self):
        super().join()

        if(self.__result is None):
            self.__result = self.__queue.get()
        if(core.is_typeof(self.__result.value, Exception)):
            raise excps.ApplicationError(inner=self.__result.value)
        else:
            pass

    def wait(self):       
        self.join()


