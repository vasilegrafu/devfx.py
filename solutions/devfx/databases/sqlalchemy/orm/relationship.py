import sqlalchemy as sa
import sqlalchemy.orm

"""------------------------------------------------------------------------------------------------
"""
relationship = sa.orm.relationship

"""------------------------------------------------------------------------------------------------
"""
def Relationship_one_to_many(target_database_entity, back_populates=None, foreign_keys=None, *args, **kwargs):
    return relationship(argument=target_database_entity, back_populates=back_populates, cascade="save-update, merge", foreign_keys=foreign_keys, *args, **kwargs)

def Relationship_One_to_many(target_database_entity, back_populates=None, foreign_keys=None, *args, **kwargs):
    return relationship(argument=target_database_entity, back_populates=back_populates, cascade="save-update, merge, refresh-expire, expunge, delete, delete-orphan", foreign_keys=foreign_keys, *args, **kwargs)


def Relationship_many_to_one(target_database_entity, back_populates=None, foreign_keys=None, *args, **kwargs):
    return relationship(argument=target_database_entity, back_populates=back_populates, cascade="save-update, merge", foreign_keys=foreign_keys, *args, **kwargs)

def Relationship_many_to_One(target_database_entity, back_populates=None, foreign_keys=None, *args, **kwargs):
    return relationship(argument=target_database_entity, back_populates=back_populates, cascade="save-update, merge", foreign_keys=foreign_keys, *args, **kwargs)


def Relationship_one_to_one(target_database_entity, back_populates=None, foreign_keys=None, *args, **kwargs):
    return relationship(argument=target_database_entity, back_populates=back_populates, uselist=False, cascade="save-update, merge", foreign_keys=foreign_keys, *args, **kwargs)

def Relationship_One_to_one(target_database_entity, back_populates=None, foreign_keys=None, *args, **kwargs):
    return relationship(argument=target_database_entity, back_populates=back_populates, uselist=False, cascade="save-update, merge, refresh-expire, expunge, delete, delete-orphan", foreign_keys=foreign_keys, *args, **kwargs)

def Relationship_one_to_One(target_database_entity, back_populates=None, foreign_keys=None, *args, **kwargs):
    return relationship(argument=target_database_entity, back_populates=back_populates, uselist=False, cascade="save-update, merge", foreign_keys=foreign_keys, *args, **kwargs)