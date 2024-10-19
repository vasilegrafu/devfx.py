import numpy as np
import pandas as pd
import devfx.exceptions as exp
import devfx.core as core
from . import validation

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def count(data):
    return len(data)

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def get(data, indices):
    if(core.is_typeof(data, pd.Series)):
        return pd.Series([data[index] for index in indices]) if core.is_iterable(indices) else data[indices]
    elif(core.is_typeof(data, np.ndarray)):
        return np.array([data[index] for index in indices]) if core.is_iterable(indices) else data[indices]
    else:
        return [data[index] for index in indices] if core.is_iterable(indices) else data[indices]

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def shuffle(data):
    return get(data, np.random.permutation(count(data)))

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def split(data, delimeter):
    if(core.is_typeof(delimeter, int)):
        return [get(data, slice(None, delimeter)), get(data, slice(delimeter, None))]
    elif(core.is_typeof(delimeter, float)):
        return [get(data, slice(None, int(delimeter*count(data)))), get(data, slice(int(delimeter*count(data)), None))]
    else:
        raise exp.NotSupportedError()