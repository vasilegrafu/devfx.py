import pandas as pd
import devfx.reflection as refl
import devfx.exceptions as exps

"""------------------------------------------------------------------------------------------------
"""
def rolling_skew(data, n):
    if(refl.is_typeof(data, pd.DataFrame)):
        return data.rolling(window=n).skew()
    elif(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).skew()
    else:
        raise exps.ArgumentError()

"""------------------------------------------------------------------------------------------------
"""
def rolling_kurtosis(data, n):
    if(refl.is_typeof(data, pd.DataFrame)):
        return data.rolling(window=n).kurt()
    elif(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).kurt()
    else:
        raise exps.ArgumentError()