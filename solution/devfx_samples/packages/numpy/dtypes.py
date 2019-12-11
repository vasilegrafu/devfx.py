import numpy as np
import datetime as dt
import devfx.core as core

"""------------------------------------------------------------------------------------------------
"""
def as_dtype(arg, dtype):
    if(core.is_iterable(arg)):
        return np.asarray(arg, dtype=dtype)
    else:
        return np.asarray([arg], dtype=dtype)[0]


def as_int(arg):
    return as_dtype(arg, dtype=np.int)

def as_int8(arg):
    return as_dtype(arg, dtype=np.int8)

def as_int16(arg):
    return as_dtype(arg, dtype=np.int16)

def as_int32(arg):
    return as_dtype(arg, dtype=np.int32)

def as_int64(arg):
    return as_dtype(arg, dtype=np.int64)

def as_int128(arg):
    return as_dtype(arg, dtype=np.int128)


def as_uint(arg):
    return as_dtype(arg, dtype=np.uint)

def as_uint8(arg):
    return as_dtype(arg, dtype=np.uint8)

def as_uint16(arg):
    return as_dtype(arg, dtype=np.uint16)

def as_uint32(arg):
    return as_dtype(arg, dtype=np.uint32)

def as_uint64(arg):
    return as_dtype(arg, dtype=np.uint64)

def as_uint128(arg):
    return as_dtype(arg, dtype=np.uint128)


def as_float(arg):
    return as_dtype(arg, dtype=np.float)

def as_float16(arg):
    return as_dtype(arg, dtype=np.float16)

def as_float32(arg):
    return as_dtype(arg, dtype=np.float32)

def as_float64(arg):
    return as_dtype(arg, dtype=np.float64)

def as_float80(arg):
    return as_dtype(arg, dtype=np.float80)

def as_float128(arg):
    return as_dtype(arg, dtype=np.float128)

def as_float256(arg):
    return as_dtype(arg, dtype=np.float256)


def as_complex(arg):
    return as_dtype(arg, dtype=np.complex)

def as_complex32(arg):
    return as_dtype(arg, dtype=np.complex32)

def as_complex64(arg):
    return as_dtype(arg, dtype=np.complex64)

def as_complex128(arg):
    return as_dtype(arg, dtype=np.complex128)

def as_complex256(arg):
    return as_dtype(arg, dtype=np.complex256)

def as_complex512(arg):
    return as_dtype(arg, dtype=np.complex512)


def as_bool(arg):
    return as_dtype(arg, dtype=np.bool)


def as_datetime64(arg, dtu='us'):
    return as_dtype(arg, dtype='datetime64[{}]'.format(dtu))

def as_timedelta64(arg, dtu='us'):
    return as_dtype(arg, dtype='timedelta64[{}]'.format(dtu))


def as_str(arg):
    return as_dtype(arg, dtype=np.str)


def as_object(arg):
    return as_dtype(arg, dtype=np.object)


"""------------------------------------------------------------------------------------------------
"""
def to_type(arg, type):
    return arg.astype(type)

#----------------------------------------------------------------
def to_int(arg):
    return arg.astype(int)

def to_float(arg):
    return arg.astype(float)

def to_complex(arg):
    return arg.astype(complex)

def to_bool(arg):
    return arg.astype(bool)

def to_datetime(arg):
    arg.astype(dt.datetime)

def to_timedelta(arg):
    return arg.astype(dt.timedelta)

def to_str(arg):
    return arg.astype(str)

def to_object(arg):
    return arg.astype(object)
