import numpy as np
import devfx.exceptions as exp
import devfx.core as core
from .. import series
from . import ops
from . import validation

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def sample(data, size=None):
    return ops.get(data, np.random.choice(ops.rows_count(data), size=size))

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_mseries('data')
def choose_one(data):
    if(ops.rows_count(data) == 0):
        raise exp.ArgumentError()
    return [_[0] for _ in sample(data, size=1)]
