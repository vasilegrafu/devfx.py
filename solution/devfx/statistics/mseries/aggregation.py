from .. import series

"""------------------------------------------------------------------------------------------------
"""
def sum(data):
    return [series.sum(column_data) for column_data in data]
