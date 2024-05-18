import pandas as pd
import sqlalchemy as sa
import devfx.core as core

"""------------------------------------------------------------------------------------------------
"""
Query = sa.orm.Query

"""----------------------------------------------------------------
"""
def to_list(self):
    return self.all()

Query.to_list = to_list

"""----------------------------------------------------------------
"""
def to_dataframe(self, index_columns=None):
    index_columns2 = None
    if(index_columns is not None):
        index_columns2 = []
        for index_column in index_columns:
            if(core.is_typeof(index_column, sa.orm.attributes.InstrumentedAttribute)):
                index_columns2.append(index_column.name)
            else:
                index_columns2.append(index_column)
    return pd.read_sql(sql=self.statement, con=self.session.bind, index_col=index_columns2)

Query.to_dataframe = to_dataframe
