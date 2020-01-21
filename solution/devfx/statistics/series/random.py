import numpy as np
import pandas as pd
import devfx.exceptions as exps
import devfx.core as core
from . import validation
from . import ops

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def sample(data, size=None):
    return ops.get(data, np.random.choice(ops.count(data), size=size))

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def choose_one(data):
    if(ops.count(data) == 0):
        raise exps.ArgumentError()
    return sample(data, size=1)[0]

@validation.validate_args_is_series('data')
def choose_one_with_probability(data, p=1.0):
    if(ops.count(data) == 0):
        raise exps.ArgumentError()
    rv = np.random.uniform(low=0.0, high=1.0, size=1)
    if(rv <= p):
        return sample(data, size=1)[0]
    else:
        return None
