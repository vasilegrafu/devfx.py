import numpy as np
import tensorflow as tf
from . import types
from . import tensors

"""------------------------------------------------------------------------------------------------
"""
def is_finite(x, name=None):
    return tf.is_finite(x, name=name)

def is_inf(x, name=None):
    return tf.is_inf(x, name=name)

def is_neginf(x, name=None):
    return tf.equal(x, -np.inf, name=name)

def is_posinf(x, name=None):
    return tf.equal(x, +np.inf, name=name)

def is_nan(x, name=None):
    return tf.is_nan(x, name=name)

"""------------------------------------------------------------------------------------------------
"""
def clip_by_value(x, min, max, name=None):
    return tf.clip_by_value(x, min, max, name=name)


def clip_by_inf(x, name=None):
    return clip_by_value(x, x.dtype.min, x.dtype.max, name=name)

def clip_by_halfinf(x, name=None):
    return clip_by_value(x, x.dtype.min/2.0, x.dtype.max/2.0, name=name)

def clip_by_neginf_max(x, max, name=None):
    return clip_by_value(x, x.dtype.min, max, name=name)

def clip_by_neghalfinf_max(x, max, name=None):
    return clip_by_value(x, x.dtype.min/2.0, max, name=name)

def clip_by_min_posinf(min, x, name=None):
    return clip_by_value(x, min, x.dtype.max, name=name)

def clip_by_min_poshalfinf(min, x, name=None):
    return clip_by_value(x, min, x.dtype.max/2.0, name=name)

"""------------------------------------------------------------------------------------------------
"""
add = tf.add
add_n = tf.add_n
subtract = tf.subtract
multiply = tf.multiply
scalar_multiply = tf.scalar_mul
divide = tf.divide
mod = tf.mod

"""------------------------------------------------------------------------------------------------
"""
min = tf.minimum
max = tf.maximum

argmin = tf.argmin
argmax = tf.argmax

"""------------------------------------------------------------------------------------------------
"""
cumulative_sum = tf.cumsum
cumulative_product = tf.cumprod

"""------------------------------------------------------------------------------------------------
"""
def reduce_sum(x, axis=None, keepdims=False, name=None):
    return tf.reduce_sum(x, axis=axis, keepdims=keepdims, name=name)

def reduce_prod(x, axis=None, keep_dims=False, name=None):
    return tf.reduce_prod(x, axis=axis, keep_dims=keep_dims, name=name)

def reduce_min(x, axis=None, keep_dims=False, name=None):
    return tf.reduce_min(x, axis=axis, keep_dims=keep_dims, name=name)

def reduce_max(x, axis=None, keep_dims=False, name=None):
    return tf.reduce_max(x, axis=axis, keep_dims=keep_dims, name=name)

def reduce_all(x, axis=None, keep_dims=False, name=None):
    return tf.reduce_all(x, axis=axis, keep_dims=keep_dims, name=name)

def reduce_any(x, axis=None, keep_dims=False, name=None):
    return tf.reduce_any(x, axis=axis, keep_dims=keep_dims, name=name)


def reduce_mean(x, axis=None, keepdims=False):
    return tf.reduce_mean(x, axis=axis, keepdims=keepdims)

def reduce_var(x, axis=None, keep_dims=False):
    mean = reduce_mean(x, axis=axis, keepdims=True)
    return reduce_mean(square(x - mean), axis=axis, keepdims=keep_dims)

def reduce_std(x, axis=None, keep_dims=False):
    return sqrt(reduce_var(x, axis=axis, keep_dims=keep_dims))

"""------------------------------------------------------------------------------------------------
"""
sign = tf.sign
reciprocal = tf.reciprocal
round = tf.round
ceil = tf.ceil
floor = tf.floor

"""------------------------------------------------------------------------------------------------
"""
identity = tf.identity
exp = tf.exp
log = tf.log
abs = tf.abs
sqrt = tf.sqrt
square = tf.square
pow = tf.pow
sin = tf.sin
cos = tf.cos
arcsin = tf.asin
arccos = tf.acos
tan = tf.tan
arctan = tf.atan

"""------------------------------------------------------------------------------------------------
"""
matrix_eye = tf.eye
matrix_determinant = tf.matrix_determinant
matrix_transpose = tf.matrix_transpose
matrix_inverse = tf.matrix_inverse
matrix_multiply = tf.matmul

"""------------------------------------------------------------------------------------------------
"""
def tensordot(a, b, axes, dtype=None, name=None):
    if(dtype is None):
        return tf.tensordot(a=a, b=b, axes=axes, name=name)
    else:
        return tf.tensordot(a=tf.cast(a, dtype), b=tf.cast(b, dtype), axes=axes, name=name)

einsum = tf.einsum


"""------------------------------------------------------------------------------------------------
"""
def iverson(condition, dtype=None):
    if (dtype is None):
        return tensors.where(condition, tensors.ones_like(condition), tensors.zeros_like(condition))
    else:
        return tensors.where(condition, types.cast(tensors.ones_like(condition), dtype), types.cast(tensors.zeros_like(condition), dtype))

def macaulay(x, dtype=None):
    if (dtype is None):
        return tensors.where(tensors.greater_equal(x, 0), x, tensors.zeros_like(x))
    else:
        return tensors.where(tensors.greater_equal(x, 0), types.cast(x, dtype), types.cast(tensors.zeros_like(x), dtype))

def kronecker(x_i, x_j, dtype=None):
    return iverson(tensors.equal(x_i, x_j), dtype=dtype)



