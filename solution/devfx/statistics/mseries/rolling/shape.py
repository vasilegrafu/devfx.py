from ... import series

"""------------------------------------------------------------------------------------------------
"""
def rolling_skew(data, n):
    return [series.rolling_skew(data, n) for data in data]

"""------------------------------------------------------------------------------------------------
"""
def rolling_kurtosis(data, n):
    return [series.rolling_kurtosis(data, n) for data in data]