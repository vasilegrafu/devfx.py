import tensorflow as tf
import devfx.reflection as refl
from . import types


"""------------------------------------------------------------------------------------------------
"""
def convert_to_tensor(value, dtype=None, name=None):
    return tf.convert_to_tensor(value, dtype=dtype, name=name)

"""------------------------------------------------------------------------------------------------
"""
def constant(value, shape=None, dtype=types.float32, name=None):
    return tf.constant(value, shape=shape, dtype=dtype, name=name)

def placeholder(shape=None, dtype=types.float32, name=None):
    return tf.placeholder(dtype, shape=shape, name=name)


"""------------------------------------------------------------------------------------------------
"""
def zeros(shape, dtype=types.float32, name=None):
    return tf.zeros(shape, dtype=dtype, name=name)

def zeros_like(tensor, dtype=None, name=None):
    return tf.zeros_like(tensor, dtype=dtype, name=name)

def ones(shape, dtype=types.float32, name=None):
    return tf.ones(shape, dtype=dtype, name=name)

def ones_like(tensor, dtype=None, name=None):
    return tf.ones_like(tensor, dtype=dtype, name=name)

def fill(shape, value, name=None):
    return tf.fill(shape, value, name=name)

def fill_like(tensor, value, name=None):
    return fill(shape(tensor), value, name=name)

"""------------------------------------------------------------------------------------------------
"""
def linspace(start, stop, n, dtype=types.float32, name=None):
    return tf.linspace(types.cast(start, dtype=dtype), types.cast(stop, dtype=dtype), n, name=name)

def range(start, stop, step, dtype=types.float32, name=None):
    return tf.range(start, limit=stop, delta=step, dtype=dtype, name=name)


"""------------------------------------------------------------------------------------------------
"""
def random_uniform(shape, min=0.0, max=None, dtype=types.float32, seed=None, name=None):
    return tf.random_uniform(shape, minval=min, maxval=max, dtype=dtype, seed=seed, name=name)

def random_normal(shape, mean=0.0, stddev=1.0, dtype=types.float32, seed=None, name=None):
    return tf.random_normal(shape, mean=mean, stddev=stddev, dtype=dtype, seed=seed, name=name)

def random_truncated_normal(shape, mean=0.0, stddev=1.0, dtype=types.float32, seed=None, name=None):
    return tf.truncated_normal(shape=shape, mean=mean, stddev=stddev, dtype=dtype, seed=seed, name=name)

"""------------------------------------------------------------------------------------------------
"""
def one_hot(indices, depth, on_value=None, off_value=None, axis=None, dtype=None, name=None):
    return tf.one_hot(indices, depth, on_value=on_value, off_value=off_value, axis=axis, dtype=dtype, name=name)

"""------------------------------------------------------------------------------------------------
"""
def shape(tensor, dtype=None, name=None):
    return tf.shape(tensor, name=name, out_type=dtype)

def rank(tensor, name=None):
    return tf.rank(tensor, name=name)

def size(tensor, dtype=None, name=None):
    return tf.size(tensor, name=name, out_type=dtype)

"""------------------------------------------------------------------------------------------------
"""
def reshape(tensor, shape, name=None):
    if(refl.is_iterable(shape)):
        shape = [(_ if _ is not None else -1) for _ in shape]
    return tf.reshape(tensor, shape, name=name)

def transpose(tensor, permutation=None, name=None):
    return tf.transpose(tensor, perm=permutation, name=name)

def pad(tensor, paddings, mode="CONSTANT", name=None):
    return tf.pad(tensor, paddings, mode=mode, name=name)

def reverse(tensor, axis, name=None):
    return tf.reverse(tensor, axis, name=name)

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

"""------------------------------------------------------------------------------------------------
"""
logical_not = tf.logical_not
logical_and = tf.logical_and
logical_or = tf.logical_or
logical_xor = tf.logical_xor

"""------------------------------------------------------------------------------------------------
"""
assign = tf.assign


