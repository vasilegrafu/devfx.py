import sqlalchemy as sa
import sqlalchemy.orm
import datetime as dt

"""------------------------------------------------------------------------------------------------
"""
def Column_as_BigInteger(default=None, nullable=False, unique=False, index=False):
    return sa.Column(sa.BigInteger(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Integer(default=None, nullable=False, unique=False, index=False):
    return sa.Column(sa.Integer(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_SmallInteger(default=None, nullable=False, unique=False, index=False):
    return sa.Column(sa.SmallInteger(), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_FixedPointNumber(precision=None, scale=None, default=None, nullable=False, unique=False, index=False):
    return sa.Column(sa.Numeric(precision=precision, scale=scale, asdecimal=True), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_FloatingPointNumber(default=None, nullable=False, unique=False, index=False):
    return sa.Column(sa.Float(), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_String(length=None, default=None, nullable=False, unique=False, index=False):
    return sa.Column(sa.String(length), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_UnicodeString(length=None, default=None, nullable=False, unique=False, index=False):
    return sa.Column(sa.Unicode(length), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Text(default=None, nullable=False, unique=False, index=False):
    return sa.Column(sa.Text(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_UnicodeText(default=None, nullable=False, unique=False, index=False):
    return sa.Column(sa.UnicodeText(), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Binary(nullable=False):
    return sa.Column(sa.LargeBinary(), nullable=nullable)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Boolean(default=None, nullable=False):
    return sa.Column(sa.Boolean(), default=default, nullable=nullable)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Enum(enum):
    return sa.Column(sa.Enum(enum))

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Date(default=None, nullable=False, unique=False, index=False):
    return sa.Column(sa.Date(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_DateTime(default=None, nullable=False, unique=False, index=False):
    return sa.Column(sa.DateTime(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Time(default=None, nullable=False, unique=False, index=False):
    return sa.Column(sa.Time(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Timedelta(default=None, nullable=False, unique=False, index=False):
    return sa.Column(sa.Interval(), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_PrimaryKey(autoincrement=True):
    return sa.Column(sa.Integer(), primary_key=True, autoincrement=autoincrement)

def Column_as_ForeignKey(column, nullable=False, unique=False, index=False):
    return sa.Column(sa.ForeignKey(column), nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as__id(autoincrement=True):
    return sa.Column(sa.Integer(), primary_key=True, autoincrement=autoincrement)

def Column_as__created_on(nullable=False, unique=False, index=False):
    return sa.Column(sa.DateTime(), default=dt.datetime.utcnow(), nullable=nullable, unique=unique, index=index)

def Column_as__updated_on(nullable=False, unique=False, index=False):
    return sa.Column(sa.DateTime(), default=dt.datetime.utcnow(), onupdate=lambda: dt.datetime.utcnow(), nullable=nullable, unique=unique, index=index)