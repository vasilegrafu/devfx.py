import numpy as np
import pandas as pd
import devfx.reflection as refl

"""------------------------------------------------------------------------------------------------
"""
def sum(data):
    if(refl.is_typeof(data, pd.Series)):
        return data.sum()
    else:
        data = np.asarray(data)
        return np.sum(data, axis=None)
