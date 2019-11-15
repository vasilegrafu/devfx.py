from .. import series

"""------------------------------------------------------------------------------------------------
"""
def cov(data1, data2):
    return [series.cov(data1, data2) for data in data]

"""------------------------------------------------------------------------------------------------
"""
def corr(data1, data2):
    return [series.corr(data1, data2) for data in data]
