import pandas as pd
import devfx.reflection as refl
import devfx.exceptions as exps

"""------------------------------------------------------------------------------------------------
"""
def rolling_min(data, n):
    if(refl.is_typeof(data, pd.DataFrame)):
        return data.rolling(window=n).min()
    elif(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).min()
    else:
        raise exps.ArgumentError()

def rolling_max(data, n):
    if(refl.is_typeof(data, pd.DataFrame)):
        return data.rolling(window=n).max()
    elif(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).max()
    else:
        raise exps.ArgumentError()

"""------------------------------------------------------------------------------------------------
"""
def rolling_var(data, n, ddof=0):
    if(refl.is_typeof(data, pd.DataFrame)):
        return data.rolling(window=n).var(ddof=0)
    elif(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).var(ddof=0)
    else:
        raise exps.ArgumentError()

def rolling_stddev(data, n, ddof=0):
    if(refl.is_typeof(data, pd.DataFrame)):
        return data.rolling(window=n).std(ddof=0)
    elif(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).std(ddof=0)
    else:
        raise exps.ArgumentError()
