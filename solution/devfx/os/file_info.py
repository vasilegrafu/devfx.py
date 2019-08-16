import os
import datetime as dt
from .path import path as Path

class file_info(object):
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

    """----------------------------------------------------------------
    """
    @classmethod
    def last_access_datetime(cls, path):
        return dt.datetime.fromtimestamp(os.path.getatime(path))

    @classmethod
    def last_access_date(cls, path):
        return file_info.last_access_datetime(path).date()

    @classmethod
    def last_access_time(cls, path):
        return file_info.last_access_datetime(path).time()

    @classmethod
    def last_modification_datetime(cls, path):
        return dt.datetime.fromtimestamp(os.path.getmtime(path))

    @classmethod
    def last_modification_date(cls, path):
        return file_info.last_modification_datetime(path).date()

    @classmethod
    def last_modification_time(cls, path):
        return file_info.last_modification_datetime(path).time()

