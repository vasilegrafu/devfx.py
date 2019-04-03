import sqlalchemy as sa

"""------------------------------------------------------------------------------------------------
"""
def create_database_metadata():
    return sa.MetaData()

"""------------------------------------------------------------------------------------------------
"""
def deploy_database_metadata(database_metadata, connection_string, echo=False):
    engine = sa.create_engine(connection_string, echo=echo)
    database_metadata.create_all(bind=engine)