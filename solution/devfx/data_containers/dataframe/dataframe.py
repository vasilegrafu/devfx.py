import pandas as pd

"""------------------------------------------------------------------------------------------------
"""
DataFrame = pd.DataFrame

"""------------------------------------------------------------------------------------------------
"""
@classmethod
def from_objects(cls, data, columns=None, index=None):
    return pd.DataFrame.from_records(data=(_.__dict__ for _ in data), columns=columns, index=index)

DataFrame.from_objects = from_objects

"""------------------------------------------------------------------------------------------------
"""
@classmethod
def from_columns(cls, data, columns=None, index=None):
    return pd.DataFrame.from_records(data=(_ for _ in zip(*data)), columns=columns, index=index)

DataFrame.from_columns = from_columns

"""------------------------------------------------------------------------------------------------
"""
@classmethod
def from_rows(cls, data, columns=None, index=None):
    return pd.DataFrame.from_records(data=data, columns=columns, index=index)

DataFrame.from_rows = from_rows

"""------------------------------------------------------------------------------------------------
"""
@classmethod
def from_sql(cls, query, connection=None, index_columns=None):
    return pd.read_sql(sql=query, con=connection, index_col=index_columns)

DataFrame.from_sql = from_sql

"""------------------------------------------------------------------------------------------------
"""
@classmethod
def from_csv(cls, *args, **kwargs):
    return pd.read_csv(*args, **kwargs)

DataFrame.from_csv = from_csv