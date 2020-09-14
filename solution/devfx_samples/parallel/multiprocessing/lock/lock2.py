import time
import devfx.core as core
import devfx.diagnostics as dgn
import devfx.parallel.processing as parallel

class Targets(object):
    lock = parallel.Lock()

    @classmethod
    def target(cls, *args, **kwargs):
        cls.lock.acquire()
        time.sleep(2)
        cls.lock.release()

def main():
    sw = dgn.stopwatch().start()

    process1 = parallel.Process().target(fn=Targets.target)
    process1.start()

    process2 = parallel.Process().target(fn=Targets.target)
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

