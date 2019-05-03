import h5py as hdf5
import devfx.exceptions as exps
from .group_adapter import GroupAdapter

class File(GroupAdapter):
    def __init__(self, path, mode='rw'):
        if(mode == 'r'):
            mode = 'r'
        elif(mode == 'w'):
            mode = 'w'
        elif (mode == 'rw'):
            mode = 'a'
        else:
            raise exps.ArgumentError()
        self.__file = hdf5.File(name=path, mode=mode)
        super().__init__(group=self.__file)

    @classmethod
    def open(cls, path, mode='rw'):
        return File(path=path, mode=mode)

    def flush(self):
        self.__file.flush()

    def close(self):
        self.__file.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()


