import sqlalchemy as sa
import sqlalchemy.ext.declarative

"""------------------------------------------------------------------------------------------------
"""
def create_base_entity_type():
    BaseEntity = sa.ext.declarative.declarative_base()
    return BaseEntity
