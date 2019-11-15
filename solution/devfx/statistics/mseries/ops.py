import numpy as np
from .. import series

"""------------------------------------------------------------------------------------------------
"""
def get(data, indexes):
    return [series.get(data, indexes) for data in data]

"""------------------------------------------------------------------------------------------------
"""
def shuffle(data):
    return get(data, series.shuffle(range(len(data[0]))))


