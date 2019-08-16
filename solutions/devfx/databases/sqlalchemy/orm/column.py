import sqlalchemy as sa
import sqlalchemy.orm
import datetime as dt

"""------------------------------------------------------------------------------------------------
"""
Column = sa.Column

"""------------------------------------------------------------------------------------------------
"""
def Column_as_BigInteger(default=None, nullable=False, unique=False, index=False):
    return Column(sa.types.BigInteger(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Integer(default=None, nullable=False, unique=False, index=False):
    return Column(sa.types.Integer(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_SmallInteger(default=None, nullable=False, unique=False, index=False):
    return Column(sa.types.SmallInteger(), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_FixedPointNumber(precision=None, scale=None, default=None, nullable=False, unique=False, index=False):
    return Column(sa.types.Numeric(precision=precision, scale=scale, asdecimal=True), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_FloatingPointNumber(default=None, nullable=False, unique=False, index=False):
    return Column(sa.types.Float(), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_String(length=1024, convert_unicode=True, default=None, nullable=False, unique=False, index=False):
    return Column(sa.types.String(length=length, convert_unicode=convert_unicode), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Text(convert_unicode=True, default=None, nullable=False, unique=False, index=False):
    return Column(sa.types.Text(convert_unicode=convert_unicode), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Binary(length=None, nullable=False):
    return Column(sa.types.LargeBinary(length=length), nullable=nullable)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Boolean(default=None, nullable=False):
    return Column(sa.types.Boolean(), default=default, nullable=nullable)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Enum(enum):
    return Column(sa.types.Enum(enum))

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Date(default=None, nullable=False, unique=False, index=False):
    return Column(sa.types.Date(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_DateTime(default=None, nullable=False, unique=False, index=False):
    return Column(sa.types.DateTime(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Time(default=None, nullable=False, unique=False, index=False):
    return Column(sa.types.Time(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Timedelta(default=None, nullable=False, unique=False, index=False):
    return Column(sa.types.Interval(), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_BigIntegerPrimaryKey(autoincrement=True):
    return Column(sa.types.BigInteger(), primary_key=True, autoincrement=autoincrement)

def Column_as_IntegerPrimaryKey(autoincrement=True):
    return Column(sa.types.Integer(), primary_key=True, autoincrement=autoincrement)

def Column_as_SmallIntegerPrimaryKey(autoincrement=True):
    return Column(sa.types.SmallInteger(), primary_key=True, autoincrement=autoincrement)

def Column_as_PrimaryKey(*args, **kwargs):
    return Column(primary_key=True, *args, **kwargs)


def Column_as_ForeignKey(column, nullable=False, unique=False, index=False):
    return Column(sa.schema.ForeignKey(column), nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as__BigInteger_id(autoincrement=True):
    return Column(sa.types.BigInteger(), primary_key=True, autoincrement=autoincrement)

def Column_as__Integer_id(autoincrement=True):
    return Column(sa.types.Integer(), primary_key=True, autoincrement=autoincrement)

def Column_as__SmallInteger_id(autoincrement=True):
    return Column(sa.types.SmallInteger(), primary_key=True, autoincrement=autoincrement)

def Column_as__id(*args, **kwargs):
    return Column(primary_key=True, *args, **kwargs)


def Column_as__created_on(nullable=False, unique=False, index=False):
    return Column(sa.types.DateTime(), default=lambda: dt.datetime.utcnow(), nullable=nullable, unique=unique, index=index)

def Column_as__updated_on(nullable=False, unique=False, index=False):
    return Column(sa.types.DateTime(), default=lambda: dt.datetime.utcnow(), onupdate=lambda: dt.datetime.utcnow(), nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as(primary_key=False, default=None, onupdate=None, nullable=False, unique=False, index=False, *args, **kwargs):
    return Column(primary_key=primary_key, default=default, nullable=nullable, unique=unique, index=index, *args, **kwargs)

