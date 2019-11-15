from .. import series

"""------------------------------------------------------------------------------------------------
"""
def mean(data):
    return [series.mean(data) for data in data]

"""------------------------------------------------------------------------------------------------
"""
def median(data):
    return [series.median(data) for data in data]

"""------------------------------------------------------------------------------------------------
"""
def mode(data):
    return [series.mode(data) for data in data]