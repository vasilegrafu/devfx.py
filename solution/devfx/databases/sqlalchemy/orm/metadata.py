import sqlalchemy as sa

"""------------------------------------------------------------------------------------------------
"""
def deploy_metadata(base_entity_type, database_url, echo=False):
    engine = sa.create_engine(database_url, echo=echo)
    base_entity_type.metadata.create_all(bind=engine)