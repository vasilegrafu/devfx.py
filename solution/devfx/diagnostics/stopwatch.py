import datetime as dt
import devfx.exceptions as excs

class stopwatch(object):
    def __init__(self):
        self.__running = False

        self.__start = None
        self.__elapsed = dt.timedelta(microseconds=0)
       
    def start(self):
        if(self.__running == True):
            raise excs.OperationError()

        self.__running = True
        self.__start = dt.datetime.utcnow()
        return self

    def is_running(self):
        return self.__running

    def stop(self):
        if(self.__running == False):
            raise excs.OperationError()

        self.__running = False
        self.__elapsed = self.__elapsed + (dt.datetime.utcnow() - self.__start)
        return self

    def reset(self):
        if(self.__running == False):
            self.__start = None
            self.__elapsed = dt.timedelta(microseconds=0)
        else:
            self.__start = dt.datetime.utcnow()
            self.__elapsed = dt.timedelta(microseconds=0)
        return self

    @property
    def elapsed(self):
        if(self.__running == True):
            return self.__elapsed + (dt.datetime.utcnow() - self.__start)
        else:
            return self.__elapsed

    @classmethod
    def start_new(cls):
        sw = stopwatch()
        sw.start()
        return sw      

"""------------------------------------------------------------------------------------------------
"""
def test():
    sw = stopwatch()

    #
    sw.start()
    for i in range(0, 1024*1024*4):
        pass
    print("time elapsed: ", sw.stop().elapsed)

    #
    for i in range(0, 1024*1024*4):
        pass

    #
    sw.start()
    for i in range(0, 1024*1024*4):
        pass
    print("time elapsed: ", sw.stop().elapsed)


"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    test()

