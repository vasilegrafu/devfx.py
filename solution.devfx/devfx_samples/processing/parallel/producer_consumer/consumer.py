import time

class Consumer(object):
    def __init__(self):
        pass

    def run(self, queue):
        while True:
            (id, i) = queue.get()
            if(i is None):
                break
            print(f'producer_{id}: {i}')
