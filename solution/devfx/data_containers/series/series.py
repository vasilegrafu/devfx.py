import pandas as pd

"""------------------------------------------------------------------------------------------------
"""
Series = pd.Series

"""------------------------------------------------------------------------------------------------
"""
@classmethod
def from_objects(cls, data, column, index=None, name=None):
    return pd.Series(data=(_.__dict__[column] for _ in data), index=(_.__dict__[index] for _ in data), name=name)

"""------------------------------------------------------------------------------------------------
"""
@classmethod
def from_sequence(cls, data, index=None, name=None):
    return pd.Series(data=data, index=index, name=name)

