import numpy as np

"""------------------------------------------------------------------------------------------------
"""
class Normalizer(object):
    def __init__(self):
        pass

    def transform(self, data):
        data = np.asarray(data)
        return data/np.sqrt(np.sum(np.square(data)))

