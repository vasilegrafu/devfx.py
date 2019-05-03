import numpy as np
import devfx.exceptions as exps

"""------------------------------------------------------------------------------------------------
"""
class LabelEncoder(object):
    def __init__(self, classes=None):
        if(classes is not None):
            self.fit(classes)

    @property
    def classes(self):
        return self.__classes

    def fit(self, classes):
        if(classes is None):
            raise exps.ArgumentError()
        classes = np.asarray(classes)
        if (len(np.shape(classes)) != 1):
            raise exps.ArgumentError()

        self.__classes = np.unique(classes)

    def transform(self, data):
        if(data is None):
            raise exps.ArgumentError()
        data = np.asarray(data)
        if (len(np.shape(data)) != 1):
            raise exps.ArgumentError()
        if(len({_ for _ in data}.difference({_ for _ in self.__classes})) > 0):
            raise exps.ArgumentError()

        encoded_data = np.searchsorted(self.__classes, data)
        return encoded_data

    def inverse_transform(self, encoded_data):
        if(encoded_data is None):
            raise exps.ArgumentError()
        encoded_data = np.asarray(encoded_data)
        if (len(np.shape(encoded_data)) != 1):
            raise exps.ArgumentError()
        if(len({_ for _ in encoded_data}.difference({_ for _ in range(len(self.__classes))})) > 0):
            raise exps.ArgumentError()

        data = self.__classes[encoded_data]
        return data


# label_encoder = LabelEncoder(['a', 'a', 'b', 2])
# print(label_encoder.classes)
#
# x = label_encoder.transform(['b', 'a', 2])
# print(x)
# x = label_encoder.transform(['a'])
# print(x)
#
# x = label_encoder.inverse_transform([0])
# print(x)