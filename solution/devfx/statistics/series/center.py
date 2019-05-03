import numpy as np
import scipy as sp
import scipy.stats

"""------------------------------------------------------------------------------------------------
"""
def mean(data):
    data = np.asarray(data)
    return np.average(data, axis=None)

"""------------------------------------------------------------------------------------------------
"""
def median(data):
    data = np.asarray(data)
    return np.percentile(data, 50, axis=None)

"""------------------------------------------------------------------------------------------------
"""
def mode(data):
    data = np.asarray(data)
    mode = sp.stats.mode(data, axis=None)
    return (mode[0][0], mode.count[1][0])