import tensorflow as tf

"""------------------------------------------------------------------------------------------------
"""
bool = tf.bool

int8 = tf.int8
int16 = tf.int16
int32 = tf.int32
int64 = tf.int64

uint8 = tf.uint8
uint16 = tf.uint16

float16 = tf.float16
float32 = tf.float32
float64 = tf.float64

string = tf.string

"""------------------------------------------------------------------------------------------------
"""
def is_typeof(x, dtype): return x.dtype == dtype

def is_typeof_bool(x): return is_typeof(x, bool)

def is_typeof_int8(x): return is_typeof(x, int8)
def is_typeof_int16(x): return is_typeof(x, int16)
def is_typeof_int32(x): return is_typeof(x, int32)
def is_typeof_int64(x): return is_typeof(x, int64)

def is_typeof_uint8(x): return is_typeof(x, uint8)
def is_typeof_uint16(x): return is_typeof(x, uint16)

def is_typeof_float16(x): return is_typeof(x, float16)
def is_typeof_float32(x): return is_typeof(x, float32)
def is_typeof_float64(x): return is_typeof(x, float64)

def is_typeof_string(x): return is_typeof(x, string)

"""------------------------------------------------------------------------------------------------
"""
def cast(x, dtype, name=None):
    return tf.cast(x, dtype=dtype, name=name)


def cast_to_bool(tensor, name=None):
    return cast(tensor, dtype=bool, name=name)


def cast_to_int8(tensor, name=None):
    return cast(tensor, dtype=int8, name=name)

def cast_to_int16(tensor, name=None):
    return cast(tensor, dtype=int16, name=name)

def cast_to_int32(tensor, name=None):
    return cast(tensor, dtype=int32, name=name)

def cast_to_int64(tensor, name=None):
    return cast(tensor, dtype=int64, name=name)


def cast_to_uint8(tensor, name=None):
    return cast(tensor, dtype=uint8, name=name)

def cast_to_uint16(tensor, name=None):
    return cast(tensor, dtype=uint16, name=name)


def cast_to_float16(tensor, name=None):
    return cast(tensor, dtype=float16, name=name)

def cast_to_float32(tensor, name=None):
    return cast(tensor, dtype=float32, name=name)

def cast_to_float64(tensor, name=None):
    return cast(tensor, dtype=float64, name=name)


def cast_to_string(tensor, name=None):
    return cast(tensor, dtype=string, name=name)