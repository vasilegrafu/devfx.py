from ... import series

"""------------------------------------------------------------------------------------------------
"""
def rolling_cov(data1, data2, n):
    return [series.rolling_cov(data1, data2, n) for data in data]

def rolling_ewcov(data1, data2, n, alpha=0.05):
    return [series.rolling_ewcov(data1, data2, n) for data in data]


def rolling_corr(data1, data2, n):
    return [series.rolling_corr(data1, data2, n) for data in data]

def rolling_ewcorr(data1, data2, n, alpha=0.05):
    return [series.rolling_ewcorr(data1, data2, n) for data in data]