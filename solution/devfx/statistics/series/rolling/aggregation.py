import numpy as np
import pandas as pd
import devfx.reflection as refl

"""------------------------------------------------------------------------------------------------
"""
def rolling_sum(data, n):
    if(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).sum()
    else:
        data = np.asarray(data)
        return rolling_sum(data=pd.Series(data), n=n).values

