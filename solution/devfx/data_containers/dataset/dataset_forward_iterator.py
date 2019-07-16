import devfx.exceptions as exceps
from .dataset_iterator import DatasetIterator

class DatasetForwardIterator(DatasetIterator):
    def __init__(self, dataset, batch_size=None):
        super().__init__(dataset=dataset, batch_size=batch_size if(batch_size is not None) else 1, position=0)

    """----------------------------------------------------------------
    """
    def next(self, batch_size=None):
        if(batch_size is None):
            batch_size = self.batch_size 
        if(self.position > (len(self.dataset) - 1)):
            raise StopIteration()
        start = self.position
        stop = (self.position + batch_size) if((self.position + batch_size) <= (len(self.dataset) - 1)) else None
        step = 1
        data = self.dataset[start:stop:step]
        self.position = (self.position + batch_size) if((self.position + batch_size) <= (len(self.dataset) - 1)) else len(self.dataset)
        return data

