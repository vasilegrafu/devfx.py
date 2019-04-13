import devfx.multiprocessing as mproc
import time

class Producer(object):
    def __init__(self):
        pass

    def run(self, queue):
        i = 0
        while True:
            i += 1
            queue.put(i)
            time.sleep(0.05)
