import sqlalchemy as sa

"""------------------------------------------------------------------------------------------------
"""
def deploy_database_metadata(base_database_entity_type, connection_string, echo=False):
    engine = sa.create_engine(connection_string, echo=echo)
    base_database_entity_type.metadata.create_all(bind=engine)