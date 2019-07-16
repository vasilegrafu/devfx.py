import numpy as np
import devfx.exceptions as exceps
import devfx.reflection as refl
from .dataset_forward_iterator import DatasetForwardIterator
from .dataset_backward_iterator import DatasetBackwardIterator
from .dataset_iterator_kind import DatasetIteratorKind

class Dataset(object):
    def __init__(self, data, iterator_kind=DatasetIteratorKind.FORWARD, hparams=()):
        self.__data = [data[c] for c in range(0, len(data))]
        self.__iterator_kind = iterator_kind
        self.__hparams = hparams

    """----------------------------------------------------------------
    """
    @property
    def data(self):
        return self.__data

    @property
    def iterator_kind(self):
        return self.__iterator_kind

    @property
    def hparams(self):
        return self.__hparams

    """----------------------------------------------------------------
    """
    def __len__(self):
       return len(self.data[0])

    """----------------------------------------------------------------
    """
    def __getitem__(self, key):
        if (refl.is_typeof(key, int)):
            data = [self.data[c] for c in range(0, len(self.data))]
            data = self._on_getitem_data_filter(data=data, hparams=self.hparams)
            data = data[key]
            return data
        elif (refl.is_typeof(key, tuple)):
            data = [self.data[c] for c in range(0, len(self.data))]
            data = self._on_getitem_data_filter(data=data,hparams=self.hparams)
            data = [data[c] for c in key]
            return data
        elif (refl.is_typeof(key, list)):
            data = []
            for c in range(0, len(self.data)):
                if (refl.is_typeof(self.data[c], list)):
                    data_c = [self.data[c][i] for i in key]
                else:
                    data_c = self.data[c][key]
                data.append(data_c)
            data = self._on_getitem_data_filter(data=data, hparams=self.hparams)
            return data
        else:
            data = [self.data[c][key] for c in range(0, len(self.data))]
            data = self._on_getitem_data_filter(data=data, hparams=self.hparams)
            return data

    def _on_getitem_data_filter(self, data, hparams):
        return data
    
    # def __str__(self):
    #     raise exceps.NotSupportedError()

    # def __repr__(self):
    #     raise exceps.NotSupportedError()

    """----------------------------------------------------------------
    """
    def iterator(self, batch_size=None):
        if(self.iterator_kind == DatasetIteratorKind.FORWARD):
            return DatasetForwardIterator(dataset=self, batch_size=batch_size)
        elif(self.iterator_kind == DatasetIteratorKind.BACKWARD):
            return DatasetBackwardIterator(dataset=self, batch_size=batch_size)
        else:
            raise exceps.NotSupportedError()

    """----------------------------------------------------------------
    """
    def random_select(self, n):
        indexes = np.random.choice(np.arange(0, len(self)), size=n, replace=False)
        data = []
        for c in range(0, len(self.data)):
            if(refl.is_typeof(self.data[c], list)):
                data_c = [self.data[c][i] for i in indexes]
            else:
                data_c = self.data[c][indexes]
            data.append(data_c)
        iterator_kind = self.iterator_kind
        dataset = self.__class__(data=data, iterator_kind=iterator_kind, hparams=self.hparams)
        return dataset

    """----------------------------------------------------------------
    """
    def shuffle(self):
        indexes = np.random.choice(np.arange(0, len(self)), size=len(self), replace=False)
        data = []
        for c in range(0, len(self.data)):
            if(refl.is_typeof(self.data[c], list)):
                data_c = [self.data[c][i] for i in indexes]
            else:
                data_c = self.data[c][indexes]
            data.append(data_c)
        iterator_kind = self.iterator_kind
        dataset = self.__class__(data=data, iterator_kind=iterator_kind, hparams=self.hparams)
        return dataset

    """----------------------------------------------------------------
    """
    def slice(self, key):
        data = [self.data[c][key] for c in range(0, len(self.data))]
        iterator_kind = self.iterator_kind
        sliced_dataset = self.__class__(data=data, iterator_kind=iterator_kind, hparams=self.hparams)
        return sliced_dataset

    """----------------------------------------------------------------
    """
    def split(self, ratios=(0.75,)):
        bounds = np.unique(np.sort(np.int32(len(self)*np.asarray(ratios))))
        splitted_datasets = []
        i = 0
        while i <= (len(bounds) - 1):
            if (i == 0):
                data = [self.data[c][slice(None, bounds[i], None)] for c in range(0, len(self.data))]
                iterator_kind = self.iterator_kind
                dataset = self.__class__(data=data, iterator_kind=iterator_kind, hparams=self.hparams)
                splitted_datasets.append(dataset)
            else:
                data = [self.data[c][slice(bounds[i - 1], bounds[i], None)] for c in range(0, len(self.data))]
                iterator_kind = self.iterator_kind
                dataset = self.__class__(data=data, iterator_kind=iterator_kind, hparams=self.hparams)
                splitted_datasets.append(dataset)
            i += 1
        data = [self.data[c][slice(bounds[-1], None, None)] for c in range(0, len(self.data))]
        iterator_kind = self.iterator_kind
        dataset = self.__class__(data=data, iterator_kind=iterator_kind, hparams=self.hparams)
        splitted_datasets.append(dataset)
        return splitted_datasets




