import pandas as pd
from ..series import series

class Dataframe(pd.DataFrame):
    """----------------------------------------------------------------
        Property Attributes 	    DataFrame
        _constructor 	            DataFrame
        _constructor_sliced 	    Series
    """
    @property
    def _constructor(self):
        return Dataframe

    @property
    def _constructor_sliced(self):
        return series.Series

    """----------------------------------------------------------------
    """
    @classmethod
    def from_objects(cls, data, columns=None, index=None):
        return pd.DataFrame.from_records(data=(_.__dict__ for _ in data), columns=columns, index=index)

    """----------------------------------------------------------------
    """
    @classmethod
    def from_columns(cls, data, columns=None, index=None):
        return pd.DataFrame.from_records(data=(_ for _ in zip(*data)), columns=columns, index=index)

    """----------------------------------------------------------------
    """
    @classmethod
    def from_rows(cls, data, columns=None, index=None):
        return pd.DataFrame.from_records(data=data, columns=columns, index=index)

