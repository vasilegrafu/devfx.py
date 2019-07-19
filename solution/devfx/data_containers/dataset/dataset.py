import numpy as np
import devfx.exceptions as exceps
import devfx.reflection as refl
from .dataset_forward_iterator import DatasetForwardIterator
from .dataset_backward_iterator import DatasetBackwardIterator
from .dataset_iterator_kind import DatasetIteratorKind

class Dataset(object):
    def __init__(self, data, hparams=()):
        self.__data = [data[c] for c in range(0, len(data))]
        self.__hparams = hparams

    """----------------------------------------------------------------
    """
    def __len__(self):
       return len(self.__data[0])

    """----------------------------------------------------------------
    """
    def __getitem__(self, key):
        if(not refl.is_iterable(key) or not len(key) == 2):
            raise exceps.NotSupportedError()

        rkey = key[0]
        ckey = key[1]

        data = [self.__data[c][rkey] for c in range(0, len(self.__data))]

        if(refl.is_typeof(ckey, slice)):
            data = self.__data[ckey]
            data = self._on_getitem_data_filter(data=data, hparams=self.__hparams)
            dataset = self.__class__(data=data, hparams=self.__hparams)
            return dataset
        elif refl.is_iterable(ckey):
            data = [self.__data[c] for c in ckey]
            data = self._on_getitem_data_filter(data=data, hparams=self.__hparams)
            dataset = self.__class__(data=data, hparams=self.__hparams)
            return dataset
        elif(refl.is_typeof(ckey, int)):
            data = self.__data[ckey]
            data = self._on_getitem_data_filter(data=data, hparams=self.__hparams)
            return data
        else:
            raise exceps.NotSupportedError()

    def _on_getitem_data_filter(self, data, hparams):
        return data
    
    """----------------------------------------------------------------
    """
    def __str__(self):
        return self.__data.__str__()

    def __repr__(self):
        raise exceps.NotSupportedError()

    """----------------------------------------------------------------
    """
    def iterator(self, iterator_kind=DatasetIteratorKind.FORWARD, batch_size=None):
        if(iterator_kind == DatasetIteratorKind.FORWARD):
            return DatasetForwardIterator(dataset=self, batch_size=batch_size)
        elif(iterator_kind == DatasetIteratorKind.BACKWARD):
            return DatasetBackwardIterator(dataset=self, batch_size=batch_size)
        else:
            raise exceps.NotSupportedError()

    """----------------------------------------------------------------
    """
    def random_select(self, n):
        indexes = np.random.choice(np.arange(0, len(self)), size=n, replace=False)
        data = []
        for c in range(0, len(self.__data)):
            if(refl.is_typeof(self.__data[c], list)):
                data_c = [self.__data[c][i] for i in indexes]
            else:
                data_c = self.__data[c][indexes]
            data.append(data_c)
        dataset = self.__class__(data=data, hparams=self.__hparams)
        return dataset

    """----------------------------------------------------------------
    """
    def shuffle(self):
        indexes = np.random.choice(np.arange(0, len(self)), size=len(self), replace=False)
        data = []
        for c in range(0, len(self.__data)):
            if(refl.is_typeof(self.__data[c], list)):
                data_c = [self.__data[c][i] for i in indexes]
            else:
                data_c = self.__data[c][indexes]
            data.append(data_c)
        dataset = self.__class__(data=data, hparams=self.__hparams)
        return dataset

    """----------------------------------------------------------------
    """
    def split(self, ratios=(0.75,)):
        bounds = np.unique(np.sort(np.int32(len(self)*np.asarray(ratios))))
        splitted_datasets = []
        i = 0
        while i <= (len(bounds) - 1):
            if (i == 0):
                data = [self.__data[c][slice(None, bounds[i], None)] for c in range(0, len(self.__data))]
                dataset = self.__class__(data=data, hparams=self.__hparams)
                splitted_datasets.append(dataset)
            else:
                data = [self.__data[c][slice(bounds[i - 1], bounds[i], None)] for c in range(0, len(self.__data))]
                dataset = self.__class__(data=data, hparams=self.__hparams)
                splitted_datasets.append(dataset)
            i += 1
        data = [self.__data[c][slice(bounds[-1], None, None)] for c in range(0, len(self.__data))]
        dataset = self.__class__(data=data, hparams=self.__hparams)
        splitted_datasets.append(dataset)
        return splitted_datasets




