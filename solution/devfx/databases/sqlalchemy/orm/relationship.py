import sqlalchemy as sa
import sqlalchemy.orm

"""------------------------------------------------------------------------------------------------
"""
relationship = sa.orm.relationship

"""------------------------------------------------------------------------------------------------
"""
def Relationship_one_to_many(target_database_entity, foreign_keys=None):
    return relationship(argument=target_database_entity, foreign_keys=foreign_keys, cascade="save-update, merge")

def Relationship_One_to_many(target_database_entity, foreign_keys=None):
    return relationship(argument=target_database_entity, foreign_keys=foreign_keys, cascade="save-update, merge, refresh-expire, expunge, delete, delete-orphan")


def Relationship_many_to_one(target_database_entity, foreign_keys=None):
    return relationship(argument=target_database_entity, foreign_keys=foreign_keys, cascade="save-update, merge")

def Relationship_many_to_One(target_database_entity, foreign_keys=None):
    return relationship(argument=target_database_entity, foreign_keys=foreign_keys, cascade="save-update, merge")


def Relationship_one_to_one(target_database_entity):
    return relationship(argument=target_database_entity, uselist=False, cascade="save-update, merge")

def Relationship_One_to_one(target_database_entity):
    return relationship(argument=target_database_entity, uselist=False, cascade="save-update, merge, refresh-expire, expunge, delete, delete-orphan")

def Relationship_one_to_One(target_database_entity):
    return relationship(argument=target_database_entity, uselist=False, cascade="save-update, merge")