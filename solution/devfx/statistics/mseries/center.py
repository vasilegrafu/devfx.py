from .. import series

"""------------------------------------------------------------------------------------------------
"""
def mean(data):
    return [series.mean(column_data) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
def median(data):
    return [series.median(column_data) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
def mode(data):
    return [series.mode(column_data) for column_data in data]