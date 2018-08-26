import numpy as np
from ..series import dispersion

"""------------------------------------------------------------------------------------------------
"""
def outliersNx_limits(data, Nx):
    Q1 = dispersion.Q1(data)
    Q3 = dispersion.Q3(data)
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
