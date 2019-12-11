import numpy as np
import pandas as pd
import devfx.core as core

"""------------------------------------------------------------------------------------------------
"""
def rolling_sum(data, n):
    if(core.is_typeof(data, pd.Series)):
        return data.rolling(window=n).sum()
    else:
        data = np.asarray(data)
        return rolling_sum(data=pd.Series(data), n=n).values

