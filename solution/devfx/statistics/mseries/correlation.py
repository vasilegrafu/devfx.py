from .. import series

"""------------------------------------------------------------------------------------------------
"""
def cov(data1, data2):
    return [series.cov(column_data1, column_data2) for column_data1, column_data2 in zip(data1, data2)]

"""------------------------------------------------------------------------------------------------
"""
def corr(data1, data2):
    return [series.corr(column_data1, column_data2) for column_data1, column_data2 in zip(data1, data2)]