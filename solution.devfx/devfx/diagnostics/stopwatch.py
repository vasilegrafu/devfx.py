import datetime
import contextlib
import devfx.exceptions as exp


class Stopwatch(object):
    def __init__(self):
        self.__running = False

        self.__start = None
        self.__elapsed = datetime.timedelta(microseconds=0)
       
    def start(self):
        if(self.__running == True):
            raise exp.OperationError()

        self.__running = True
        self.__start = datetime.datetime.utcnow()
        return self

    def is_running(self):
        return self.__running

    def stop(self):
        if(self.__running == False):
            raise exp.OperationError()

        self.__running = False
        self.__elapsed = self.__elapsed + (datetime.datetime.utcnow() - self.__start)
        return self

    def reset(self):
        if(self.__running == False):
            self.__start = None
            self.__elapsed = datetime.timedelta(microseconds=0)
        else:
            self.__start = datetime.datetime.utcnow()
            self.__elapsed = datetime.timedelta(microseconds=0)
        return self

    @property
    def elapsed(self):
        if(self.__running == True):
            return self.__elapsed + (datetime.datetime.utcnow() - self.__start)
        else:
            return self.__elapsed

    @classmethod
    def start_new(cls):
        stopwatch = Stopwatch()
        stopwatch.start()
        return stopwatch   


@contextlib.contextmanager
def print_elapsed_time(message='{}'):
    try:
        stopwatch = Stopwatch()
        stopwatch.start()
        yield stopwatch
    finally:
        stopwatch.stop()
        print(message.format(stopwatch.elapsed))


