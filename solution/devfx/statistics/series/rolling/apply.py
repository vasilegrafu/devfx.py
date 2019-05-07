import pandas as pd
import devfx.reflection as refl
import devfx.exceptions as exceps

"""------------------------------------------------------------------------------------------------
"""
def rolling_apply(data, n, func, args=(), kwargs={}):
    if(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).apply(func=func, raw=True, args=args, kwargs=kwargs)
    else:
        raise exceps.ArgumentError()

