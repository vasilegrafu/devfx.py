import devfx.multiprocessing as mproc
import devfx.diagnostics as dgn
import time

class Targets(object):
    lock = mproc.Lock()

    @classmethod
    def target(cls, *args, **kwargs):
        cls.lock.acquire()
        time.sleep(2)
        cls.lock.release()

def main():
    sw = dgn.stopwatch().start()

    process1 = mproc.Process(target=Targets.target)
    process1.start()

    process2 = mproc.Process(target=Targets.target)
    process2.start()

    process1.join()
    process2.join()

    if (process1.result_is_exception()):
        print(process1.result)

    if (process2.result_is_exception()):
        print(process2.result)

    print("time elapsed: ", sw.stop().elapsed)


if (__name__ == '__main__'):
    main()
