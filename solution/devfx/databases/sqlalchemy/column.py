import sqlalchemy as sa
import datetime as dt

"""------------------------------------------------------------------------------------------------
"""
def Column_as_BigInteger(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.BigInteger(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Integer(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.Integer(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_SmallInteger(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.SmallInteger(), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_FixedPointNumber(name, precision=None, scale=None, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.Numeric(precision=precision, scale=scale, asdecimal=True), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_FloatingPointNumber(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.Float(), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_String(name, length=1024, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.String(length), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_UnicodeString(name, length=1024, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.Unicode(length), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Text(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.Text(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_UnicodeText(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.UnicodeText(), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Binary(name, nullable=False):
    return sa.Column(name, sa.LargeBinary(), nullable=nullable)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Boolean(name, default=None, nullable=False):
    return sa.Column(name, sa.Boolean(), default=default, nullable=nullable)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Enum(name, enum):
    return sa.Column(name, sa.Enum(enum))

"""------------------------------------------------------------------------------------------------
"""
def Column_as_Date(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.Date(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_DateTime(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.DateTime(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Time(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.Time(), default=default, nullable=nullable, unique=unique, index=index)

def Column_as_Timedelta(name, default=None, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.Interval(), default=default, nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as_PrimaryKey(name, autoincrement=True):
    return sa.Column(name, sa.Integer(), primary_key=True, autoincrement=autoincrement)

def Column_as_ForeignKey(name, column, nullable=False, unique=False, index=False):
    return sa.Column(name, sa.ForeignKey(column), nullable=nullable, unique=unique, index=index)

"""------------------------------------------------------------------------------------------------
"""
def Column_as__id(autoincrement=True):
    return sa.Column('id', sa.Integer(), primary_key=True, autoincrement=autoincrement)

def Column_as__created_on(nullable=False, unique=False, index=False):
    return sa.Column('created_on', sa.DateTime(), default=dt.datetime.utcnow(), nullable=nullable, unique=unique, index=index)

def Column_as__updated_on(nullable=False, unique=False, index=False):
    return sa.Column('updated_on', sa.DateTime(), default=dt.datetime.utcnow(), onupdate=lambda: dt.datetime.utcnow(), nullable=nullable, unique=unique, index=index)