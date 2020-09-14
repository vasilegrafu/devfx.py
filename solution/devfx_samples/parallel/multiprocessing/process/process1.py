import time
import devfx.core as core
import devfx.diagnostics as dgn
import devfx.parallel.processing as parallel

class TargetArgs(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p1

class TargetResult(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p1

class Targets(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def target1(self, p1, p2):
        time.sleep(2)
        print(self.p1, self.p2)
        print(p1, p2)
        return TargetResult('target1', 'target1')

    def target2(self, p1, p2):
        time.sleep(2)
        print(self.p1, self.p2)
        print(p1, p2)
        return TargetResult('target2', 'target2')

def main():
    sw = dgn.stopwatch().start()

    targets = Targets(4, 4)

    process1 = parallel.Process().target(targets.target1, p1=1, p2=1)
    process1.start()

    process2 = parallel.Process().target(targets.target2, p1=2, p2=2)
    process2.start()

    process1.join()
    process2.join()

    if(process1.result.is_exception()):
        print(process1.result.value)
    else:
        print(process1.result.value.p1, process1.result.value.p2)

    if(process2.result.is_exception()):
        print(process2.result.value)
    else:
        print(process2.result.value.p1, process2.result.value.p2)

    print("time elapsed: ", sw.stop().elapsed)

if(__name__ == '__main__'):
    main()

