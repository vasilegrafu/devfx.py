import numpy as np
from ..series import dispersion

"""------------------------------------------------------------------------------------------------
"""
class MinMaxScaler(object):
    def __init__(self, data=None):
        if(data is not None):
            self.fit(data)

    @property
    def min(self):
        return self.__min

    @property
    def max(self):
        return self.__max

    def fit(self, data):
        data = np.asarray(data)
        self.__min = dispersion.min(data)
        self.__max = dispersion.max(data)

    def transform(self, data):
        data = np.asarray(data)
        return (data - self.__min)/(self.__max - self.__min)

