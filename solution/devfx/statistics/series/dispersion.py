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

