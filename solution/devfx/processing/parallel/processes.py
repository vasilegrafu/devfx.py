import multiprocessing
import devfx.exceptions as ex
import devfx.core as core

from .process import Process

class Processes(object):
    def __init__(self, processes):
        self.__processes = processes

    @classmethod
    def create(cls, n, name=lambda i: None, daemon=lambda i: None, fn=lambda i: None, args=lambda i: (), kwargs=lambda i: {}):
        return Processes([Process(name=name(i), daemon=daemon(i), fn=fn(i), args=args(i), kwargs=kwargs(i)) for i in range(0, n)])

    def __getitem__(self, key): 
        return self.__processes[key]
  
    def __setitem__(self, key, value): 
        self.__processes[key] = value

    def __len__(self):
        return len(self.__processes)

    def __iter__(self):
        for process in self.__processes:
            yield process
        
    # ----------------------------------------------------------------  
    def start(self):
        for process in self.__processes:
            process.start()

    def are_all_alive(self):
        return all((process.is_alive() for process in self.__processes))

    def are_any_alive(self):
        return any((process.is_alive() for process in self.__processes))

    def terminate(self):
        for process in self.__processes:
            process.terminate()

    def kill(self):
        for process in self.__processes:
            process.kill()

    def close(self):
        for process in self.__processes:
            process.close()
  
    # ----------------------------------------------------------------  
    @property
    def results(self):
        return [process.result for process in self.__processes]

    # ----------------------------------------------------------------  
    def join(self):
        for process in self.__processes:
            process.join()

    def wait(self):       
        for process in self.__processes:
            process.wait()

