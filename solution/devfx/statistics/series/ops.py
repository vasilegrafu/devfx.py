import numpy as np
import pandas as pd
import devfx.reflection as refl

"""------------------------------------------------------------------------------------------------
"""
def len(data):
    return len(data)

"""------------------------------------------------------------------------------------------------
"""
def get(data, indices):
    if(refl.is_typeof(data, pd.Series)):
        return pd.Series([data[index] for index in indices]) if refl.is_iterable(indices) else data[indices]
    elif(refl.is_typeof(data, np.ndarray)):
        return np.array([data[index] for index in indices]) if refl.is_iterable(indices) else data[indices]
    else:
        return [data[index] for index in indices] if refl.is_iterable(indices) else data[indices]

"""------------------------------------------------------------------------------------------------
"""
def shuffle(data):
    return get(data, len(data))



"""------------------------------------------------------------------------------------------------
"""
def split(data, delimiter):
    pass

