import numpy as np
import devfx.exceptions as exceptions
from .one_hot import one_hot

"""------------------------------------------------------------------------------------------------
"""
class LabelBinarizer(object):
    def __init__(self, data=None):
        if(data is not None):
            self.fit(data)

    @property
    def classes(self):
        return self.__classes

    def fit(self, classes):
        if(classes is None):
            raise exceptions.ArgumentError()
        classes = np.asarray(classes)
        if(len(np.shape(classes)) != 1):
            raise exceptions.ArgumentError()

        self.__classes = np.unique(classes)

    def transform(self, data):
        if(data is None):
            raise exceptions.ArgumentError()
        data = np.asarray(data)
        if(len(np.shape(data)) != 1):
            raise exceptions.ArgumentError()
        if(len({_ for _ in data}.difference({_ for _ in self.__classes})) > 0):
            raise exceptions.ArgumentError()

        n = len(self.__classes)
        binarized_data = np.array([one_hot(n, np.argwhere(self.__classes == _)) for _ in data])
        return binarized_data

    def inverse_transform(self, binarized_data):
        if(binarized_data is None):
            raise exceptions.ArgumentError()
        binarized_data = np.asarray(binarized_data)
        if(len(np.shape(binarized_data)) != 2):
            raise exceptions.ArgumentError()
        if(np.shape(binarized_data)[1] != len(self.__classes)):
            raise exceptions.ArgumentError()

        classes = np.array([self.__classes[np.argmax(_)] for _ in binarized_data])
        return classes


# label_binarizer = LabelBinarizer(['a', 'a', 'b', 2])
# print(label_binarizer.classes)
#
# x = label_binarizer.transform(['b', 2, 'a'])
# print(x)
# x = label_binarizer.transform(['a'])
# print(x)
#
# x = label_binarizer.inverse_transform([[0, 1, 0], [0, 0, 1]])
# print(x)