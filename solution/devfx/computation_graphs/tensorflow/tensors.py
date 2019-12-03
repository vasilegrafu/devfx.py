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
    return tf.constant(value=value, shape=shape, dtype=dtype, name=name)

def fill(value, shape=None, dtype=types.float32, name=None):
    return tf.cast(tf.fill(dims=shape, value=value, name=name), dtype=dtype)


"""------------------------------------------------------------------------------------------------
"""
def zeros(shape, dtype=types.float32, name=None):
    return tf.zeros(shape=shape, dtype=dtype, name=name)

def zeros_like(input, dtype=None, name=None):
    return tf.zeros_like(input=input, dtype=dtype, name=None)  

def ones(shape, dtype=types.float32, name=None):
    return tf.ones(shape=shape, dtype=dtype, name=name)

def ones_like(input, dtype=None, name=None):
    return tf.ones_like(input=input, dtype=dtype, name=None)  

"""------------------------------------------------------------------------------------------------
"""
def linspace(start, stop, n, name=None):
    return tf.linspace(start=start, stop=stop, num=n, name=name)

def range(start, stop, step=1, dtype=types.int32, name=None):
    return tf.range(start, limit=stop, delta=step, dtype=dtype, name=name)


"""------------------------------------------------------------------------------------------------
"""
def random_uniform(shape, min=0.0, max=None, dtype=types.float32, seed=None, name=None):
    return tf.random.uniform(shape, minval=min, maxval=max, dtype=dtype, seed=seed, name=name)

def random_normal(shape, mean=0.0, stddev=1.0, dtype=types.float32, seed=None, name=None):
    return tf.random.normal(shape, mean=mean, stddev=stddev, dtype=dtype, seed=seed, name=name)

def random_truncated_normal(shape, mean=0.0, stddev=1.0, dtype=types.float32, seed=None, name=None):
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
    if(refl.is_iterable(shape)):
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






