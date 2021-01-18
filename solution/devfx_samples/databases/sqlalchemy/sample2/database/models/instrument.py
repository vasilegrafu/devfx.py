import devfx.databases.sqlalchemy as sa
from .metadata import BaseEntity

class Instrument(BaseEntity):
    __tablename__ = "instrument"

    id = sa.orm.Column_as__Integer_id()

    candlesticks = sa.orm.Relationship_One_to_many('Candlestick', back_populates='instrument')

    code = sa.orm.Column_as_String(length=16)
    name = sa.orm.Column_as_String(length=64, nullable=True)

    @classmethod
    def copy(self, source, destination, include_primary_key=False):
        if(include_primary_key):
            destination.id = source.id
        destination.code = source.code
        destination.name = source.name

    def copy_from(self, instance, include_primary_key=False):
        Instrument.copy(source=instance, destination=self, include_primary_key=include_primary_key)
        return self

    def copy_to(self, instance, include_primary_key=False):
        Instrument.copy(source=self, destination=instance, include_primary_key=include_primary_key)
        return self

sa.Index('idx_instrument__code', Instrument.code, unique=True)