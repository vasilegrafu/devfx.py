import numpy as np
import pandas as pd
import scipy as sp
import scipy.stats
import devfx.core as core
from . import validation

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def mean(data):
    if(core.is_typeof(data, pd.Series)):
        return data.mean()
    else:
        data = np.asarray(data)
        return np.mean(data, axis=None)

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def median(data):
    if(core.is_typeof(data, pd.Series)):
        return data.median()
    else:
        data = np.asarray(data)
        return np.percentile(data, 50, axis=None)

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def mode(data):
    if(core.is_typeof(data, pd.Series)):
        return data.mode()
    else:
        data = np.asarray(data)
        mode = sp.stats.mode(data, axis=None)
        return (mode[0][0], mode.count[1][0])