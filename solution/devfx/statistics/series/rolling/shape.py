import numpy as np
import pandas as pd
import devfx.reflection as refl

"""------------------------------------------------------------------------------------------------
"""
def rolling_skew(data, n):
    if(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).skew()
    else:
        data = np.asarray(data)
        return rolling_skew(data=pd.Series(data), n=n).values

"""------------------------------------------------------------------------------------------------
"""
def rolling_kurtosis(data, n):
    if(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).kurt()
    else:
        data = np.asarray(data)
        return rolling_kurtosis(data=pd.Series(data), n=n).values