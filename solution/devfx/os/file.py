import os
import devfx.exceptions as exceptions
from .file_info import file_info
from .directory import directory

class file(file_info):
    """----------------------------------------------------------------
    """
    @classmethod
    def create(cls, path):
        file.write_bytes(path, b'')

    @classmethod
    def create_if_not_exists(cls, path):
        if(not file.exists(path)):
            file.write_bytes(path, b'')

    @classmethod
    def creates(cls, path):
        file.writes_bytes(path, b'')

    @classmethod
    def creates_if_not_exists(cls, path):
        if(not file.exists(path)):
            file.writes_bytes(path, b'')

    """----------------------------------------------------------------
    """
    @classmethod
    def remove(cls, path):
        os.remove(path)

    @classmethod
    def removes(cls, path):
        os.removedirs(path)

    """----------------------------------------------------------------
    """
    @classmethod
    def rename(cls, from_path, to_path):
        os.rename(from_path, to_path)

    @classmethod
    def renames(cls, from_path, to_path):
        os.renames(from_path, to_path)

    """----------------------------------------------------------------
    """
    @classmethod
    def copy(self, from_path, to_path, overwrite=True):
        raise exceptions.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """
    @classmethod
    def read_text(cls, path, encoding=None, readlines=False):
        with open(file=path, mode='rt', encoding=encoding) as f:
            if(not readlines):
                content = f.read()
            else:
                content = f.readlines()
            return content

    @classmethod
    def write_text(cls, path, text, encoding=None):
        with open(file=path, mode='wt', encoding=encoding) as f:
            f.write(text)

    @classmethod
    def writes_text(cls, path, text, encoding=None):
        directory.creates_if_not_exists(file.parent_directorypath(path))
        with open(file=path, mode='wt', encoding=encoding) as f:
            f.write(text)

    """------------------------------------------------------------------------------------------------
    """
    @classmethod
    def read_bytes(cls, path):
        with open(file=path, mode='rb') as f:
            content = f.read()
            return content

    @classmethod
    def write_bytes(cls, path, bytes):
        with open(file=path, mode='wb') as f:
            f.write(bytes)

    @classmethod
    def writes_bytes(cls, path, bytes):
        directory.creates_if_not_exists(file.parent_directorypath(path))
        with open(file=path, mode='wb') as f:
            f.write(bytes)