import tensorflow as tf
import inspect as insp
import functools as fnt
import devfx.core as core
import devfx.exceptions as exceps

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

"""------------------------------------------------------------------------------------------------
"""
def as_tensor(value, dtype=None, shape=None):
    if((dtype is None) and (shape is None)):
        raise exceps.ArgumentError()
    if(dtype is not None):
        value = convert_to_tensor(value, dtype_hint=dtype)
        if(value.dtype != dtype):
            value = cast(value, dtype=dtype)
    if(shape is not None):
        value = reshape(value, shape=shape)
    return value

def output_as_tensor(targ):
    def _(fn):
        @fnt.wraps(fn)
        def __(*args, **kwargs):
            output = fn(*args, **kwargs)
            output = as_tensor(output, dtype=targ[0], shape=targ[1])
            return output
        return __
    return _

def input_as_tensor(**tkwargs):
    def _(fn):
        signature = insp.signature(fn)
        @fnt.wraps(fn)
        def __(*args, **kwargs):
            bound_arguments = signature.bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            for tkarg in tkwargs.keys():
                bound_arguments.arguments[tkarg] = as_tensor(bound_arguments.arguments[tkarg], dtype=tkwargs[tkarg][0], shape=tkwargs[tkarg][1])
            output = fn(*bound_arguments.args, **bound_arguments.kwargs)
            return output
        return __
    return _

"""------------------------------------------------------------------------------------------------
"""
def build_graph(**tkwargs):
    def _(fn):
        signature = insp.signature(fn)
        parameters = signature.parameters
        if('self' not in signature.parameters):
            @fnt.wraps(fn)
            @tf.function(input_signature=[tf.TensorSpec(dtype=tkwargs[parameter][0], shape=tkwargs[parameter][1]) for parameter in parameters.keys()])
            def __(*args, **kwargs):
                output = fn(*args, **kwargs)
                return output
            return __
        if('self' in signature.parameters):
            @fnt.wraps(fn)
            @tf.function(input_signature=[tf.TensorSpec(dtype=tkwargs[parameter][0], shape=tkwargs[parameter][1]) for parameter in parameters.keys() if parameter != 'self'])
            def __(self, *args, **kwargs):
                output = fn(self, *args, **kwargs)
                return output
            return __
        raise exceps.NotSupportedError()
    return _

"""------------------------------------------------------------------------------------------------
"""
def convert_to_tensor(value, dtype=None, dtype_hint=None, name=None):
    return tf.convert_to_tensor(value, dtype=dtype, dtype_hint=dtype_hint, name=name)


"""------------------------------------------------------------------------------------------------
"""
def constant(value, shape=None, dtype=float32, name=None):
    return tf.constant(value=value, shape=shape, dtype=dtype, name=name)

def fill(value, shape=None, dtype=float32, name=None):
    return tf.cast(tf.fill(dims=shape, value=value, name=name), dtype=dtype)


"""------------------------------------------------------------------------------------------------
"""
def zeros(shape, dtype=float32, name=None):
    return tf.zeros(shape=shape, dtype=dtype, name=name)

def zeros_like(input, dtype=None, name=None):
    return tf.zeros_like(input=input, dtype=dtype, name=None)  

def ones(shape, dtype=float32, name=None):
    return tf.ones(shape=shape, dtype=dtype, name=name)

def ones_like(input, dtype=None, name=None):
    return tf.ones_like(input=input, dtype=dtype, name=None)  

"""------------------------------------------------------------------------------------------------
"""
def linspace(start, stop, n, name=None):
    return tf.linspace(start=start, stop=stop, num=n, name=name)

def range(start, stop, step=1, dtype=int32, name=None):
    return tf.range(start, limit=stop, delta=step, dtype=dtype, name=name)


"""------------------------------------------------------------------------------------------------
"""
def random_uniform(shape, min=0.0, max=None, dtype=float32, seed=None, name=None):
    return tf.random.uniform(shape, minval=min, maxval=max, dtype=dtype, seed=seed, name=name)

def random_normal(shape, mean=0.0, stddev=1.0, dtype=float32, seed=None, name=None):
    return tf.random.normal(shape, mean=mean, stddev=stddev, dtype=dtype, seed=seed, name=name)

def random_truncated_normal(shape, mean=0.0, stddev=1.0, dtype=float32, seed=None, name=None):
    return tf.random.truncated_normal(shape=shape, mean=mean, stddev=stddev, dtype=dtype, seed=seed, name=name)

"""------------------------------------------------------------------------------------------------
"""
def one_hot(indices, depth, on_value=None, off_value=None, axis=None, dtype=None, name=None):
    return tf.one_hot(indices, depth, on_value=on_value, off_value=off_value, axis=axis, dtype=dtype, name=name)

"""------------------------------------------------------------------------------------------------
"""
def shape(tensor, name=None):
    return tf.shape(tensor, name=name)

def rank(tensor, name=None):
    return tf.rank(tensor, name=name)

def size(tensor, name=None):
    return tf.size(tensor, name=name)

"""------------------------------------------------------------------------------------------------
"""
def reshape(tensor, shape, name=None):
    if(core.is_iterable(shape)):
        shape = [(_ if _ is not None else -1) for _ in shape]
    return tf.reshape(tensor, shape, name=name)

"""------------------------------------------------------------------------------------------------
"""
def tile(tensor, multiples, name=None):
    return tf.tile(tensor, multiples, name=name)

def slice(tensor, begin, size, name=None):
    return tf.slice(tensor, begin, size, name=name)

def split(tensor, number_or_size_splits, axis=0, name=None):
    return tf.split(tensor, number_or_size_splits, axis=axis, num=None, name=name)

def stack(tensors, axis=0, name=None):
    return tf.stack(tensors, axis=axis, name=name)

def unstack(tensor, axis=0, name=None):
    return tf.unstack(tensor, num=None, axis=axis, name=name)

def concatenate(tensors, axis=0, name=None):
    return tf.concat(values=tensors, axis=axis, name=name)

"""------------------------------------------------------------------------------------------------
"""
def where(condition, x=None, y=None, name=None):
    return tf.where(condition, x=x, y=y, name=name)

"""------------------------------------------------------------------------------------------------
"""
equal = tf.equal
not_equal = tf.not_equal
less = tf.less
less_equal = tf.less_equal
greater = tf.greater
greater_equal = tf.greater_equal






