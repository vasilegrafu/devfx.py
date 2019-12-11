import numpy as np
import devfx.exceptions as exceps
import devfx.core as core
from .. import series

"""------------------------------------------------------------------------------------------------
"""
def columns(data):
    return [column_data for column_data in data]

def columns_count(data):
    return len(data)

def rows_count(data):
    return len(data[0])

def rows(data):
    return [row_data for row_data in zip(*data)]

"""------------------------------------------------------------------------------------------------
"""
def get(data, indexes):
    return [series.get(column_data, indexes) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
def sample(data, size=None):
    return get(data, np.random.choice(rows_count(data), size=size))

def shuffle(data):
    return get(data, np.random.permutation(rows_count(data)))

"""------------------------------------------------------------------------------------------------
"""
def split(data, delimeter):
    if(core.is_typeof(delimeter, int)):
        return [get(data, slice(None, delimeter)), get(data, slice(delimeter, None))]
    elif(core.is_typeof(delimeter, float)):
        return [get(data, slice(None, int(delimeter*rows_count(data)))), get(data, slice(int(delimeter*rows_count(data)), None))]
    else:
        raise exceps.NotSupportedError()


