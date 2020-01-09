import numpy as np
import pandas as pd
import devfx.core as core
from . import validation
from . import center

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def mad(data):
    if(core.is_typeof(data, pd.Series)):
        return data.mad()
    else:
        data = np.asarray(data)
        return center.mean(np.abs(data-center.mean(data)))

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def var(data):
    if(core.is_typeof(data, pd.Series)):
        return data.var(ddof=1, axis=None)
    else:
        data = np.asarray(data)
        return np.var(data, ddof=1, axis=None)

@validation.validate_args_is_series('data')
def stddev(data):
    if(core.is_typeof(data, pd.Series)):
        return data.std(ddof=1, axis=None)
    else:
        data = np.asarray(data)
        return np.std(data, ddof=1, axis=None)

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def min(data):
    if(core.is_typeof(data, pd.Series)):
        return data.min()
    else:
        data = np.asarray(data)
        return np.amin(data, axis=None)

@validation.validate_args_is_series('data')
def max(data):
    if(core.is_typeof(data, pd.Series)):
        return data.max()
    else:
        data = np.asarray(data)
        return np.amax(data, axis=None)

@validation.validate_args_is_series('data')
def range(data):
    return max(data)-min(data)

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def percentile(data, p100):
    if(core.is_typeof(data, pd.Series)):
        return data.quantile(p100/100.0)
    else:
        data = np.asarray(data)
        return np.percentile(data, p100)

@validation.validate_args_is_series('data')
def Q1(data):
    return percentile(data, 25)

@validation.validate_args_is_series('data')
def Q2(data):
    return percentile(data, 50)

@validation.validate_args_is_series('data')
def Q3(data):
    return percentile(data, 75)

@validation.validate_args_is_series('data')
def IQR(data):
    return Q3(data)-Q1(data)


"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def outliersNx_limits(data, Nx):
    q1 = Q1(data)
    q3 = Q3(data)
    IQR = q3-q1
    lol = q1-Nx*1.5*IQR
    uol = q3+Nx*1.5*IQR
    return (lol, uol)

@validation.validate_args_is_series('data')
def is_outlierNx(data, x, Nx):
    x = np.asarray(x)
    (lol, uol) = outliersNx_limits(data, Nx)
    return ~((lol <= x) & (x <= uol))

@validation.validate_args_is_series('data')
def lolNx(data, Nx):
    (lol, uol) = outliersNx_limits(data, Nx)
    return lol

@validation.validate_args_is_series('data')
def uolNx(data, Nx):
    (lol, uol) = outliersNx_limits(data, Nx)
    return uol

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def outliers_limits(data):
    return outliersNx_limits(data, Nx=1)

@validation.validate_args_is_series('data')
def is_outlier(data, x):
    return is_outlierNx(data, x=x, Nx=1)

@validation.validate_args_is_series('data')
def lol(data):
    (lol, uol) = outliers_limits(data)
    return lol

@validation.validate_args_is_series('data')
def uol(data):
    (lol, uol) = outliers_limits(data)
    return uol

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def outliers2x_limits(data):
    return outliersNx_limits(data, Nx=2)

@validation.validate_args_is_series('data')
def is_outlier2x(data, x):
    return is_outlierNx(data, x=x, Nx=2)

@validation.validate_args_is_series('data')
def lol2x(data):
    (lol, uol) = outliers2x_limits(data)
    return lol

@validation.validate_args_is_series('data')
def uol2x(data):
    (lol, uol) = outliers2x_limits(data)
    return uol

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def outliers4x_limits(data):
    return outliersNx_limits(data, Nx=4)

@validation.validate_args_is_series('data')
def is_outlier4x(data, x):
    return is_outlierNx(data, x=x, Nx=4)

@validation.validate_args_is_series('data')
def lol4x(data):
    (lol, uol) = outliers4x_limits(data)
    return lol

@validation.validate_args_is_series('data')
def uol4x(data):
    (lol, uol) = outliers4x_limits(data)
    return uol

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def outliers8x_limits(data):
    return outliersNx_limits(data, Nx=8)

@validation.validate_args_is_series('data')
def is_outlier8x(data, x):
    return is_outlierNx(data, x=x, Nx=8)

@validation.validate_args_is_series('data')
def lol8x(data):
    (lol, uol) = outliers8x_limits(data)
    return lol

@validation.validate_args_is_series('data')
def uol8x(data):
    (lol, uol) = outliers8x_limits(data)
    return uol
