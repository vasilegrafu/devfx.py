from ... import series

"""------------------------------------------------------------------------------------------------
"""
def rolling_sum(data, n):
    return [series.rolling_sum(data, n) for data in data]

