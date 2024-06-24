import multiprocessing
import multiprocessing.connection
import pickle
import time
import math
import devfx.exceptions as excs
import devfx.diagnostics as dgn

"""------------------------------------------------------------------------------------------------
"""
class Channel():
    class End(object):
        # ----------------------------------------------------------------  
        def __init__(self, receiver_end, receiver_end_lock, sender_end, sender_end_lock):
            self.__receiver_end = receiver_end
            self.__receiver_end_lock = receiver_end_lock
            self.__sender_end = sender_end
            self.__sender_end_lock = sender_end_lock

        def __getstate__(self):
            state = (self.__receiver_end, self.__receiver_end_lock, self.__sender_end, self.__sender_end_lock)
            return state

        def __setstate__(self, state):
            (self.__receiver_end, self.__receiver_end_lock, self.__sender_end, self.__sender_end_lock) = state

        def close(self):
            with self.__receiver_end_lock, self.__sender_end_lock:
                self.__receiver_end.close()
                self.__sender_end.close()


        # ----------------------------------------------------------------  
        def send(self, obj):
            with self.__sender_end_lock:
                try:
                    obj_bytes = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
                    self.__sender_end.send_bytes(obj_bytes)
                except Exception as exception:
                    excs.ErrorInfo.print()
                    raise exception

        # ----------------------------------------------------------------  
        def is_empty(self):
            with self.__receiver_end_lock:
                try:
                    is_empty = not self.__receiver_end.poll()
                    return is_empty
                except Exception as exception:
                    excs.ErrorInfo.print()
                    raise exception

        class Empty(Exception):
            pass

        def receive(self, timeout=None):
            with self.__receiver_end_lock:
                try:
                    wait_result = multiprocessing.connection.wait([self.__receiver_end], timeout=timeout)
                    if(len(wait_result) == 0):
                         raise Channel.End.Empty()
                    else:
                        obj_bytes = self.__receiver_end.recv_bytes()
                        obj = pickle.loads(obj_bytes)
                        return obj
                except Exception as exception:
                    excs.ErrorInfo.print()
                    raise exception

        def try_receive(self):
            with self.__receiver_end_lock:
                try:
                    wait_result = multiprocessing.connection.wait([self.__receiver_end], timeout=0)
                    if(len(wait_result) == 0):
                        return (False, None)
                    else:
                        obj_bytes = self.__receiver_end.recv_bytes()
                        obj = pickle.loads(obj_bytes)
                        return (True, obj)
                except Exception as exception:
                    excs.ErrorInfo.print()
                    raise exception

    def __init__(self):
        (end11, end12) = multiprocessing.Pipe(duplex=False)
        (lock21, lock22) = (multiprocessing.RLock(), multiprocessing.Lock())
        (end21, end22) = multiprocessing.Pipe(duplex=False)
        (lock11, lock12) = (multiprocessing.RLock(), multiprocessing.Lock())
        self.__end1 = Channel.End(end11, lock11, end22, lock22)
        self.__end2 = Channel.End(end21, lock21, end12, lock12)

    def __getstate__(self):
        state = (self.__end1, self.__end2)
        return state

    def __setstate__(self, state):
        (self.__end1, self.__end2) = state

    def close(self):
        self.__end1.close()
        self.__end2.close()


    @property
    def end1(self):
        return self.__end1

    @property
    def end2(self):
        return self.__end2
