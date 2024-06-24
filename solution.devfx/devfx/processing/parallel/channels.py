import multiprocessing
import devfx.exceptions as excs
import devfx.core as core

from .channel import Channel

class Channels(object):
    class Ends(object):
        def __init__(self, ends):
            self.__ends = ends

        def send(self, obj):
            for end in self.__ends:
                end.send(obj)

        def is_empty(self):
            return all([end.is_empty() for end in self.__ends])

        def receive(self, timeout=None):
            return [end.receive(timeout=timeout) for end in self.__ends]

        def try_receive(self):
            return [end.try_receive() for end in self.__ends]              

    def __init__(self, channels):
        self.__channels = channels
        self.__end1 = Channels.Ends([channel.end1 for channel in self.__channels])
        self.__end2 = Channels.Ends([channel.end2 for channel in self.__channels])

    @classmethod
    def create(cls, n):
        return Channels([Channel() for _ in range(0, n)])

    def __getitem__(self, key): 
        return self.__channels[key]
  
    def __setitem__(self, key, value): 
        self.__channels[key] = value

    def __len__(self):
        return len(self.__channels)

    def __iter__(self):
        for channel in self.__channels:
            yield channel


    def end1(self, key):
        return self.__channels[key].end1

    def end2(self, key):
        return self.__channels[key].end2


    @property
    def end1s(self):
        return self.__end1

    @property
    def end2s(self):
        return self.__end2