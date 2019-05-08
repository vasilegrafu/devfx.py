import numpy as np
import pandas as pd
import devfx.reflection as refl

"""------------------------------------------------------------------------------------------------
"""
def rolling_mean(data, n):
    if(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).mean()
    else:
        data = np.asarray(data)
        return rolling_mean(data=pd.Series(data), n=n).values

def rolling_ewmean(data, n, alpha=0.05):
    if(refl.is_typeof(data, pd.Series)):
        return data.ewm(alpha=alpha).mean()
    else:
        data = np.asarray(data)
        return rolling_expmean(data=pd.Series(data), n=n).values

"""------------------------------------------------------------------------------------------------
"""
def rolling_median(data, n):
    if(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).median()
    else:
        data = np.asarray(data)
        return rolling_median(data=pd.Series(data), n=n).values

