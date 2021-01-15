import devfx.databases.sqlalchemy as sa
from .database_metadata import BaseDatabaseEntity

"""------------------------------------------------------------------------------------------------
"""
class Granularity(BaseDatabaseEntity):
    __tablename__ = "granularity"

    """----------------------------------------------------------------
    """
    id = sa.orm.Column_as__Integer_id()

    """----------------------------------------------------------------
    """
    candlesticks = sa.orm.Relationship_One_to_many('Candlestick', back_populates='granularity')

    """----------------------------------------------------------------
    """
    code = sa.orm.Column_as_String(length=4)

    """----------------------------------------------------------------
    """
    @classmethod
    def copy(self, source, destination, include_primary_key=False):
        if(include_primary_key):
            destination.id = source.id
        destination.code = source.code

    def copy_from(self, instance, include_primary_key=False):
        Granularity.copy(source=instance, destination=self, include_primary_key=include_primary_key)
        return self

    def copy_to(self, instance, include_primary_key=False):
        Granularity.copy(source=self, destination=instance, include_primary_key=include_primary_key)
        return self

sa.Index('idx_granularity__code', Granularity.code, unique=True)