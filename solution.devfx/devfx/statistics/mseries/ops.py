import numpy as np
import devfx.exceptions as exp
import devfx.core as core
from .. import series
from . import validation

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def columns(data):
    return [column_data for column_data in data]

@validation.validate_args_is_mseries('data')
def columns_count(data):
    return len(data)

@validation.validate_args_is_mseries('data')
def rows_count(data):
    if(columns_count(data) == 0):
        raise exp.ArgumentError()
    return len(data[0])

@validation.validate_args_is_mseries('data')
def rows(data):
    return [row_data for row_data in zip(*data)]

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def get(data, indexes):
    return [series.get(column_data, indexes) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def shuffle(data):
    return get(data, np.random.permutation(rows_count(data)))

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def split(data, delimeter):
    if(core.is_typeof(delimeter, int)):
        return [get(data, slice(None, delimeter)), get(data, slice(delimeter, None))]
    elif(core.is_typeof(delimeter, float)):
        return [get(data, slice(None, int(delimeter*rows_count(data)))), get(data, slice(int(delimeter*rows_count(data)), None))]
    else:
        raise exp.NotSupportedError()


