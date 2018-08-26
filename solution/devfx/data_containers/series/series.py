import pandas as pd
from ..dataframe import dataframe

"""------------------------------------------------------------------------------------------------
"""
class Series(pd.Series):
    """----------------------------------------------------------------
        Property Attributes 	    Series
        _constructor 	            Series
        _constructor_expanddim 	    DataFrame
    """
    @property
    def _constructor(self):
        return Series

    @property
    def _constructor_expanddim(self):
        return dataframe.Dataframe

    """----------------------------------------------------------------
    """
    @classmethod
    def from_objects(cls, data, column, index=None, name=None):
        return pd.Series(data=(_.__dict__[column] for _ in data), index=(_.__dict__[index] for _ in data), name=name)

    """----------------------------------------------------------------
    """
    @classmethod
    def from_sequence(cls, data, index=None, name=None):
        return pd.Series(data=data, index=index, name=name)

