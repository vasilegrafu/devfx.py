import numpy as np
import devfx.exceptions as exps

def trend(x, y, n_max=None):
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
    x = x[-n:]

    y = np.asarray(y)
    y = y[-n:]

    w = np.linalg.lstsq(np.vstack([x, np.ones(len(x))]).T, y)[0]
    w = (np.arctan(w[0]), w[1])
    return w
