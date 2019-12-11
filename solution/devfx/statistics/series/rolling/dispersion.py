import numpy as np
import pandas as pd
import devfx.core as core

"""------------------------------------------------------------------------------------------------
"""
def rolling_min(data, n):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).min()
    else:
        data = np.asarray(data)
        return rolling_min(data=pd.Series(data), n=n).values

def rolling_max(data, n):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).max()
    else:
        data = np.asarray(data)
        return rolling_max(data=pd.Series(data), n=n).values

"""------------------------------------------------------------------------------------------------
"""
def rolling_var(data, n, ddof=0):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).var(ddof=1)
    else:
        data = np.asarray(data)
        return rolling_var(data=pd.Series(data), n=n).values

def rolling_ewvar(data, n, alpha=0.05):
    if(core.is_typeof(data, pd.Series)):
        return data.ewm(alpha=alpha).var()
    else:
        data = np.asarray(data)
        return rolling_ewvar(data=pd.Series(data), n=n).values


def rolling_stddev(data, n, ddof=0):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).std(ddof=1)
    else:
        data = np.asarray(data)
        return rolling_stddev(data=pd.Series(data), n=n).values

def rolling_ewstddev(data, n, alpha=0.05):
    if(core.is_typeof(data, pd.Series)):
        return data.ewm(alpha=alpha).std()
    else:
        data = np.asarray(data)
        return rolling_ewstddev(data=pd.Series(data), n=n).values
