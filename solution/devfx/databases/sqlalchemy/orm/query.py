import pandas as pd
import sqlalchemy as sa

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
def to_dataframe(self, index_col=None):
    return pd.read_sql(sql=self.statement, con=self.session.bind, index_col=index_col)

Query.to_dataframe = to_dataframe
