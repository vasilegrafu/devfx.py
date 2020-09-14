import time
import devfx.core as core
import devfx.diagnostics as dgn
import devfx.parallel.processing as parallel

class Targets(object):
    def __init__(self):
        self.__lock = parallel.Lock()

    def target(self, *args, **kwargs):
        self.__lock.acquire()
        time.sleep(2)
        self.__lock.release()

def main():
    sw = dgn.stopwatch().start()

    targets = Targets()

    process1 = parallel.Process().target(fn=targets.target)
    process1.start()

    process2 = parallel.Process().target(fn=targets.target)
    process2.start()

    process1.join()
    process2.join()

    if(process1.result.is_exception()):
        print(process1.result.value)

    if(process2.result.is_exception()):
        print(process2.result.value)

    print("time elapsed: ", sw.stop().elapsed)


if (__name__ == '__main__'):
    main()

