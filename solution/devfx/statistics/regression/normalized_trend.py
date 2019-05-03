import numpy as np
import devfx.exceptions as exps
from ..series.dispersion import min
from ..series.dispersion import max

def normalized_trend(x, y, n_max=None):
    if(len(x) < 2):
        raise exps.ArgumentError()
    if(len(y) < 2):
        raise exps.ArgumentError()
    if (not (len(x) == len(y))):
        raise exps.ArgumentError()
    if(n_max is None):
        n_max = len(x)

    n = len(x) if(len(x) < n_max) else n_max

    x = np.asarray(x)
    x_min = min(x)
    x_max = max(x)
    x = (x[-n:] - x_min)/(x_max - x_min)

    y = np.asarray(y)
    y_min = min(y)
    y_max = max(y)
    y = (y[-n:] - y_min)/(y_max - y_min)

    w = np.linalg.lstsq(np.vstack([x, np.ones(len(x))]).T, y, rcond=None)[0]
    w = (np.arctan(w[0]), w[1])
    return w