import devfx.exceptions as exceps

class DatasetIterator(object):
    def __init__(self, dataset, batch_size, position):
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
    def batch_size(self):
        return self.__batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        self.__batch_size = batch_size

    """----------------------------------------------------------------
    """
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    """----------------------------------------------------------------
    """
    def get_relative_position(self):
        if(self.__position < 0):
            return 0.0
        elif(self.__position > (len(self) - 1)):
            return 1.0
        else:
            return (self.__position+1)/len(self)

    """----------------------------------------------------------------
    """
    def next(self, batch_size=None):
        raise exceps.NotImplementedError()

    """----------------------------------------------------------------
    """
    def __str__(self):
        return "{batch_size} | {position}".format(batch_size=self.__batch_size, position=self.__position)

    def __repr__(self):
        raise exceps.NotSupportedError()

