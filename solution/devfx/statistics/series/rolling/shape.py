import numpy as np
import pandas as pd
import devfx.core as core

"""------------------------------------------------------------------------------------------------
"""
def rolling_skew(data, n):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).skew()
    else:
        data = np.asarray(data)
        return rolling_skew(data=pd.Series(data), n=n).values

"""------------------------------------------------------------------------------------------------
"""
def rolling_kurtosis(data, n):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).kurt()
    else:
        data = np.asarray(data)
        return rolling_kurtosis(data=pd.Series(data), n=n).values