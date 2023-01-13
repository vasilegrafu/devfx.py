import numpy as np
import pandas as pd
import devfx.core as core
from .. import validation

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def skew(data, n):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).skew()
    else:
        data = np.asarray(data)
        return skew(data=pd.Series(data), n=n).values

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def kurtosis(data, n):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).kurt()
    else:
        data = np.asarray(data)
        return kurtosis(data=pd.Series(data), n=n).values