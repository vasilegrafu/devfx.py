import numpy as np
import pandas as pd
import scipy as sp
import scipy.stats
import devfx.core as core
from . import validation

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def skew(data):
    if(core.is_typeof(data, pd.Series)):
        return data.skew(axis=None)
    else:
        data = np.asarray(data)
        return sp.stats.skew(data, axis=None)

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def kurtosis(data):
    if(core.is_typeof(data, pd.Series)):
        return data.kurtosis(axis=None)
    else:
        data = np.asarray(data)
        return sp.stats.kurtosis(data, axis=None)
        