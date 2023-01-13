import sqlalchemy as sa

"""------------------------------------------------------------------------------------------------
"""
def create_metadata():
    return sa.MetaData()

"""------------------------------------------------------------------------------------------------
"""
def deploy_metadata(metadata, url, echo=False):
    engine = sa.create_engine(url, echo=echo)
    metadata.create_all(bind=engine)