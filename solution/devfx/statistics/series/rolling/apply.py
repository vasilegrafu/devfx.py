import pandas as pd
import devfx.reflection as refl
import devfx.exceptions as exps

"""------------------------------------------------------------------------------------------------
"""
def rolling_apply(data, n, func, args=(), kwargs={}):
    if(refl.is_typeof(data, pd.DataFrame)):
        return data.rolling(window=n).apply(func=func, raw=False, args=args, kwargs=kwargs)
    elif(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).apply(func=func, raw=False, args=args, kwargs=kwargs)
    else:
        raise exps.ArgumentError()

