from .. import series
from . import validation

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def mean(data):
    return [series.mean(column_data) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def median(data):
    return [series.median(column_data) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def mode(data):
    return [series.mode(column_data) for column_data in data]