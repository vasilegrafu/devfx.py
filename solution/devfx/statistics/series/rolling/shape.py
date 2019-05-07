import pandas as pd
import devfx.reflection as refl
import devfx.exceptions as exceps

"""------------------------------------------------------------------------------------------------
"""
def rolling_skew(data, n):
    if(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).skew()
    else:
        raise exceps.ArgumentError()

"""------------------------------------------------------------------------------------------------
"""
def rolling_kurtosis(data, n):
    if(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).kurt()
    else:
        raise exceps.ArgumentError()