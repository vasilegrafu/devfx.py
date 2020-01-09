import numpy as np
import pandas as pd
import devfx.core as core
from . import validation
from . import dispersion

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data1', 'data2')
def cov(data1, data2):
    if(core.is_typeof(data1, pd.Series) and core.is_typeof(data2, pd.Series)):
        return data1.cov(data2)
    else:
        data1 = np.asarray(data1)
        data2 = np.asarray(data2)
        data = np.vstack((data1, data2))
        return np.cov(data, ddof=1)[0][1]

"""------------------------------------------------------------------------------------------------
"""
@validation.validate_args_is_series('data1', 'data2')
def corr(data1, data2):
    return cov(data1, data2)/(dispersion.stddev(data1)*dispersion.stddev(data2))
