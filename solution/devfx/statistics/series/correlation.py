import numpy as np
import pandas as pd
import devfx.reflection as refl
from .dispersion import stddev

"""------------------------------------------------------------------------------------------------
"""
def cov(data1, data2):
    if(refl.is_typeof(data1, pd.Series) and refl.is_typeof(data2, pd.Series)):
        return data1.cov(data2)
    else:
        data1 = np.asarray(data1)
        data2 = np.asarray(data2)
        data = np.vstack((data1, data2))
        return np.cov(data, ddof=1)[0][1]

"""------------------------------------------------------------------------------------------------
"""
def corr(data1, data2):
    return cov(data1, data2)/(stddev(data1)*stddev(data2))
