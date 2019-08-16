import sqlalchemy as sa
import sqlalchemy.ext.declarative

"""------------------------------------------------------------------------------------------------
"""
def create_base_database_entity_type():
    BaseDatabaseEntity = sa.ext.declarative.declarative_base()
    return BaseDatabaseEntity
