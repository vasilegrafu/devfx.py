import numpy as np
import pandas as pd
import devfx.core as core
from .. import validation

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data')
def sum(data, n):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).sum()
    else:
        data = np.asarray(data)
        return sum(data=pd.Series(data), n=n).values

