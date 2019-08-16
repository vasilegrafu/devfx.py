import datetime as dt
import devfx.exceptions as exceps

class stopwatch(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.__running = False

        self.__start = 0
        self.__elapsed = dt.timedelta(microseconds=0)
        return self
        
    def start(self):
        if(self.__running == True):
            raise exceps.OperationError()

        self.__running = True
        self.__start = dt.datetime.utcnow()
        return self

    def stop(self):
        if(self.__running == False):
            raise exceps.OperationError()

        self.__running = False
        self.__elapsed = self.__elapsed + (dt.datetime.utcnow() - self.__start)
        return self


    @property
    def elapsed(self):
        if(self.__running == True):
            return self.__elapsed + (dt.datetime.utcnow() - self.__start)
        else:
            return self.__elapsed


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

