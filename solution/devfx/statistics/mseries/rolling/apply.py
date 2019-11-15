from ... import series

"""------------------------------------------------------------------------------------------------
"""
def rolling_apply(data, n, func, args=(), kwargs={}):
    return [series.rolling_apply(data, n, func, args, kwargs) for data in data]

