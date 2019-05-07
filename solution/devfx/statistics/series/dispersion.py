import numpy as np
import pandas as pd
import devfx.reflection as refl
from .center import mean

"""------------------------------------------------------------------------------------------------
"""
def mad(data):
    if(refl.is_typeof(data, pd.Series)):
        return data.mad()
    else:
        data = np.asarray(data)
        return mean(np.abs(data-mean(data)))

"""------------------------------------------------------------------------------------------------
"""
def var(data):
    if(refl.is_typeof(data, pd.Series)):
        return data.var(ddof=1, axis=None)
    else:
        data = np.asarray(data)
        return np.var(data, ddof=1, axis=None)

def stddev(data):
    if(refl.is_typeof(data, pd.Series)):
        return data.std(ddof=1, axis=None)
    else:
        data = np.asarray(data)
        return np.std(data, ddof=1, axis=None)

"""------------------------------------------------------------------------------------------------
"""
def min(data):
    if(refl.is_typeof(data, pd.Series)):
        return data.min()
    else:
        data = np.asarray(data)
        return np.amin(data, axis=None)

def max(data):
    if(refl.is_typeof(data, pd.Series)):
        return data.max()
    else:
        data = np.asarray(data)
        return np.amax(data, axis=None)

def range(data):
    return max(data)-min(data)

"""------------------------------------------------------------------------------------------------
"""
def percentile(data, p100):
    if(refl.is_typeof(data, pd.Series)):
        return data.quantile(p100/100.0)
    else:
        data = np.asarray(data)
        return np.percentile(data, p100)

def Q1(data):
    return percentile(data, 25)

def Q2(data):
    return percentile(data, 50)

def Q3(data):
    return percentile(data, 75)

def IQR(data):
    return Q3(data)-Q1(data)


"""------------------------------------------------------------------------------------------------
"""
def outliersNx_limits(data, Nx):
    q1 = Q1(data)
    q3 = Q3(data)
    IQR = q3-q1
    lol = q1-Nx*1.5*IQR
    uol = q3+Nx*1.5*IQR
    return (lol, uol)

def is_outlierNx(data, x, Nx):
    x = np.asarray(x)
    (lol, uol) = outliersNx_limits(data, Nx)
    return ~((lol <= x) & (x <= uol))

def lolNx(data, Nx):
    (lol, uol) = outliersNx_limits(data, Nx)
    return lol

def uolNx(data, Nx):
    (lol, uol) = outliersNx_limits(data, Nx)
    return uol

"""------------------------------------------------------------------------------------------------
"""
def outliers_limits(data):
    return outliersNx_limits(data, Nx=1)

def is_outlier(data, x):
    return is_outlierNx(data, x=x, Nx=1)

def lol(data):
    (lol, uol) = outliers_limits(data)
    return lol

def uol(data):
    (lol, uol) = outliers_limits(data)
    return uol

"""------------------------------------------------------------------------------------------------
"""
def outliers2x_limits(data):
    return outliersNx_limits(data, Nx=2)

def is_outlier2x(data, x):
    return is_outlierNx(data, x=x, Nx=2)

def lol2x(data):
    (lol, uol) = outliers2x_limits(data)
    return lol

def uol2x(data):
    (lol, uol) = outliers2x_limits(data)
    return uol

"""------------------------------------------------------------------------------------------------
"""
def outliers4x_limits(data):
    return outliersNx_limits(data, Nx=4)

def is_outlier4x(data, x):
    return is_outlierNx(data, x=x, Nx=4)

def lol4x(data):
    (lol, uol) = outliers4x_limits(data)
    return lol

def uol4x(data):
    (lol, uol) = outliers4x_limits(data)
    return uol

"""------------------------------------------------------------------------------------------------
"""
def outliers8x_limits(data):
    return outliersNx_limits(data, Nx=8)

def is_outlier8x(data, x):
    return is_outlierNx(data, x=x, Nx=8)

def lol8x(data):
    (lol, uol) = outliers8x_limits(data)
    return lol

def uol8x(data):
    (lol, uol) = outliers8x_limits(data)
    return uol
