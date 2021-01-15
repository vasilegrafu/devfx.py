import numpy as np
import pandas as pd
import devfx.core as core
from . import validation

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def sum(data):
    if(core.is_typeof(data, pd.Series)):
        return data.sum()
    else:
        return sum(data=pd.Series(data), axis=None)
