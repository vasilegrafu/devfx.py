import devfx.exceptions as exceps
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

def is_typeof(arg, classinfo):
    if(is_instance(arg, object)):
        return is_instance(arg, classinfo)
    if(is_instance(arg, type)):
        return is_class_or_subclass(arg, classinfo)
    raise exceps.NotSupportedError()





   

    

