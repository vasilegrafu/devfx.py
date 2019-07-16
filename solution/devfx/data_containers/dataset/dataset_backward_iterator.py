from .dataset_iterator import DatasetIterator

class DatasetBackwardIterator(DatasetIterator):
    def __init__(self, dataset, batch_size=None):
        super().__init__(dataset=dataset, batch_size=batch_size if(batch_size is not None) else -1, position=len(dataset)-1)

    """----------------------------------------------------------------
    """
    def next(self, batch_size=None):
        if(batch_size is None):
            batch_size = self.batch_size 
        if(self.position < 0):
            raise StopIteration()
        start = self.position
        stop = (self.position - batch_size) if((self.position - batch_size) >= 0) else None
        step = -1
        data = self.dataset[start:stop:step]
        self.position = (self.position - batch_size) if((self.position - batch_size) >= 0) else -1
        return data


