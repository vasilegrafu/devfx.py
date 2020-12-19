import time
import devfx.core as core
import devfx.diagnostics as dgn
import devfx.processing.parallel as pp

class Targets(object):
    lock = pp.Lock()

    @classmethod
    def target(cls, *args, **kwargs):
        cls.lock.acquire()
        time.sleep(2)
        cls.lock.release()

def main():
    sw = dgn.stopwatch().start()

    process1 = pp.Process(fn=Targets.target)
    process1.start()

    process2 = pp.Process(fn=Targets.target)
    process2.start()

    process1.join()
    process2.join()

    print(process1.result)

    print(process2.result)

    print("time elapsed: ", sw.stop().elapsed)


if (__name__ == '__main__'):
    main()

