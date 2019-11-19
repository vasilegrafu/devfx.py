import numpy as np
from .. import series

"""------------------------------------------------------------------------------------------------
"""
def columns(data):
    return [column_data for column_data in data]

def columns_count(data):
    return len(data)


def rows_count(data):
    return len(data[0])

def rows(data):
    return [row_data for row_data in zip(*data)]

"""------------------------------------------------------------------------------------------------
"""
def get(data, indexes):
    return [series.get(column_data, indexes) for column_data in data]

"""------------------------------------------------------------------------------------------------
"""
def shuffle(data):
    return get(data, series.shuffle(range(rows_count(data))))


"""------------------------------------------------------------------------------------------------
"""
def split(data, index):
    pass