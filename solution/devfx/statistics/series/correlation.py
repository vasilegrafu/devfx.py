import numpy as np
from ..series import dispersion

"""------------------------------------------------------------------------------------------------
"""
def cov(data1, data2):
    data1 = np.asarray(data1)
    data2 = np.asarray(data2)
    data = np.vstack((data1, data2))
    return np.cov(data, ddof=0)[0][1]

"""------------------------------------------------------------------------------------------------
"""
def corr(data1, data2):
    return cov(data1, data2)/(dispersion.stddev(data1)*dispersion.stddev(data2))
