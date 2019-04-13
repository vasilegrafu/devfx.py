import devfx.multiprocessing as mproc
import time

class Consumer(object):
    def __init__(self):
        pass

    def run(self, queue):
        while True:
            i = queue.get()
            print(i)
