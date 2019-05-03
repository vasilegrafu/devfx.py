import numpy as np
import scipy as sp
import scipy.stats

"""------------------------------------------------------------------------------------------------
"""
def skew(data):
    data = np.asarray(data)
    return sp.stats.skew(data)

"""------------------------------------------------------------------------------------------------
"""
def kurtosis(data):
    data = np.asarray(data)
    return sp.stats.kurtosis(data)