from ... import series

"""------------------------------------------------------------------------------------------------
"""
def rolling_min(data, n):
    return [series.rolling_min(data, n) for data in data]

def rolling_max(data, n):
    return [series.rolling_max(data, n) for data in data]

"""------------------------------------------------------------------------------------------------
"""
def rolling_var(data, n, ddof=0):
    return [series.rolling_var(data, n, ddof) for data in data]

def rolling_ewvar(data, n, alpha=0.05):
    return [series.rolling_ewvar(data, n, alpha) for data in data]


def rolling_stddev(data, n, ddof=0):
    return [series.rolling_stddev(data, n, ddof) for data in data]

def rolling_ewstddev(data, n, alpha=0.05):
    return [series.rolling_ewstddev(data, n, alpha) for data in data]
