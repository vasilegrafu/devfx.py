import numpy as np
import pandas as pd
import scipy as sp
import scipy.stats
import devfx.reflection as refl

"""------------------------------------------------------------------------------------------------
"""
def mean(data):
    if(refl.is_typeof(data, pd.Series)):
        return data.mean()
    else:
        data = np.asarray(data)
        return np.mean(data, axis=None)

"""------------------------------------------------------------------------------------------------
"""
def median(data):
    if(refl.is_typeof(data, pd.Series)):
        return data.median()
    else:
        data = np.asarray(data)
        return np.percentile(data, 50, axis=None)

"""------------------------------------------------------------------------------------------------
"""
def mode(data):
    if(refl.is_typeof(data, pd.Series)):
        return data.mode()
    else:
        data = np.asarray(data)
        mode = sp.stats.mode(data, axis=None)
        return (mode[0][0], mode.count[1][0])