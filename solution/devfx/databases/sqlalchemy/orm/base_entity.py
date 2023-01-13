import sqlalchemy as sa

"""------------------------------------------------------------------------------------------------
"""
def create_base_entity_type():
    BaseEntity = sa.orm.declarative_base()
    return BaseEntity
