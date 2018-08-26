import sqlalchemy as sa
import sqlalchemy.orm

"""------------------------------------------------------------------------------------------------
"""
def Relationship_one_to_many(target_database_entity, owned=True, foreign_keys=None):
    if(owned == True):
        return sa.orm.relationship(argument=target_database_entity, foreign_keys=foreign_keys, cascade="save-update, refresh-expire, expunge, delete, delete-orphan")
    else:
        return sa.orm.relationship(argument=target_database_entity, foreign_keys=foreign_keys, cascade="save-update")

def Relationship_many_to_one(target_database_entity, foreign_keys=None):
    return sa.orm.relationship(argument=target_database_entity, foreign_keys=foreign_keys, cascade="save-update")

def Relationship_one_to_one(target_database_entity, owned=True):
    if (owned == True):
        return sa.orm.relationship(argument=target_database_entity, uselist=False, cascade="save-update, refresh-expire, expunge, delete")
    else:
        return sa.orm.relationship(argument=target_database_entity, uselist=False, cascade="save-update")