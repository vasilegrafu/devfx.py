import numpy as np
import pandas as pd
import devfx.reflection as refl
import devfx.exceptions as exceps
from .apply import rolling_apply

"""------------------------------------------------------------------------------------------------
"""
def rolling_mean(data, n):
    if(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).mean()
    else:
        raise exceps.ArgumentError()

# def rolling_expmean(data, n, alpha=0.05):
#     if(refl.is_typeof(data, pd.DataFrame)):
#         return data.ewm(alpha=alpha).mean()
#     elif(refl.is_typeof(data, pd.Series)):
#         return data.ewm(alpha=alpha).mean()
#     else:
#         raise exceps.ArgumentError()

def rolling_expmean(data, n, alpha=0.05):
    def func(data, alpha):
        return np.average(data, weights=np.power((1.0-alpha), np.arange(1, len(data)+1)))

    return rolling_apply(data=data, n=n, func=func, args=(alpha, ), kwargs={})

"""------------------------------------------------------------------------------------------------
"""
def rolling_median(data, n):
    if(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).median()
    else:
        raise exceps.ArgumentError()

