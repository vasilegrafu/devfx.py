from .attributes_manager import AttributesManager

class DatasetAdapter(object):
    def __init__(self, dataset):
        self.__dataset = dataset

    """----------------------------------------------------------------
    """
    @property
    def dtype(self):
       return self.__dataset.dtype

    @property
    def shape(self):
       return self.__dataset.shape

    """----------------------------------------------------------------
    """
    def resize(self, shape):
        return self.__dataset.resize(shape)

    """----------------------------------------------------------------
    """
    def __setitem__(self, key, value):
        self.__dataset[key] = value

    def __getitem__(self, key):
        return self.__dataset[key]

    """----------------------------------------------------------------
    """
    def __len__(self):
        return len(self.__dataset)

    """----------------------------------------------------------------
    """
    @property
    def attributes(self):
        return AttributesManager(self.__dataset.attrs)