import time

class Producer(object):
    def __init__(self, id):
        self.__id = id

    def run(self, queue):
        i = 0
        while True:
            i += 1
            if(i > 64):
                queue.put((self.__id, None))
                break
            queue.put((self.__id, i))
            time.sleep(0.05)
