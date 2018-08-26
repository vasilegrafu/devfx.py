import os
import devfx.exceptions as exceptions

class path(object):
    """----------------------------------------------------------------
    """
    @classmethod
    def exists(cls, path):
        exists = os.path.exists(path)
        return exists

    """----------------------------------------------------------------
    """
    @classmethod
    def current(cls):
        current = os.getcwd()
        return current

    """----------------------------------------------------------------
    """
    @classmethod
    def absolute(cls, path):
        return os.path.abspath(path)

    @classmethod
    def is_absolute(cls, path):
        return os.path.isabs(path)

    """----------------------------------------------------------------
    """
    @classmethod
    def head(cls, path):
        (head, tail) = os.path.split(path)
        return head

    @classmethod
    def tail(cls, path):
        (head, tail) = os.path.split(path)
        return tail

    """----------------------------------------------------------------
    """
    @classmethod
    def is_file(cls, path):
        is_file = os.path.isfile(path)
        return is_file

    @classmethod
    def is_directory(cls, path):
        is_directory = os.path.isdir(path)
        return is_directory

    """----------------------------------------------------------------
    """
    @classmethod
    def size(cls, path):
        if(os.path.isdir(path)):
            size = 0
            for (root, directorynames, filenames) in os.walk(path):
                for filename in filenames:
                    size += os.path.getsize(os.path.join(root, filename))
            return size
        elif os.path.isfile(path):
            size = os.path.getsize(path)
            return size
        else:
            raise exceptions.NotSupportedError()

    """----------------------------------------------------------------
    """
    @classmethod
    def join(cls, path, *paths):
        path = os.path.join(path, *paths)
        return path




