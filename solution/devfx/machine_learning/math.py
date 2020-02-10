import numpy as np
import tensorflow as tf
from . import types
from . import tensors
from . import math

"""------------------------------------------------------------------------------------------------
"""
def is_finite(x, name=None):
    return tf.math.is_finite(x, name=name)

def is_inf(x, name=None):
    return tf.math.is_inf(x, name=name)

def is_neginf(x, name=None):
    return tf.math.equal(x, -np.inf, name=name)

def is_posinf(x, name=None):
    return tf.equal(x, +np.inf, name=name)

def is_nan(x, name=None):
    return tf.math.is_nan(x, name=name)

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
def equal(x, y, name=None):
    return tf.math.equal(x, y, name=None)

def not_equal(x, y, name=None):
    return tf.math.not_equal(x, y, name=None)

def less(x, y, name=None):
    return tf.math.less(x, y, name=None)

def less_equal(x, y, name=None):
    return tf.math.less_equal(x, y, name=None)


def greater(x, y, name=None):
    return tf.math.greater(x, y, name=None)

def greater_equal(x, y, name=None):
    return tf.math.greater_equal(x, y, name=None)

"""------------------------------------------------------------------------------------------------
"""
def logical_not(x, y, name=None):
    return tf.math.logical_not(x, y, name=None)

def logical_and(x, y, name=None):
    return tf.math.logical_and(x, y, name=None)

def logical_or(x, y, name=None):
    return tf.math.logical_or(x, y, name=None)

def logical_xor(x, y, name=None):
    return tf.math.logical_xor(x, y, name=None)

"""------------------------------------------------------------------------------------------------
"""
def add(x, y, name=None):
    return tf.math.add(x, y, name=None)

def add_n(tensors, name=None):
    return tf.math.add_n(tensors, name=None)


def subtract(x, y, name=None):
    return tf.math.subtract(x, y, name=None)


def multiply(x, y, name=None):
    return tf.math.multiply(x, y, name=None)

def scalar_multiply(scalar, x, name=None):
    return tf.math.scalar_mul(scalar, x, name=None)


def divide(x, y, name=None):
    return tf.math.divide(x, y, name=None)

def mod(x, y, name=None):
    return tf.math.mod(x, y, name=None)

"""------------------------------------------------------------------------------------------------
"""
def min(x, y, name=None):
    return tf.math.minimum(x, y, name=None)

def max(x, y, name=None):
    return tf.math.maximum(x, y, name=None)


def argmin(tensor, axis=None, dtype=types.int32, name=None):
    return tf.math.argmin(tensor, axis=axis, output_type=dtype, name=name)

def argmax(tensor, axis=None, dtype=types.int32, name=None):
    return tf.math.argmax(tensor, axis=axis, output_type=dtype, name=name)

"""------------------------------------------------------------------------------------------------
"""
def cumulative_sum(x, axis=0, reverse=False, name=None):
    return tf.math.cumsum(x, axis=axis, reverse=reverse, name=name)

def cumulative_product(x, axis=0, reverse=False, name=None):
    return tf.math.cumprod(x, axis=axis, reverse=reverse, name=name)

"""------------------------------------------------------------------------------------------------
"""
def reduce_sum(x, axis=None, keepdims=False, name=None):
    return tf.math.reduce_sum(x, axis=axis, keepdims=keepdims, name=name)

def reduce_prod(x, axis=None, keepdims=False, name=None):
    return tf.math.reduce_prod(x, axis=axis, keepdims=keepdims, name=name)

def reduce_min(x, axis=None, keepdims=False, name=None):
    return tf.math.reduce_min(x, axis=axis, keepdims=keepdims, name=name)

def reduce_max(x, axis=None, keepdims=False, name=None):
    return tf.math.reduce_max(x, axis=axis, keepdims=keepdims, name=name)

def reduce_all(x, axis=None, keepdims=False, name=None):
    return tf.math.reduce_all(x, axis=axis, keepdims=keepdims, name=name)

def reduce_any(x, axis=None, keepdims=False, name=None):
    return tf.math.reduce_any(x, axis=axis, keepdims=keepdims, name=name)


def reduce_mean(x, axis=None, keepdims=False):
    return tf.math.reduce_mean(x, axis=axis, keepdims=keepdims)

def reduce_var(x, axis=None, keepdims=False):
    return tf.math.reduce_variance(x, axis=axis, keepdims=keepdims)

def reduce_std(x, axis=None, keepdims=False):
    return tf.math.reduce_std(x, axis=axis, keepdims=keepdims)

"""------------------------------------------------------------------------------------------------
"""
sign = tf.math.sign
reciprocal = tf.math.reciprocal
round = tf.math.round
ceil = tf.math.ceil
floor = tf.math.floor

"""------------------------------------------------------------------------------------------------
"""
identity = tf.identity
exp = tf.math.exp
log = tf.math.log
abs = tf.math.abs
sqrt = tf.math.sqrt
square = tf.math.square
pow = tf.math.pow
sin = tf.math.sin
arcsin = tf.math.asin
cos = tf.math.cos
arccos = tf.math.acos
tan = tf.math.tan
arctan = tf.math.atan

"""------------------------------------------------------------------------------------------------
"""
matrix_eye = tf.eye
matrix_determinant = tf.linalg.det
matrix_transpose = tf.linalg.matrix_transpose
matrix_inverse = tf.linalg.inv
matrix_multiply = tf.linalg.matmul

"""------------------------------------------------------------------------------------------------
"""
def tensordot(a, b, axes, dtype=None, name=None):
    if(dtype is None):
        return tf.tensordot(a=a, b=b, axes=axes, name=name)
    else:
        return tf.tensordot(a=tf.cast(a, dtype), b=tf.cast(b, dtype), axes=axes, name=name)

def einsum(equation, *inputs, **kwargs):
    return tf.einsum(equation, *inputs, **kwargs)

"""------------------------------------------------------------------------------------------------
"""
def sigmoid(x, name=None):
    y = tf.math.sigmoid(x, name=name)
    return y

def softmax(x, axis=None, name=None):
    y = tf.nn.softmax(x, axis=axis,  name=name)
    return y

"""------------------------------------------------------------------------------------------------
"""
def iverson(condition, dtype=types.int32):
    return tensors.where(condition, tensors.ones_like(condition, dtype=dtype), tensors.zeros_like(condition, dtype=dtype))
        

def macaulay(x, dtype=types.int32):
    if (dtype is None):
        return tensors.where(tensors.greater_equal(x, 0), x, tensors.zeros_like(x))
    else:
        return tensors.where(tensors.greater_equal(x, 0), tensors.cast(x, dtype), tensors.zeros_like(x, dtype=dtype))

def kronecker(x_i, x_j, dtype=types.int32):
    return iverson(math.equal(x_i, x_j), dtype=dtype)



