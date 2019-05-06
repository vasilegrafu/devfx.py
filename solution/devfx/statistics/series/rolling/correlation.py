import pandas as pd
import devfx.reflection as refl
import devfx.exceptions as exceps

"""------------------------------------------------------------------------------------------------
"""
def rolling_cov(data1, data2, n, ddof=0):
    if(refl.is_typeof(data1, pd.DataFrame) and refl.is_typeof(data2, pd.DataFrame)):
        return data1.rolling(window=n).cov(other=data2, ddof=0)
    elif(refl.is_typeof(data1, pd.Series) and refl.is_typeof(data2, pd.Series)):
        return data1.rolling(window=n).cov(other=data2, ddof=0)
    else:
        raise exceps.ArgumentError()

def rolling_corr(data1, data2, n, ddof=0):
    if(refl.is_typeof(data1, pd.DataFrame) and refl.is_typeof(data2, pd.DataFrame)):
        return data1.rolling(window=n).corr(other=data2, ddof=0)
    elif(refl.is_typeof(data1, pd.Series) and refl.is_typeof(data2, pd.Series)):
        return data1.rolling(window=n).corr(other=data2, ddof=0)
    else:
        raise exceps.ArgumentError()

