from .. import series

"""------------------------------------------------------------------------------------------------
"""
def mad(data):
    return [series.mad(data) for data in data]

"""------------------------------------------------------------------------------------------------
"""
def var(data):
    return [series.var(data) for data in data]

def stddev(data):
    return [series.stddev(data) for data in data]

"""------------------------------------------------------------------------------------------------
"""
def min(data):
    return [series.min(data) for data in data]

def max(data):
    return [series.max(data) for data in data]

def range(data):
    return [series.range(data) for data in data]

"""------------------------------------------------------------------------------------------------
"""
def percentile(data, p100):
    return [series.percentile(data, p100) for data in data]

def Q1(data):
    return [series.Q1(data) for data in data]

def Q2(data):
    return [series.Q2(data) for data in data]

def Q3(data):
    return [series.Q3(data) for data in data]

def IQR(data):
    return [series.IQR(data) for data in data]


"""------------------------------------------------------------------------------------------------
"""
def outliersNx_limits(data, Nx):
    return [series.outliersNx_limits(data, Nx) for data in data]

def is_outlierNx(data, x, Nx):
    return [series.is_outlierNx(data, x, Nx) for data in data]

def lolNx(data, Nx):
    return [series.lolNx(data, Nx) for data in data]

def uolNx(data, Nx):
    return [series.uolNx(data, Nx) for data in data]

"""------------------------------------------------------------------------------------------------
"""
def outliers_limits(data):
    return [series.outliers_limits(data) for data in data]

def is_outlier(data, x):
    return [series.is_outlier(data, x) for data in data]

def lol(data):
    return [series.lol(data) for data in data]

def uol(data):
    return [series.uol(data) for data in data]

"""------------------------------------------------------------------------------------------------
"""
def outliers2x_limits(data):
    return [series.outliers2x_limits(data) for data in data]

def is_outlier2x(data, x):
    return [series.is_outlier2x(data, x) for data in data]

def lol2x(data):
    return [series.lol2x(data) for data in data]

def uol2x(data):
    return [series.uol2x(data) for data in data]

"""------------------------------------------------------------------------------------------------
"""
def outliers4x_limits(data):
    return [series.outliers4x_limits(data) for data in data]

def is_outlier4x(data, x):
    return [series.is_outlier4x(data, x) for data in data]

def lol4x(data):
    return [series.lol4x(data) for data in data]

def uol4x(data):
    return [series.uol4x(data) for data in data]

"""------------------------------------------------------------------------------------------------
"""
def outliers8x_limits(data):
    return [series.outliers8x_limits(data) for data in data]

def is_outlier8x(data, x):
    return [series.is_outlier8x(data, x) for data in data]

def lol8x(data):
    return [series.lol8x(data) for data in data]

def uol8x(data):
    return [series.uol8x(data) for data in data]
