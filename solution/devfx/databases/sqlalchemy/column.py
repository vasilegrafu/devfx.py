import sqlalchemy as sa
import datetime as dt

"""------------------------------------------------------------------------------------------------
"""
def Column_as_BigInteger(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.types.BigInteger(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Integer(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.types.Integer(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_SmallInteger(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.types.SmallInteger(), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_FixedPointNumber(name, precision=None, scale=None, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.types.Numeric(precision=precision, scale=scale, asdecimal=True), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_FloatingPointNumber(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.types.Float(), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_String(name, length=1024, convert_unicode=True, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.types.String(length=length, convert_unicode=convert_unicode), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Text(name, convert_unicode=True, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.types.Text(convert_unicode=convert_unicode), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Binary(name, length=None, nullable=False):
    return sa.Column(name, sa.types.LargeBinary(length=length), nullable=nullable)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Boolean(name, default=None, nullable=False):
    return sa.Column(name, sa.types.Boolean(), default=default, nullable=nullable)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Enum(name, enum):
    return sa.Column(name, sa.types.Enum(enum))

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Date(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.types.Date(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_DateTime(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.types.DateTime(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Time(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.types.Time(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Timedelta(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.types.Interval(), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_BigIntegerPrimaryKey(name, autoincrement=True):
    return sa.Column(name, sa.types.BigInteger(), primary_key=True, autoincrement=autoincrement)

def Column_as_IntegerPrimaryKey(name, autoincrement=True):
    return sa.Column(name, sa.types.Integer(), primary_key=True, autoincrement=autoincrement)

def Column_as_SmallIntegerPrimaryKey(name, autoincrement=True):
    return sa.Column(name, sa.types.SmallInteger(), primary_key=True, autoincrement=autoincrement)

def Column_as_PrimaryKey(name, *args, **kwargs):
    return sa.Column(name, primary_key=True, *args, **kwargs)


def Column_as_ForeignKey(name, column, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.schema.ForeignKey(column), nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as__BigInteger_id(autoincrement=True):
    return sa.Column('id', sa.types.BigInteger(), primary_key=True, autoincrement=autoincrement)

def Column_as__Integer_id(autoincrement=True):
    return sa.Column('id', sa.types.Integer(), primary_key=True, autoincrement=autoincrement)

def Column_as__SmallInteger_id(autoincrement=True):
    return sa.Column('id', sa.types.SmallInteger(), primary_key=True, autoincrement=autoincrement)

def Column_as__id(*args, **kwargs):
    return sa.Column('id', primary_key=True, *args, **kwargs)


def Column_as__created_on(nullable=False, unique=False, index=False):
    return sa.Column('created_on', sa.types.DateTime(), default=lambda: dt.datetime.utcnow(), nullable=nullable, unique=unique, index=index)

def Column_as__updated_on(nullable=False, unique=False, index=False):
    return sa.Column('updated_on', sa.types.DateTime(), default=lambda: dt.datetime.utcnow(), onupdate=lambda: dt.datetime.utcnow(), nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as(name, primary_key=False, default=None, onupdate=None, nullable=False, unique=False, index=False, *args, **kwargs):
    return sa.Column(name, primary_key=primary_key, default=default, nullable=nullable, unique=unique, index=index, *args, **kwargs)

