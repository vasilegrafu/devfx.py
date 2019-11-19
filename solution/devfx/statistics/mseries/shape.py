from .. import series

"""------------------------------------------------------------------------------------------------
"""
def skew(data):
    return [series.skew(column_data) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
def kurtosis(data):
    return [series.kurtosis(column_data) for column_data in data]