import h5py as hdf5
import devfx.exceptions as excps
import devfx.core as core
from .dataset_adapter import DatasetAdapter
from .attributes_adapter import AttributesAdapter

class GroupAdapter(object):
    def __init__(self, group):
        self.__group = group

    """----------------------------------------------------------------
    """
    def exists(self, path):
        return path in self.__group

    def is_group(self, path):
        if(not self.exists(path)):
            raise excps.ArgumentError()
        return core.is_typeof(self.__group[path], hdf5.Group)

    def is_dataset(self, path):
        if(not self.exists(path)):
            raise excps.ArgumentError()
        return core.is_typeof(self.__group[path], hdf5.Dataset)

    """----------------------------------------------------------------
    """
    def set(self, path, value):
        self.__group[path] = value

    def __setitem__(self, path, value):
        return self.set(path, value)

    def get(self, path):
        if(not self.exists(path)):
            raise excps.ArgumentError()
        if(self.is_group(path)):
            return GroupAdapter(self.__group[path])
        elif(self.is_dataset(path)):
            return DatasetAdapter(self.__group[path])
        else:
            raise excps.NotSupportedError()

    def __getitem__(self, path):
        return self.get(path)

    def remove(self, path):
        del self.__group[path]


    """----------------------------------------------------------------
    """
    def exists_group(self, path):
        if(not self.exists(path)):
            return False
        if(not self.is_group(path)):
            return False
        return True

    def create_group(self, path):
        return GroupAdapter(self.__group.create_group(path))

    def get_group(self, path):
        if(not self.exists(path)):
            raise excps.ArgumentError()
        if (not self.is_group(path)):
            raise excps.ArgumentError()
        return self.get(path)

    def get_or_create_group(self, path):
        if(self.exists(path)):
            return self.get_group(path)
        else:
            return self.create_group(path)

    def remove_group(self, path):
        if(not self.exists(path)):
            raise excps.ArgumentError()
        if (not self.is_group(path)):
            raise excps.ArgumentError()
        self.remove(path)

    """----------------------------------------------------------------
    """
    def exists_dataset(self, path):
        if(not self.exists(path)):
            return False
        if(not self.is_dataset(path)):
            return False
        return True

    def create_dataset(self, path, shape=None, max_shape=None, dtype=None, initial_data=None):
        return DatasetAdapter(self.__group.create_dataset(name=path, shape=shape, maxshape=max_shape, dtype=dtype, data=initial_data))

    def get_dataset(self, path):
        if(not self.exists(path)):
            raise excps.ArgumentError()
        if (not self.is_dataset(path)):
            raise excps.ArgumentError()
        return self.get(path)

    def get_or_create_dataset(self, path, shape=None, max_shape=None, dtype=None, initial_data=None):
        if(self.exists(path)):
            return self.get_dataset(path)
        else:
            return self.create_dataset(path=path, shape=shape, max_shape=max_shape, dtype=dtype, initial_data=initial_data)

    def remove_dataset(self, path):
        if(not self.exists(path)):
            raise excps.ArgumentError()
        if (not self.is_dataset(path)):
            raise excps.ArgumentError()
        self.remove(path)

    """----------------------------------------------------------------
    """
    @property
    def attributes(self):
        return AttributesAdapter(self.__group.attrs)

    """----------------------------------------------------------------
    """
    def paths(self, root='', max_depth=1):
        def paths_iterator(depth, group, root=root):
            for key in group.keys():
                item = group[key]
                path = '{}/{}'.format(root, key)
                if(isinstance(item, hdf5.Group)):
                    yield path
                    if ((depth+1) <= max_depth):
                        yield from paths_iterator(depth=(depth+1), group=item, root=path)
                elif(isinstance(item, hdf5.Dataset)):
                    yield path
                else:
                    raise excps.NotSupportedError()
        return [_ for _ in paths_iterator(depth=1, group=self.__group, root=root)]
