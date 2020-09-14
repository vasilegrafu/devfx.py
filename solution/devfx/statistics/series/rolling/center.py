import numpy as np
import pandas as pd
import devfx.core as core
from .. import validation

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def mean(data, n):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).mean()
    else:
        data = np.asarray(data)
        return mean(data=pd.Series(data), n=n).values

@validation.validate_args_is_series('data')
def ewmean(data, n, alpha=0.05):
    if(core.is_typeof(data, pd.Series)):
        return data.ewm(alpha=alpha).mean()
    else:
        data = np.asarray(data)
        return ewmean(data=pd.Series(data), n=n).values

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def median(data, n):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).median()
    else:
        data = np.asarray(data)
        return median(data=pd.Series(data), n=n).values

