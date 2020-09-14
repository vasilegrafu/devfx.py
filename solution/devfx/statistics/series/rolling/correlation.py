import numpy as np
import pandas as pd
import devfx.core as core
from .. import validation

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data1', 'data2')
def cov(data1, data2, n):
    if(core.is_typeof(data1, pd.Series) and core.is_typeof(data2, pd.Series)):
        return data1.rolling(window=n).cov(other=data2, ddof=1)
    else:
        data1 = np.asarray(data1)
        data2 = np.asarray(data2)
        return cov(data1=pd.Series(data1), data2=pd.Series(data2), n=n).values

@validation.validate_args_is_series('data1', 'data2')
def ewcov(data1, data2, n, alpha=0.05):
    if(core.is_typeof(data1, pd.Series) and core.is_typeof(data2, pd.Series)):
        return data1.ewm(alpha=alpha).cov(other=data2)
    else:
        data1 = np.asarray(data1)
        data2 = np.asarray(data2)
        return ewcov(data1=pd.Series(data1), data2=pd.Series(data2), n=n, alpha=alpha).values


@validation.validate_args_is_series('data1', 'data2')
def corr(data1, data2, n):
    if(core.is_typeof(data1, pd.Series) and core.is_typeof(data2, pd.Series)):
        return data1.rolling(window=n).corr(other=data2, ddof=1)
    else:
        data1 = np.asarray(data1)
        data2 = np.asarray(data2)
        return corr(data1=pd.Series(data1), data2=pd.Series(data2), n=n).values

@validation.validate_args_is_series('data1', 'data2')
def ewcorr(data1, data2, n, alpha=0.05):
    if(core.is_typeof(data1, pd.Series) and core.is_typeof(data2, pd.Series)):
        return data1.ewm(alpha=alpha).corr(other=data2)
    else:
        data1 = np.asarray(data1)
        data2 = np.asarray(data2)
        return ewcorr(data1=pd.Series(data1), data2=pd.Series(data2), n=n, alpha=alpha).values