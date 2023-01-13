import numpy as np
import devfx.exceptions as ex

"""------------------------------------------------------------------------------------------------
"""
def normalized_trend(x, y, n_max=None):
    if(len(x) < 2):
        raise ex.ArgumentError()
    if(len(y) < 2):
        raise ex.ArgumentError()
    if (not (len(x) == len(y))):
        raise ex.ArgumentError()
    if(n_max is None):
        n_max = len(x)

    n = len(x) if(len(x) < n_max) else n_max

    x = np.asarray(x)
    x_min = np.min(x)
    x_max = np.max(x)
    x = (x[-n:] - x_min)/(x_max - x_min)

    y = np.asarray(y)
    y_min = np.min(y)
    y_max = np.max(y)
    y = (y[-n:] - y_min)/(y_max - y_min)

    w = np.linalg.lstsq(np.vstack([x, np.ones(len(x))]).T, y, rcond=None)[0]
    w = ((np.arctan(w[0]), np.arctan(w[0])*360/(2.0*np.pi)), w[1])
    return w
