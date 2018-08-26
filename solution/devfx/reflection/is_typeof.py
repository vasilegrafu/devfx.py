import devfx.exceptions as exceptions
from builtins import bool
from datetime import date, time, datetime, timedelta
from calendar import calendar
from enum import Enum
from builtins import int, float, complex
from fractions import Fraction
from decimal import Decimal
from builtins import str
from builtins import tuple, list, set, dict, range, bytes
from collections import Generator, namedtuple, deque
from types import FunctionType
from types import LambdaType
from types import MethodType
from .is_instance import is_instance
from .is_class_or_subclass import is_class_or_subclass

"""------------------------------------------------------------------------------------------------
"""
def is_typeof(arg, classinfo):
    if(is_instance(arg, object) and not is_instance(arg, type)):
        return is_instance(arg, classinfo)
    if(is_instance(arg, type)):
        return is_class_or_subclass(arg, classinfo)
    raise exceptions.NotSupportedError()

"""------------------------------------------------------------------------------------------------
"""
def is_typeof_bool(arg): return is_typeof(arg, bool)

def is_typeof_date(arg): return is_typeof(arg, date)
def is_typeof_time(arg): return is_typeof(arg, time)
def is_typeof_datetime(arg): return is_typeof(arg, datetime)
def is_typeof_timedelta(arg): return is_typeof(arg, timedelta)
def is_typeof_calendar(arg): return is_typeof(arg, calendar)

def is_typeof_enum(arg): return is_typeof(arg, Enum)

def is_typeof_int(arg): return is_typeof(arg, int)
def is_typeof_fraction(arg): return is_typeof(arg, Fraction)
def is_typeof_decimal(arg): return is_typeof(arg, Decimal)
def is_typeof_float(arg): return is_typeof(arg, float)
def is_typeof_complex(arg): return is_typeof(arg, complex)

def is_typeof_str(arg): return is_typeof(arg, str)

def is_typeof_tuple(arg): return is_typeof(arg, tuple)
def is_typeof_list(arg): return is_typeof(arg, list)
def is_typeof_generator(arg): return is_typeof(arg, Generator)
def is_typeof_set(arg): return is_typeof(arg, set)
def is_typeof_dict(arg): return is_typeof(arg, dict)
def is_typeof_range(arg): return is_typeof(arg, range)
def is_typeof_slice(arg): return is_typeof(arg, slice)
def is_typeof_namedtuple(arg): return is_typeof(arg, namedtuple)
def is_typeof_deque(arg): return is_typeof(arg, deque)
def is_typeof_bytes(arg): return is_typeof(arg, bytes)

def is_typeof_function(arg): return is_typeof(arg, FunctionType)
def is_typeof_lambda(arg): return is_typeof(arg, LambdaType)
def is_typeof_method(arg): return is_typeof(arg, MethodType)




   

    

