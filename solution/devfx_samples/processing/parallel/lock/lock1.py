import time
import devfx.core as core
import devfx.diagnostics as dgn
import devfx.processing.parallel as pp

class Targets(object):
    def __init__(self):
        self.__lock = pp.Lock()

    def target(self, *args, **kwargs):
        self.__lock.acquire()
        time.sleep(2)
        self.__lock.release()
        return 0

def main():
    sw = dgn.stopwatch().start()

    targets = Targets()

    process1 = pp.Process(fn=targets.target)
    process1.start()

    process2 = pp.Process(fn=targets.target)
    process2.start()

    process1.join()
    process2.join()

    print(process1.result)
    print(process2.result)

    print("time elapsed: ", sw.stop().elapsed)


if (__name__ == '__main__'):
    main()

