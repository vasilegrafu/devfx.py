import pandas as pd
import devfx.reflection as refl
import devfx.exceptions as exps

"""------------------------------------------------------------------------------------------------
"""
def rolling_mean(data, n):
    if(refl.is_typeof(data, pd.DataFrame)):
        return data.rolling(window=n).mean()
    elif(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).mean()
    else:
        raise exps.ArgumentError()

"""------------------------------------------------------------------------------------------------
"""
def rolling_median(data, n):
    if(refl.is_typeof(data, pd.DataFrame)):
        return data.rolling(window=n).median()
    elif(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).median()
    else:
        raise exps.ArgumentError()

