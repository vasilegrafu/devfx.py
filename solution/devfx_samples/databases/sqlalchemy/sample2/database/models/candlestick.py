import devfx.databases.sqlalchemy as sa
from .metadata import BaseEntity

class Candlestick(BaseEntity):
    __tablename__ = "candlestick"

    id = sa.orm.Column_as__Integer_id()

    instrument_id = sa.orm.Column_as_ForeignKey("instrument.id")
    instrument = sa.orm.Relationship_many_to_One('Instrument', back_populates='candlesticks')

    granularity_id = sa.orm.Column_as_ForeignKey("granularity.id")
    granularity = sa.orm.Relationship_many_to_One('Granularity', back_populates='candlesticks')

    datetime = sa.orm.Column_as_DateTime()
    open = sa.orm.Column_as_FloatingPointNumber()
    high = sa.orm.Column_as_FloatingPointNumber()
    low = sa.orm.Column_as_FloatingPointNumber()
    close = sa.orm.Column_as_FloatingPointNumber()
    spread = sa.orm.Column_as_FloatingPointNumber()
    volume = sa.orm.Column_as_FloatingPointNumber()
    complete = sa.orm.Column_as_Boolean()

    @classmethod
    def copy(cls, source, destination, include_primary_key=False):
        if(include_primary_key):
            destination.id = source.id
        destination.instrument_id = source.instrument_id
        destination.granularity_id = source.granularity_id
        destination.datetime = source.datetime
        destination.open = source.open
        destination.close = source.close
        destination.high = source.high
        destination.low = source.low
        destination.spread = source.spread
        destination.volume = source.volume
        destination.complete = source.complete

    def copy_from(self, instance, include_primary_key=False):
        Candlestick.copy(source=instance, destination=self, include_primary_key=include_primary_key)
        return self

    def copy_to(self, instance, include_primary_key=False):
        Candlestick.copy(source=self, destination=instance, include_primary_key=include_primary_key)
        return self

sa.Index('idx_candlestick__instrument_id__granularity_id__datetime', Candlestick.instrument_id, Candlestick.granularity_id, Candlestick.datetime, unique=True)




