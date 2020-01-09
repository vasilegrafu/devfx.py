import numpy as np
import pandas as pd
import devfx.exceptions as exceps
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
        raise exceps.ArgumentError()
    return sample(data, size=1)[0]
