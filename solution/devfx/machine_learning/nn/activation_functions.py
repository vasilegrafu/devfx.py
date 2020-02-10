import numpy as np
import tensorflow as tf
from .. import tensors
from .. import math

"""------------------------------------------------------------------------------------------------
"""
def identity(x):
    y = math.identity(x)
    return y

"""------------------------------------------------------------------------------------------------
"""
def binary(x):
    y = tensors.where(math.less(x, 0), 0, +1)
    return y

def sigmoid(x, L=1.0, s0=1.0/4.0):
    y = L*tf.nn.sigmoid((4.0*s0/L)*x)
    return y

def bipolar(x):
    y = tensors.where(math.less(x, 0), -1, +1)
    return y

def tanh(x, L=1.0, s0=1.0/4.0):
    y = L*tf.tanh((2.0*s0/(L+1.0))*x)
    return y

def softsign(x, L=1.0, s0=1.0/4.0):
    y = L*(s0/L)*(x/(1.0 + math.abs((s0/L)*x)))
    return y

# ---------------------------------------------------------------
def softmax(x, axis=-1):
    y = tf.nn.softmax(x, axis=axis)
    return y

# ---------------------------------------------------------------
def symlog(x, s0=1.0, b=np.e):
    d = 1.0/(s0*math.log(b))
    f = lambda x, d, b: math.log(x+d)/math.log(b) - math.log(d)/math.log(b)
    y = tensors.where(math.less(x, 0), -f(-math.clip_by_neginf_max(x, 0), d, b), f(math.clip_by_min_posinf(0, x), d, b))
    return y

def sympow(x, s0=1.0, n=2.0):
    d = math.pow(1.0/(s0*n), n/(n-1))
    f = lambda x, d, n: math.pow(x+d, 1.0/n) - math.pow(d, 1.0/n)
    y = tensors.where(math.less(x, 0), -f(-math.clip_by_neginf_max(x, 0), d, n), f(math.clip_by_min_posinf(0, x), d, n))
    return y

# ----------------------------------------------------------------
def softplus(x):
    y = tf.nn.softplus(x)
    return y

def relu(x, s0=1.0, a=1e-2):
    y = tensors.where(math.less(x, 0), a*math.clip_by_neginf_max(x, 0), s0*math.clip_by_min_posinf(0, x))
    return y

def elu(x):
    y = tensors.where(math.less(x, 0), math.exp(math.clip_by_neginf_max(x, 0)) - 1.0, math.clip_by_min_posinf(0, x))
    return y

def loglu(x, s0=1.0, b=np.e):
    d = 1.0/(s0*math.log(b))
    f = lambda x, d, b: math.log(x+d)/math.log(b) - math.log(d)/math.log(b)
    y = tensors.where(math.less(x, 0), -f(-math.clip_by_neginf_max(x, 0), d, b), s0*x)
    return y

def powlu(x, s0=1.0, n=2.0):
    d = math.pow(1.0/(s0*n), n/(n-1))
    f = lambda x, d, n: math.pow(x+d, 1.0/n) - math.pow(d, 1.0/n)
    y = tensors.where(math.less(x, 0), -f(-math.clip_by_neginf_max(x, 0), d, n), s0*x)
    return y

