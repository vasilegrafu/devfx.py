import numpy as np
import pandas as pd
import devfx.core as core
from .. import validation

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def min(data, n):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).min()
    else:
        data = np.asarray(data)
        return min(data=pd.Series(data), n=n).values

@validation.validate_args_is_series('data')
def max(data, n):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).max()
    else:
        data = np.asarray(data)
        return max(data=pd.Series(data), n=n).values

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def var(data, n, ddof=0):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).var(ddof=1)
    else:
        data = np.asarray(data)
        return var(data=pd.Series(data), n=n).values

@validation.validate_args_is_series('data')
def ewvar(data, n, alpha=0.05):
    if(core.is_typeof(data, pd.Series)):
        return data.ewm(alpha=alpha).var()
    else:
        data = np.asarray(data)
        return ewvar(data=pd.Series(data), n=n).values

@validation.validate_args_is_series('data')
def stddev(data, n, ddof=0):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).std(ddof=1)
    else:
        data = np.asarray(data)
        return stddev(data=pd.Series(data), n=n).values

@validation.validate_args_is_series('data')
def ewstddev(data, n, alpha=0.05):
    if(core.is_typeof(data, pd.Series)):
        return data.ewm(alpha=alpha).std()
    else:
        data = np.asarray(data)
        return ewstddev(data=pd.Series(data), n=n).values
