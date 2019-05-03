import numpy as np
import devfx.mathematics as math
from ..series import center

"""------------------------------------------------------------------------------------------------
"""
def mad(data):
    data = np.asarray(data)
    mean = center.mean(data)
    distance = math.abs(data-mean)
    return center.mean(distance)

"""------------------------------------------------------------------------------------------------
"""
def S2(data):
    data = np.asarray(data)
    return np.var(data, ddof=1, axis=None)

def S(data):
    return math.sqrrt(S2(data))

def var(data):
    data = np.asarray(data)
    return np.var(data, ddof=0, axis=None)

def stddev(data):
    return math.sqrrt(var(data))

"""------------------------------------------------------------------------------------------------
"""
def min(data):
    data = np.asarray(data)
    return np.amin(data, axis=None)

def max(data):
    data = np.asarray(data)
    return np.amax(data, axis=None)

def range(data):
    return max(data)-min(data)

"""------------------------------------------------------------------------------------------------
"""
def percentile(data, p100):
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
    Q1 = Q1(data)
    Q3 = Q3(data)
    IQR = Q3-Q1
    lol = Q1-Nx*1.5*IQR
    uol = Q3+Nx*1.5*IQR
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
