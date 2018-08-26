import numpy as np
from ..series import center
from ..series import dispersion

"""------------------------------------------------------------------------------------------------
"""
class StandardScaler(object):
    def __init__(self, data=None):
        if(data is not None):
            self.fit(data)

    @property
    def mean(self):
        return self.__mean

    @property
    def stddev(self):
        return self.__stddev

    def fit(self, data):
        data = np.asarray(data)
        self.__mean = center.mean(data)
        self.__stddev = dispersion.stddev(data)

    def transform(self, data):
        data = np.asarray(data)
        return (data - self.__mean)/self.__stddev
