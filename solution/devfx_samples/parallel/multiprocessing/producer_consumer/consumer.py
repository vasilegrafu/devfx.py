import time

class Consumer(object):
    def __init__(self, n):
        self.__n = n

    def run(self, queue):
        while True:
            i = queue.get(timeout=0.5)
            if(i is None):
                break
            print(f'consumer_{self.__n}: {i}')
