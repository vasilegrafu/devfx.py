import numpy as np
import pandas as pd
import scipy as sp
import scipy.stats
import devfx.reflection as refl

"""------------------------------------------------------------------------------------------------
"""
def skew(data):
    if(refl.is_typeof(data, pd.Series)):
        return data.skew(axis=None)
    else:
        data = np.asarray(data)
        return sp.stats.skew(data, axis=None)

"""------------------------------------------------------------------------------------------------
"""
def kurtosis(data):
    if(refl.is_typeof(data, pd.Series)):
        return data.kurtosis(axis=None)
    else:
        data = np.asarray(data)
        return sp.stats.kurtosis(data, axis=None)