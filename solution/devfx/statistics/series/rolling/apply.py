import numpy as np
import pandas as pd
import devfx.reflection as refl


"""------------------------------------------------------------------------------------------------
"""
def rolling_apply(data, n, func, args=(), kwargs={}):
    if(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).apply(func=func, raw=True, args=args, kwargs=kwargs)
    else:
        data = np.asarray(data)
        return rolling_apply(data=pd.Series(data), n=n, func=func, args=args, kwargs=kwargs).values

