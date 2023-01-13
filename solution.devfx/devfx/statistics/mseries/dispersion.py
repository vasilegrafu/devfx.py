from .. import series
from . import validation

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def mad(data):
    return [series.mad(column_data) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def var(data):
    return [series.var(column_data) for column_data in data]

@validation.validate_args_is_mseries('data')
def stddev(data):
    return [series.stddev(column_data) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def min(data):
    return [series.min(column_data) for column_data in data]

@validation.validate_args_is_mseries('data')
def max(data):
    return [series.max(column_data) for column_data in data]

@validation.validate_args_is_mseries('data')
def range(data):
    return [series.range(column_data) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def percentile(data, p100):
    return [series.percentile(column_data, p100) for column_data in data]

@validation.validate_args_is_mseries('data')
def Q1(data):
    return [series.Q1(column_data) for column_data in data]

@validation.validate_args_is_mseries('data')
def Q2(data):
    return [series.Q2(column_data) for column_data in data]

@validation.validate_args_is_mseries('data')
def Q3(data):
    return [series.Q3(column_data) for column_data in data]

@validation.validate_args_is_mseries('data')
def IQR(data):
    return [series.IQR(column_data) for column_data in data]


"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def outliersNx_limits(data, Nx):
    return [series.outliersNx_limits(column_data, Nx) for column_data in data]

@validation.validate_args_is_mseries('data')
def is_outlierNx(data, x, Nx):
    return [series.is_outlierNx(column_data, x, Nx) for column_data in data]

@validation.validate_args_is_mseries('data')
def lolNx(data, Nx):
    return [series.lolNx(column_data, Nx) for column_data in data]

@validation.validate_args_is_mseries('data')
def uolNx(data, Nx):
    return [series.uolNx(column_data, Nx) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def outliers_limits(data):
    return [series.outliers_limits(column_data) for column_data in data]

@validation.validate_args_is_mseries('data')
def is_outlier(data, x):
    return [series.is_outlier(column_data, x) for column_data in data]

@validation.validate_args_is_mseries('data')
def lol(data):
    return [series.lol(column_data) for column_data in data]

@validation.validate_args_is_mseries('data')
def uol(data):
    return [series.uol(column_data) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def outliers2x_limits(data):
    return [series.outliers2x_limits(column_data) for column_data in data]

@validation.validate_args_is_mseries('data')
def is_outlier2x(data, x):
    return [series.is_outlier2x(column_data, x) for column_data in data]

@validation.validate_args_is_mseries('data')
def lol2x(data):
    return [series.lol2x(column_data) for column_data in data]

@validation.validate_args_is_mseries('data')
def uol2x(data):
    return [series.uol2x(column_data) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def outliers4x_limits(data):
    return [series.outliers4x_limits(column_data) for column_data in data]

@validation.validate_args_is_mseries('data')
def is_outlier4x(data, x):
    return [series.is_outlier4x(column_data, x) for column_data in data]

@validation.validate_args_is_mseries('data')
def lol4x(data):
    return [series.lol4x(column_data) for column_data in data]

@validation.validate_args_is_mseries('data')
def uol4x(data):
    return [series.uol4x(column_data) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def outliers8x_limits(data):
    return [series.outliers8x_limits(column_data) for column_data in data]

@validation.validate_args_is_mseries('data')
def is_outlier8x(data, x):
    return [series.is_outlier8x(column_data, x) for column_data in data]

@validation.validate_args_is_mseries('data')
def lol8x(data):
    return [series.lol8x(column_data) for column_data in data]

@validation.validate_args_is_mseries('data')
def uol8x(data):
    return [series.uol8x(column_data) for column_data in data]
