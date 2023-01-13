import os
import devfx.exceptions as ex
from .directory_info import directory_info

class directory(directory_info):
    """----------------------------------------------------------------
    """
    @classmethod
    def create(cls, path):
        os.mkdir(path)

    @classmethod
    def create_if_not_exists(cls, path):
        if(not directory.exists(path)):
            directory.create(path)

    """----------------------------------------------------------------
    """
    @classmethod
    def remove(cls, path):
        os.remove(path)

    """----------------------------------------------------------------
    """
    @classmethod
    def rename(cls, from_path, to_path):
        os.rename(from_path, to_path)

    """------------------------------------------------------------------------------------------------
    """
    @classmethod
    def copy(self, from_path, to_path, overwrite=True):
        raise ex.NotImplementedError()

    """------------------------------------------------------------------------------------------------
    """
    @classmethod
    def enumerate_filepaths(cls, path, recursive=False):
        for (root, directorynames, filenames) in os.walk(path):
            for filename in filenames:
                yield os.path.join(root, filename)
            if(recursive == False):
                break

    @classmethod
    def filepaths(cls, path, recursive=False):
        return [filepath for filepath in directory.enumerate_filepaths(path=path, recursive=recursive)]


    @classmethod
    def enumerate_filenames(cls, path, recursive=False):
        for (root, directorynames, filenames) in os.walk(path):
            for filename in filenames:
                yield filename
            if(recursive == False):
                break

    @classmethod
    def filenames(cls, path, recursive=False):
        return [filename for filename in directory.enumerate_filenames(path=path, recursive=recursive)]

    """------------------------------------------------------------------------------------------------
    """
    @classmethod
    def enumerate_directorypaths(cls, path, recursive=False):
        for (root, directorynames, filenames) in os.walk(path):
            for directoryname in directorynames:
                yield os.path.join(root, directoryname)
            if(recursive == False):
                break

    @classmethod
    def directorypaths(cls, path, recursive=False):
        return [directorypath for directorypath in directory.enumerate_directorypaths(path=path, recursive=recursive)]


    @classmethod
    def enumerate_directorynames(cls, path, recursive=False):
        for (root, directorynames, filenames) in os.walk(path):
            for directoryname in directorynames:
                yield directoryname
            if(recursive == False):
                break

    @classmethod
    def directorynames(cls, path, recursive=False):
        return [directoryname for directoryname in directory.enumerate_directorynames(path=path, recursive=recursive)]