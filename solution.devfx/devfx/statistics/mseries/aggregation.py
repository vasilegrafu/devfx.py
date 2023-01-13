from .. import series
from . import validation

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def sum(data):
    return [series.sum(column_data) for column_data in data]
