import devfx.exceptions as exps

class DatasetIterator(object):
    def __init__(self, dataset, position, batch_size=None):
        self.__dataset = dataset
        self.__batch_size = batch_size
        self.__position = position

    """----------------------------------------------------------------
    """
    @property
    def dataset(self):
        return self.__dataset

    """----------------------------------------------------------------
    """
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position


    @property
    def batch_size(self):
        return self.__batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        self.__batch_size = batch_size

    """----------------------------------------------------------------
    """
    def count(self):
        return len(self.dataset)

    def __len__(self):
       return self.count()

    """----------------------------------------------------------------
    """
    def next(self, batch_size=None):
        raise exps.NotImplementedError()

    def __getitem__(self, key):
        return self.dataset[key]

    """----------------------------------------------------------------
    """
    def __str__(self):
        return "{n} | {batch_size} | {position}".format(n=len(self.__dataset), batch_size=self.__batch_size, position=self.__position)

    def __repr__(self):
        raise exps.NotSupportedError()

