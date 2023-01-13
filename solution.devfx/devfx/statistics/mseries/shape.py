from .. import series
from . import validation

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def skew(data):
    return [series.skew(column_data) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def kurtosis(data):
    return [series.kurtosis(column_data) for column_data in data]