import os
from .path import path as Path

class directory_info(object):
    """----------------------------------------------------------------
    """
    @classmethod
    def parent_directorypath(cls, path):
        return Path.head(path)

    @classmethod
    def parent_directoryname(cls, path):
        return Path.tail(Path.head(path))

    @classmethod
    def name(cls, path):
        return Path.tail(path)

    """----------------------------------------------------------------
    """
    @classmethod
    def exists(cls, path):
        return Path.exists(path)

    """----------------------------------------------------------------
    """
    @classmethod
    def size(cls, path):
        return Path.size(path)

