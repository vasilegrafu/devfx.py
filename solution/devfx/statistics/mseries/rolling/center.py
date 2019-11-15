from ... import series

"""------------------------------------------------------------------------------------------------
"""
def rolling_mean(data, n):
    return [series.rolling_mean(data, n) for data in data]

def rolling_ewmean(data, n, alpha=0.05):
    return [series.rolling_ewmean(data, n) for data in data]

"""------------------------------------------------------------------------------------------------
"""
def rolling_median(data, n):
    return [series.rolling_median(data, n) for data in data]

