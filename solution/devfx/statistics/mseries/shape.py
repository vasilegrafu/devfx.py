from .. import series

"""------------------------------------------------------------------------------------------------
"""
def skew(data):
    return [series.skew(data) for data in data]

"""------------------------------------------------------------------------------------------------
"""
def kurtosis(data):
    return [series.kurtosis(data) for data in data]