import pandas as pd
import devfx.reflection as refl
import devfx.exceptions as exps

"""------------------------------------------------------------------------------------------------
"""
def rolling_sum(data, n):
    if(refl.is_typeof(data, pd.DataFrame)):
        return data.rolling(window=n).sum()
    elif(refl.is_typeof(data, pd.Series)):
        return data.rolling(window=n).sum()
    else:
        raise exps.ArgumentError()

