import numpy as np
import pandas as pd
import devfx.reflection as refl

"""------------------------------------------------------------------------------------------------
"""
def rolling_cov(data1, data2, n):
    if(refl.is_typeof(data1, pd.Series) and refl.is_typeof(data2, pd.Series)):
        return data1.rolling(window=n).cov(other=data2, ddof=1)
    else:
        data1 = np.asarray(data1)
        data2 = np.asarray(data2)
        return rolling_cov(data1=pd.Series(data1), data2=pd.Series(data2), n=n).values

def rolling_ewcov(data1, data2, n, alpha=0.05):
    if(refl.is_typeof(data1, pd.Series) and refl.is_typeof(data2, pd.Series)):
        return data1.ewm(alpha=alpha).cov(other=data2)
    else:
        data1 = np.asarray(data1)
        data2 = np.asarray(data2)
        return rolling_ewcov(data1=pd.Series(data1), data2=pd.Series(data2), n=n, alpha=alpha).values


def rolling_corr(data1, data2, n):
    if(refl.is_typeof(data1, pd.Series) and refl.is_typeof(data2, pd.Series)):
        return data1.rolling(window=n).corr(other=data2, ddof=1)
    else:
        data1 = np.asarray(data1)
        data2 = np.asarray(data2)
        return rolling_corr(data1=pd.Series(data1), data2=pd.Series(data2), n=n).values

def rolling_ewcorr(data1, data2, n, alpha=0.05):
    if(refl.is_typeof(data1, pd.Series) and refl.is_typeof(data2, pd.Series)):
        return data1.ewm(alpha=alpha).corr(other=data2)
    else:
        data1 = np.asarray(data1)
        data2 = np.asarray(data2)
        return rolling_ewcorr(data1=pd.Series(data1), data2=pd.Series(data2), n=n, alpha=alpha).values