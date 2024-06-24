import multiprocessing
import time
import devfx.exceptions as excs
import devfx.core as core

class Process(multiprocessing.Process):
    def __init__(self, name=None, daemon=None, fn=None, args=(), kwargs={}):
        super().__init__(name=name, daemon=daemon)

        self.__fn = fn
        self.__args = args
        self.__kwargs = kwargs

        self.__queue = multiprocessing.Queue()
        self.__is_started_event = multiprocessing.Event()

        self.__result = None

    def start(self):
        super().start()
        self.__is_started_event.wait()
        x = 0

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
            process_result = Process._Result(value=fn_result)
        except Exception as exception:
            process_result = Process._Result(value=exception)
            excs.ErrorInfo.print()
        finally:
            self.__is_started_event.clear()
            self.__queue.put(process_result)

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
            raise excs.ApplicationError(inner=self.__result.value)
        else:
            return self.__result.value

    # ----------------------------------------------------------------  
    def terminate(self):
        super().terminate()
        while(self.is_alive()):
            time.sleep(0.001)

    def kill(self):
        super().kill()
        while(self.is_alive()):
            time.sleep(0.001)

    def close(self):
        super().close()


    # ----------------------------------------------------------------  
    def join(self):
        super().join()
        if(self.__result is None):
            self.__result = self.__queue.get()
        if(core.is_typeof(self.__result.value, Exception)):
            raise excs.ApplicationError(inner=self.__result.value)
        else:
            pass

    def wait(self):       
        self.join()


