import time
import devfx.core as core
import devfx.diagnostics as dgn
import devfx.processing.parallel as pp

class Targets(object):
    def target1(self, p1, p2):
        time.sleep(2)
        print(p1, p2)
        return (p1, p2)

    def target2(self, p1, p2):
        time.sleep(2)
        print(p1, p2)
        return (p1, p2)

def main():
    sw = dgn.Stopwatch().start()

    targets = Targets()

    process1 = pp.Process(fn=targets.target1, args=(1, 1))
    process1.start()

    process2 = pp.Process(fn=targets.target2, args=(2, 2))
    process2.start()

    process1.join()
    process2.join()

    print(process1.result)

    print(process2.result)

    print("time elapsed: ", sw.stop().elapsed)

if(__name__ == '__main__'):
    main()

